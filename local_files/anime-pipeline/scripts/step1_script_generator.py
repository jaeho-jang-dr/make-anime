#!/usr/bin/env python3
"""
=============================================================================
STEP 1: 스토리 & 스크립트 생성기 (Claude CLI 활용)
=============================================================================
이 모듈은 Claude CLI를 사용하여 애니메이션 스크립트를 생성합니다.
- 전체 스토리 아크 생성
- 장면별 분할 (8초 단위)
- 각 장면에 대한 이미지 프롬프트 생성
- 대사 및 나레이션 스크립트 생성
"""

import json
import subprocess
import os
from dataclasses import dataclass, asdict
from typing import List, Optional
from pathlib import Path

@dataclass
class Scene:
    """개별 장면 데이터 구조"""
    scene_number: int
    duration_seconds: int
    description: str
    visual_prompt: str           # Whisk용 이미지 프롬프트
    character_action: str        # 캐릭터 동작 설명
    animation_prompt: str        # Whisk Animate용 모션 프롬프트
    dialogue: Optional[str]      # 대사 (없으면 None)
    narration: Optional[str]     # 나레이션 (없으면 None)
    sound_effects: List[str]     # 필요한 효과음
    mood: str                    # 장면 분위기
    camera_movement: str         # 카메라 움직임 (pan, zoom, static 등)

@dataclass
class Character:
    """캐릭터 정보"""
    name: str
    description: str
    visual_traits: str           # 시각적 특징 (Whisk Subject용)
    personality: str
    voice_style: str             # TTS 스타일 가이드

@dataclass
class AnimeScript:
    """전체 애니메이션 스크립트"""
    title: str
    genre: str
    total_duration_minutes: int
    synopsis: str
    characters: List[Character]
    scenes: List[Scene]
    style_reference: str         # 애니메이션 스타일 (지브리, 신카이 등)
    color_palette: str           # 색상 팔레트


class ScriptGenerator:
    """Claude CLI를 사용한 스크립트 생성기"""
    
    def __init__(self, output_dir: str = "scripts"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def call_claude(self, prompt: str) -> str:
        """Claude CLI 호출"""
        try:
            # Claude CLI 명령어 (Antigravity 환경)
            result = subprocess.run(
                ["claude", "-p", prompt],
                capture_output=True,
                text=True,
                timeout=120
            )
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                print(f"Claude CLI 오류: {result.stderr}")
                return ""
        except FileNotFoundError:
            # CLI 없으면 API 모드로 폴백
            return self._call_claude_api(prompt)
        except Exception as e:
            print(f"오류 발생: {e}")
            return ""
    
    def _call_claude_api(self, prompt: str) -> str:
        """Claude API 직접 호출 (폴백)"""
        # Anthropic API 사용 시
        try:
            import anthropic
            client = anthropic.Anthropic()
            message = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except:
            return "Claude API 호출 실패 - API 키를 확인하세요"
    
    def generate_story_concept(self, 
                                genre: str = "판타지",
                                duration_minutes: int = 10,
                                theme: str = "모험과 성장") -> dict:
        """스토리 컨셉 생성"""
        
        prompt = f"""당신은 일본 애니메이션 시나리오 작가입니다.
다음 조건으로 {duration_minutes}분 분량의 단편 애니메이션 스토리 컨셉을 만들어주세요.

장르: {genre}
테마: {theme}
길이: {duration_minutes}분 (약 {duration_minutes * 60 // 8}개의 8초 장면)

다음 JSON 형식으로만 응답해주세요:
{{
    "title": "제목",
    "title_korean": "한국어 제목",
    "synopsis": "200자 이내 줄거리",
    "style_reference": "애니메이션 스타일 (예: 신카이 마코토, 지브리, 유아사 마사아키)",
    "color_palette": "주요 색상 팔레트 설명",
    "mood": "전체적인 분위기",
    "main_conflict": "주요 갈등",
    "resolution": "결말"
}}"""
        
        response = self.call_claude(prompt)
        try:
            # JSON 파싱 시도
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                return json.loads(response[json_start:json_end])
        except json.JSONDecodeError:
            pass
        return {"raw_response": response}
    
    def generate_characters(self, story_concept: dict, num_characters: int = 3) -> List[Character]:
        """캐릭터 생성"""
        
        prompt = f"""스토리 컨셉을 기반으로 {num_characters}명의 캐릭터를 만들어주세요.

스토리: {json.dumps(story_concept, ensure_ascii=False)}

각 캐릭터에 대해 다음 JSON 배열 형식으로 응답해주세요:
[
    {{
        "name": "캐릭터 이름",
        "description": "캐릭터 설명 (50자)",
        "visual_traits": "시각적 특징 - AI 이미지 생성용 상세 설명 (머리색, 의상, 체형 등)",
        "personality": "성격",
        "voice_style": "목소리 특징 (TTS 설정용)"
    }}
]

visual_traits는 Whisk AI에서 Subject 이미지 생성에 사용됩니다.
영어와 한국어를 혼용해도 됩니다."""
        
        response = self.call_claude(prompt)
        characters = []
        
        try:
            json_start = response.find('[')
            json_end = response.rfind(']') + 1
            if json_start != -1 and json_end > json_start:
                char_data = json.loads(response[json_start:json_end])
                for c in char_data:
                    characters.append(Character(
                        name=c.get("name", "Unknown"),
                        description=c.get("description", ""),
                        visual_traits=c.get("visual_traits", ""),
                        personality=c.get("personality", ""),
                        voice_style=c.get("voice_style", "neutral")
                    ))
        except json.JSONDecodeError:
            print("캐릭터 JSON 파싱 실패")
        
        return characters
    
    def generate_scene_breakdown(self, 
                                  story_concept: dict,
                                  characters: List[Character],
                                  target_scenes: int = 75) -> List[Scene]:
        """장면 분할 생성 (8초 단위)"""
        
        char_info = [asdict(c) for c in characters]
        
        prompt = f"""스토리와 캐릭터를 기반으로 {target_scenes}개의 장면으로 분할해주세요.
각 장면은 8초 분량입니다.

스토리: {json.dumps(story_concept, ensure_ascii=False)}
캐릭터: {json.dumps(char_info, ensure_ascii=False)}

처음 10개 장면만 다음 JSON 배열 형식으로 응답해주세요:
[
    {{
        "scene_number": 1,
        "duration_seconds": 8,
        "description": "장면 설명 (한국어)",
        "visual_prompt": "Whisk용 영어 이미지 프롬프트 - 배경과 구도 중심",
        "character_action": "캐릭터의 동작",
        "animation_prompt": "Whisk Animate용 모션 프롬프트 (영어, 예: 'walking slowly, wind blowing hair')",
        "dialogue": "대사 (없으면 null)",
        "narration": "나레이션 (없으면 null)", 
        "sound_effects": ["효과음1", "효과음2"],
        "mood": "분위기",
        "camera_movement": "pan left / zoom in / static 등"
    }}
]

visual_prompt는 Whisk의 Scene 입력으로 사용됩니다.
animation_prompt는 Whisk Animate의 모션 지시로 사용됩니다."""
        
        response = self.call_claude(prompt)
        scenes = []
        
        try:
            json_start = response.find('[')
            json_end = response.rfind(']') + 1
            if json_start != -1 and json_end > json_start:
                scene_data = json.loads(response[json_start:json_end])
                for s in scene_data:
                    scenes.append(Scene(
                        scene_number=s.get("scene_number", len(scenes) + 1),
                        duration_seconds=s.get("duration_seconds", 8),
                        description=s.get("description", ""),
                        visual_prompt=s.get("visual_prompt", ""),
                        character_action=s.get("character_action", ""),
                        animation_prompt=s.get("animation_prompt", ""),
                        dialogue=s.get("dialogue"),
                        narration=s.get("narration"),
                        sound_effects=s.get("sound_effects", []),
                        mood=s.get("mood", ""),
                        camera_movement=s.get("camera_movement", "static")
                    ))
        except json.JSONDecodeError:
            print("장면 JSON 파싱 실패")
        
        return scenes
    
    def generate_full_script(self,
                             genre: str = "판타지",
                             duration_minutes: int = 10,
                             theme: str = "모험과 성장") -> AnimeScript:
        """전체 스크립트 생성 파이프라인"""
        
        print("=" * 60)
        print("🎬 AI 애니메이션 스크립트 생성 시작")
        print("=" * 60)
        
        # 1. 스토리 컨셉
        print("\n📖 Step 1: 스토리 컨셉 생성 중...")
        story_concept = self.generate_story_concept(genre, duration_minutes, theme)
        print(f"   제목: {story_concept.get('title', 'N/A')}")
        
        # 2. 캐릭터
        print("\n👤 Step 2: 캐릭터 생성 중...")
        characters = self.generate_characters(story_concept)
        print(f"   {len(characters)}명의 캐릭터 생성됨")
        
        # 3. 장면 분할
        target_scenes = (duration_minutes * 60) // 8
        print(f"\n🎬 Step 3: {target_scenes}개 장면 분할 중...")
        scenes = self.generate_scene_breakdown(story_concept, characters, target_scenes)
        print(f"   {len(scenes)}개 장면 생성됨 (샘플)")
        
        # 스크립트 객체 생성
        script = AnimeScript(
            title=story_concept.get("title", "Untitled"),
            genre=genre,
            total_duration_minutes=duration_minutes,
            synopsis=story_concept.get("synopsis", ""),
            characters=characters,
            scenes=scenes,
            style_reference=story_concept.get("style_reference", ""),
            color_palette=story_concept.get("color_palette", "")
        )
        
        return script
    
    def save_script(self, script: AnimeScript, filename: str = "anime_script.json"):
        """스크립트 저장"""
        output_path = self.output_dir / filename
        
        # dataclass를 dict로 변환
        script_dict = {
            "title": script.title,
            "genre": script.genre,
            "total_duration_minutes": script.total_duration_minutes,
            "synopsis": script.synopsis,
            "style_reference": script.style_reference,
            "color_palette": script.color_palette,
            "characters": [asdict(c) for c in script.characters],
            "scenes": [asdict(s) for s in script.scenes]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(script_dict, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 스크립트 저장됨: {output_path}")
        return output_path


# 샘플 스크립트 (Claude 없이 테스트용)
SAMPLE_SCRIPT = AnimeScript(
    title="The Last Starkeeper",
    genre="판타지",
    total_duration_minutes=10,
    synopsis="어둠이 세상을 덮은 후, 마지막 별지기 소녀 루나가 잃어버린 별들을 찾아 떠나는 여정",
    characters=[
        Character(
            name="루나 (Luna)",
            description="16세 소녀, 마지막 별지기",
            visual_traits="young girl, 16 years old, long silver hair, bright blue eyes, wearing a dark blue cloak with star patterns, holding a glowing lantern, determined expression",
            personality="용감하고 순수함, 약간 고집스러움",
            voice_style="young female, gentle but determined"
        ),
        Character(
            name="노바 (Nova)",
            description="루나의 동반자, 작은 별 정령",
            visual_traits="tiny glowing spirit, star-shaped, golden light, cute round eyes, floating, leaving sparkle trail",
            personality="장난기 많고 충성스러움",
            voice_style="high pitched, playful"
        ),
        Character(
            name="그림자 왕 (Shadow King)",
            description="별빛을 삼킨 어둠의 존재",
            visual_traits="tall dark figure, flowing shadow cloak, glowing red eyes, crown of darkness, intimidating presence",
            personality="위엄있고 냉혹함",
            voice_style="deep male, menacing"
        )
    ],
    scenes=[
        Scene(
            scene_number=1,
            duration_seconds=8,
            description="어둠에 잠긴 마을의 전경. 하늘에 별이 하나도 없다.",
            visual_prompt="dark fantasy village at night, no stars in sky, dim lantern lights, abandoned streets, gothic architecture, misty atmosphere",
            character_action="없음 - 배경 설정 장면",
            animation_prompt="slow pan across village, mist slowly moving, flickering lantern lights",
            dialogue=None,
            narration="옛날, 밤하늘에는 수천 개의 별이 빛났습니다...",
            sound_effects=["wind howling", "distant bell"],
            mood="우울하고 신비로움",
            camera_movement="slow pan right"
        ),
        Scene(
            scene_number=2,
            duration_seconds=8,
            description="루나가 창가에서 텅 빈 하늘을 바라본다.",
            visual_prompt="anime girl silhouette by window, looking at dark empty sky, moonlit room, curtains blowing, melancholic atmosphere",
            character_action="루나가 창밖을 응시하며 한숨을 쉰다",
            animation_prompt="girl sighing, curtains gently blowing, subtle body movement",
            dialogue="별들아... 어디로 간 거니?",
            narration=None,
            sound_effects=["soft wind", "fabric rustling"],
            mood="그리움과 결심",
            camera_movement="slow zoom in"
        ),
        Scene(
            scene_number=3,
            duration_seconds=8,
            description="노바가 루나 앞에 나타나 빛을 발한다.",
            visual_prompt="glowing star spirit appearing before girl in dark room, magical sparkles, warm golden light illuminating face, surprised expression",
            character_action="노바가 나타나고, 루나가 놀라서 뒤로 물러난다",
            animation_prompt="spirit materializing with sparkles, girl stepping back in surprise, light spreading",
            dialogue="루나! 드디어 찾았어! 별들을 구할 수 있어!",
            narration=None,
            sound_effects=["magical chime", "sparkle sounds"],
            mood="희망과 놀라움",
            camera_movement="static with light effects"
        )
    ],
    style_reference="신카이 마코토 스타일 - 선명한 색감과 빛의 표현",
    color_palette="딥 블루, 골드, 실버, 보라색 그라데이션"
)


if __name__ == "__main__":
    # 테스트 실행
    generator = ScriptGenerator(output_dir="/home/claude/anime-pipeline/scripts")
    
    # 샘플 스크립트 저장 (Claude CLI 없이 테스트)
    generator.save_script(SAMPLE_SCRIPT, "sample_script.json")
    
    print("\n" + "=" * 60)
    print("📋 샘플 스크립트 정보")
    print("=" * 60)
    print(f"제목: {SAMPLE_SCRIPT.title}")
    print(f"장르: {SAMPLE_SCRIPT.genre}")
    print(f"길이: {SAMPLE_SCRIPT.total_duration_minutes}분")
    print(f"캐릭터 수: {len(SAMPLE_SCRIPT.characters)}")
    print(f"장면 수: {len(SAMPLE_SCRIPT.scenes)} (샘플)")
    print(f"스타일: {SAMPLE_SCRIPT.style_reference}")
