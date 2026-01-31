#!/usr/bin/env python3
"""
=============================================================================
STEP 3: 오디오 생성기 (Google Cloud TTS + Grok 음악 제안)
=============================================================================
이 모듈은:
- Google Cloud TTS로 대사/나레이션 음성 생성
- 효과음 라이브러리 매칭
- BGM 추천 (Grok 활용)
- 오디오 믹싱 준비
"""

import os
import json
import base64
import requests
from pathlib import Path
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import time
import subprocess


@dataclass
class AudioClip:
    """오디오 클립 정보"""
    clip_id: str
    clip_type: str  # 'dialogue', 'narration', 'sfx', 'bgm'
    text: Optional[str]
    file_path: str
    duration_seconds: float
    scene_number: int
    metadata: Dict[str, Any]


class GoogleTTSGenerator:
    """Google Cloud Text-to-Speech 생성기"""
    
    def __init__(self, 
                 api_key: Optional[str] = None,
                 output_dir: str = "audio"):
        
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GOOGLE_TTS_API_KEY")
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # TTS API 엔드포인트
        self.tts_url = "https://texttospeech.googleapis.com/v1/text:synthesize"
        
        # 음성 프리셋 (애니메이션용)
        self.voice_presets = {
            "young_female": {
                "languageCode": "ko-KR",
                "name": "ko-KR-Wavenet-A",
                "ssmlGender": "FEMALE"
            },
            "young_male": {
                "languageCode": "ko-KR", 
                "name": "ko-KR-Wavenet-C",
                "ssmlGender": "MALE"
            },
            "narrator": {
                "languageCode": "ko-KR",
                "name": "ko-KR-Wavenet-B",
                "ssmlGender": "FEMALE"
            },
            "deep_male": {
                "languageCode": "ko-KR",
                "name": "ko-KR-Wavenet-D",
                "ssmlGender": "MALE"
            },
            # 일본어 음성 (애니메이션 느낌)
            "anime_female_jp": {
                "languageCode": "ja-JP",
                "name": "ja-JP-Wavenet-B",
                "ssmlGender": "FEMALE"
            },
            "anime_male_jp": {
                "languageCode": "ja-JP",
                "name": "ja-JP-Wavenet-D",
                "ssmlGender": "MALE"
            }
        }
        
        # 오디오 설정
        self.audio_config = {
            "audioEncoding": "MP3",
            "speakingRate": 1.0,  # 속도 (0.25 ~ 4.0)
            "pitch": 0.0,        # 피치 (-20.0 ~ 20.0)
            "volumeGainDb": 0.0  # 볼륨 (-96.0 ~ 16.0)
        }
    
    def generate_speech(self,
                        text: str,
                        voice_style: str = "narrator",
                        scene_number: int = 0,
                        clip_type: str = "dialogue",
                        speaking_rate: float = 1.0,
                        pitch: float = 0.0) -> Optional[AudioClip]:
        """텍스트를 음성으로 변환"""
        
        if not text or not text.strip():
            return None
        
        print(f"   🎤 음성 생성: '{text[:30]}...' ({voice_style})")
        
        # 음성 선택
        voice = self.voice_presets.get(voice_style, self.voice_presets["narrator"])
        
        # 오디오 설정
        audio_config = self.audio_config.copy()
        audio_config["speakingRate"] = speaking_rate
        audio_config["pitch"] = pitch
        
        # SSML로 감정 표현 추가
        ssml_text = self._add_ssml_emotion(text, clip_type)
        
        payload = {
            "input": {"ssml": ssml_text},
            "voice": voice,
            "audioConfig": audio_config
        }
        
        # API 호출
        if self.api_key:
            url = f"{self.tts_url}?key={self.api_key}"
        else:
            # API 키 없으면 시뮬레이션
            return self._simulate_audio(text, scene_number, clip_type, voice_style)
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                audio_content = base64.b64decode(result["audioContent"])
                
                # 파일 저장
                clip_id = f"{clip_type}_{scene_number:03d}_{int(time.time())}"
                file_path = self.output_dir / f"{clip_id}.mp3"
                
                with open(file_path, 'wb') as f:
                    f.write(audio_content)
                
                # 오디오 길이 추정 (대략 150 단어/분)
                word_count = len(text.split())
                duration = (word_count / 150) * 60 * (1 / speaking_rate)
                
                return AudioClip(
                    clip_id=clip_id,
                    clip_type=clip_type,
                    text=text,
                    file_path=str(file_path),
                    duration_seconds=duration,
                    scene_number=scene_number,
                    metadata={
                        "voice_style": voice_style,
                        "speaking_rate": speaking_rate,
                        "pitch": pitch,
                        "language": voice["languageCode"]
                    }
                )
            else:
                print(f"   ⚠️ TTS API 오류: {response.status_code}")
                return self._simulate_audio(text, scene_number, clip_type, voice_style)
                
        except Exception as e:
            print(f"   ⚠️ TTS 오류: {e}")
            return self._simulate_audio(text, scene_number, clip_type, voice_style)
    
    def _add_ssml_emotion(self, text: str, clip_type: str) -> str:
        """SSML 마크업으로 감정 표현 추가"""
        
        # 기본 SSML 래퍼
        ssml = f'<speak>{text}</speak>'
        
        # 나레이션은 천천히, 대사는 자연스럽게
        if clip_type == "narration":
            ssml = f'<speak><prosody rate="95%">{text}</prosody></speak>'
        elif clip_type == "dialogue":
            # 느낌표는 강조, 물음표는 톤 올림
            if "!" in text:
                ssml = f'<speak><prosody pitch="+2st" rate="105%">{text}</prosody></speak>'
            elif "?" in text:
                ssml = f'<speak><prosody pitch="+1st">{text}</prosody></speak>'
        
        return ssml
    
    def _simulate_audio(self, text: str, scene_number: int, 
                        clip_type: str, voice_style: str) -> AudioClip:
        """API 없을 때 시뮬레이션 (메타데이터만 생성)"""
        
        clip_id = f"{clip_type}_{scene_number:03d}_{int(time.time())}"
        
        # 스크립트 파일 저장 (나중에 TTS 처리용)
        script_path = self.output_dir / f"{clip_id}_script.txt"
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(f"Voice: {voice_style}\n")
            f.write(f"Type: {clip_type}\n")
            f.write(f"Text: {text}\n")
        
        # 대략적인 길이 추정
        word_count = len(text.split())
        duration = max(1.0, (word_count / 150) * 60)
        
        return AudioClip(
            clip_id=clip_id,
            clip_type=clip_type,
            text=text,
            file_path=str(script_path),
            duration_seconds=duration,
            scene_number=scene_number,
            metadata={
                "voice_style": voice_style,
                "simulated": True,
                "note": "API 키 없음 - 스크립트만 저장됨"
            }
        )


class SoundEffectManager:
    """효과음 관리자"""
    
    # 무료 효과음 소스 매핑
    FREE_SFX_SOURCES = {
        "wind": "https://freesound.org/search/?q=wind",
        "footsteps": "https://freesound.org/search/?q=footsteps",
        "magic": "https://freesound.org/search/?q=magic+spell",
        "sword": "https://freesound.org/search/?q=sword+slash",
        "explosion": "https://freesound.org/search/?q=explosion",
        "rain": "https://freesound.org/search/?q=rain+ambient",
        "fire": "https://freesound.org/search/?q=fire+crackling",
        "bells": "https://freesound.org/search/?q=bells",
        "door": "https://freesound.org/search/?q=door+creak",
        "crowd": "https://freesound.org/search/?q=crowd+murmur"
    }
    
    def __init__(self, output_dir: str = "audio/sfx"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.sfx_list = []
    
    def suggest_sfx(self, scene_effects: List[str], scene_number: int) -> List[dict]:
        """장면에 필요한 효과음 제안"""
        
        suggestions = []
        
        for effect in scene_effects:
            effect_lower = effect.lower()
            
            # 키워드 매칭
            matched_source = None
            for keyword, source_url in self.FREE_SFX_SOURCES.items():
                if keyword in effect_lower:
                    matched_source = source_url
                    break
            
            suggestion = {
                "scene_number": scene_number,
                "effect_name": effect,
                "suggested_source": matched_source or f"https://freesound.org/search/?q={effect.replace(' ', '+')}",
                "timing": "match with visual",
                "volume": "0.3-0.5 (배경음)"
            }
            suggestions.append(suggestion)
        
        return suggestions
    
    def generate_sfx_sheet(self, all_scenes: List[dict]) -> str:
        """전체 효과음 시트 생성"""
        
        sheet = """
╔══════════════════════════════════════════════════════════════╗
║           🔊 효과음 (SFX) 수집 가이드                          ║
╚══════════════════════════════════════════════════════════════╝

📌 무료 효과음 소스:
• Freesound.org (무료, 로그인 필요)
• Pixabay.com/sound-effects (무료, 상업용 가능)
• Mixkit.co/free-sound-effects (무료)
• YouTube Audio Library (YouTube Studio에서 접근)

📌 장면별 필요 효과음:
"""
        for scene in all_scenes:
            effects = scene.get("sound_effects", [])
            if effects:
                sheet += f"\n장면 {scene.get('scene_number', '?'):03d}: {', '.join(effects)}"
        
        sheet += """

📌 효과음 팁:
• 볼륨은 대사/나레이션보다 낮게 (30-50%)
• 페이드 인/아웃 사용하여 자연스럽게
• 여러 레이어 겹치면 풍성한 사운드스케이프
"""
        return sheet


class GrokMusicAdvisor:
    """Grok을 활용한 BGM 추천"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GROK_API_KEY") or os.getenv("XAI_API_KEY")
        self.base_url = "https://api.x.ai/v1"
    
    def suggest_bgm(self, 
                    scene_mood: str,
                    scene_description: str,
                    genre: str = "anime") -> dict:
        """장면에 맞는 BGM 추천"""
        
        if not self.api_key:
            return self._default_suggestion(scene_mood)
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": "grok-beta",
            "messages": [
                {
                    "role": "system",
                    "content": """You are a music director for anime. 
Suggest background music for scenes based on mood and description.
Respond in JSON format with:
- mood_category: (action/emotional/peaceful/mysterious/comedic/epic)
- tempo: (slow/medium/fast)
- instruments: [list of suggested instruments]
- reference_tracks: [similar anime OST examples]
- royalty_free_search: search keywords for royalty-free music sites"""
                },
                {
                    "role": "user",
                    "content": f"Scene mood: {scene_mood}\nDescription: {scene_description}\nGenre: {genre}"
                }
            ],
            "max_tokens": 300
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            if response.status_code == 200:
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                
                # JSON 파싱 시도
                try:
                    json_start = content.find('{')
                    json_end = content.rfind('}') + 1
                    if json_start != -1:
                        return json.loads(content[json_start:json_end])
                except:
                    pass
                
                return {"raw_suggestion": content}
                
        except Exception as e:
            print(f"Grok API 오류: {e}")
        
        return self._default_suggestion(scene_mood)
    
    def _default_suggestion(self, mood: str) -> dict:
        """기본 BGM 제안"""
        
        mood_mapping = {
            "우울": {"category": "emotional", "tempo": "slow", "search": "sad piano anime"},
            "희망": {"category": "emotional", "tempo": "medium", "search": "hopeful orchestral anime"},
            "긴장": {"category": "mysterious", "tempo": "medium", "search": "suspense tension anime"},
            "전투": {"category": "action", "tempo": "fast", "search": "epic battle orchestral"},
            "평화": {"category": "peaceful", "tempo": "slow", "search": "peaceful ambient anime"},
            "신비": {"category": "mysterious", "tempo": "slow", "search": "mysterious fantasy anime"},
            "슬픔": {"category": "emotional", "tempo": "slow", "search": "sad emotional piano"},
            "기쁨": {"category": "comedic", "tempo": "medium", "search": "happy cheerful anime"}
        }
        
        for key, value in mood_mapping.items():
            if key in mood.lower():
                return {
                    "mood_category": value["category"],
                    "tempo": value["tempo"],
                    "royalty_free_search": value["search"],
                    "suggested_sources": [
                        "https://pixabay.com/music/search/anime/",
                        "https://www.youtube.com/audiolibrary",
                        "https://incompetech.com/music/"
                    ]
                }
        
        return {
            "mood_category": "general",
            "tempo": "medium",
            "royalty_free_search": "anime background music",
            "suggested_sources": ["https://pixabay.com/music/"]
        }
    
    def generate_music_guide(self, scenes: List[dict]) -> str:
        """전체 BGM 가이드 생성"""
        
        guide = """
╔══════════════════════════════════════════════════════════════╗
║           🎵 BGM (배경음악) 가이드                             ║
╚══════════════════════════════════════════════════════════════╝

📌 무료 BGM 소스:
• Pixabay Music (https://pixabay.com/music/) - 상업용 무료
• YouTube Audio Library - YouTube 크리에이터용
• Incompetech (https://incompetech.com) - Kevin MacLeod 음악
• Free Music Archive (https://freemusicarchive.org)

📌 장면별 BGM 추천:
"""
        for scene in scenes:
            mood = scene.get("mood", "neutral")
            suggestion = self.suggest_bgm(mood, scene.get("description", ""))
            
            guide += f"""
─────────────────────────────────────────────────
장면 {scene.get('scene_number', '?'):03d} | 분위기: {mood}
─────────────────────────────────────────────────
• 카테고리: {suggestion.get('mood_category', 'N/A')}
• 템포: {suggestion.get('tempo', 'N/A')}
• 검색어: {suggestion.get('royalty_free_search', 'anime bgm')}
"""
        
        guide += """
📌 BGM 사용 팁:
• 대사가 있는 장면: BGM 볼륨 20-30%
• 나레이션 장면: BGM 볼륨 30-40%
• 액션/전환: BGM 볼륨 50-70%
• 장면 전환 시 크로스페이드 사용 (1-2초)
"""
        return guide


def process_script_for_audio(script_path: str, output_dir: str = "/home/claude/anime-pipeline"):
    """스크립트에서 오디오 생성"""
    
    with open(script_path, 'r', encoding='utf-8') as f:
        script = json.load(f)
    
    # 생성기 초기화
    tts_gen = GoogleTTSGenerator(output_dir=f"{output_dir}/audio")
    sfx_manager = SoundEffectManager(output_dir=f"{output_dir}/audio/sfx")
    music_advisor = GrokMusicAdvisor()
    
    print("=" * 60)
    print("🎵 오디오 생성 파이프라인 시작")
    print("=" * 60)
    
    all_audio_clips = []
    all_sfx_suggestions = []
    
    # 캐릭터별 음성 스타일 매핑
    character_voices = {}
    for char in script.get("characters", []):
        voice_style = char.get("voice_style", "narrator")
        # 간단한 매핑
        if "female" in voice_style.lower() or "girl" in voice_style.lower():
            character_voices[char["name"]] = "young_female"
        elif "male" in voice_style.lower() or "deep" in voice_style.lower():
            character_voices[char["name"]] = "deep_male"
        else:
            character_voices[char["name"]] = "narrator"
    
    print(f"\n📌 캐릭터 음성 매핑: {character_voices}")
    
    # 장면별 오디오 처리
    print("\n📌 Phase 1: 대사/나레이션 음성 생성")
    for scene in script.get("scenes", []):
        scene_num = scene["scene_number"]
        
        # 나레이션
        if scene.get("narration"):
            clip = tts_gen.generate_speech(
                text=scene["narration"],
                voice_style="narrator",
                scene_number=scene_num,
                clip_type="narration",
                speaking_rate=0.95
            )
            if clip:
                all_audio_clips.append(clip)
        
        # 대사
        if scene.get("dialogue"):
            clip = tts_gen.generate_speech(
                text=scene["dialogue"],
                voice_style="young_female",  # 기본값
                scene_number=scene_num,
                clip_type="dialogue"
            )
            if clip:
                all_audio_clips.append(clip)
        
        # 효과음 제안
        if scene.get("sound_effects"):
            sfx = sfx_manager.suggest_sfx(scene["sound_effects"], scene_num)
            all_sfx_suggestions.extend(sfx)
    
    print(f"   ✓ {len(all_audio_clips)}개 음성 클립 생성/준비됨")
    
    # 효과음 가이드 생성
    print("\n📌 Phase 2: 효과음 가이드 생성")
    sfx_sheet = sfx_manager.generate_sfx_sheet(script.get("scenes", []))
    sfx_path = Path(output_dir) / "audio" / "SFX_GUIDE.txt"
    with open(sfx_path, 'w', encoding='utf-8') as f:
        f.write(sfx_sheet)
    print(f"   ✓ 효과음 가이드 저장됨")
    
    # BGM 가이드 생성
    print("\n📌 Phase 3: BGM 가이드 생성")
    bgm_guide = music_advisor.generate_music_guide(script.get("scenes", []))
    bgm_path = Path(output_dir) / "audio" / "BGM_GUIDE.txt"
    with open(bgm_path, 'w', encoding='utf-8') as f:
        f.write(bgm_guide)
    print(f"   ✓ BGM 가이드 저장됨")
    
    # 오디오 매니페스트 저장
    manifest = {
        "total_clips": len(all_audio_clips),
        "clips": [
            {
                "clip_id": c.clip_id,
                "type": c.clip_type,
                "scene": c.scene_number,
                "duration": c.duration_seconds,
                "file": c.file_path,
                "text": c.text
            }
            for c in all_audio_clips
        ],
        "sfx_suggestions": all_sfx_suggestions
    }
    
    manifest_path = Path(output_dir) / "audio" / "audio_manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 60)
    print("✅ 오디오 준비 완료!")
    print("=" * 60)
    
    return manifest


if __name__ == "__main__":
    script_path = "/home/claude/anime-pipeline/scripts/sample_script.json"
    
    if Path(script_path).exists():
        result = process_script_for_audio(script_path)
        print(f"\n생성된 항목:")
        print(f"  - 오디오 클립: {result['total_clips']}개")
        print(f"  - 효과음 제안: {len(result['sfx_suggestions'])}개")
    else:
        print(f"스크립트 파일이 없습니다: {script_path}")
