#!/usr/bin/env python3
"""
=============================================================================
STEP 2: 캐릭터 & 장면 이미지 생성기 (Gemini 3 Pro + Imagen)
=============================================================================
이 모듈은 Google Gemini API를 사용하여:
- 캐릭터 레퍼런스 이미지 생성 (Whisk Subject용)
- 배경/장면 이미지 생성 (Whisk Scene용)
- 스타일 레퍼런스 이미지 생성 (Whisk Style용)
"""

import os
import json
import base64
import requests
from pathlib import Path
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import time


@dataclass
class GeneratedImage:
    """생성된 이미지 정보"""
    image_id: str
    image_type: str  # 'character', 'scene', 'style'
    prompt: str
    file_path: str
    metadata: Dict[str, Any]


class GeminiImageGenerator:
    """Gemini API를 사용한 이미지 생성기"""
    
    def __init__(self, 
                 api_key: Optional[str] = None,
                 output_dir: str = "characters"):
        
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Gemini API 엔드포인트
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        
        # 이미지 생성 모델
        self.image_model = "gemini-2.0-flash-exp"  # 이미지 생성 지원 모델
        
    def _make_request(self, endpoint: str, payload: dict) -> dict:
        """API 요청 헬퍼"""
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        
        if self.api_key:
            url += f"?key={self.api_key}"
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=120)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API 요청 오류: {e}")
            return {}
    
    def generate_with_gemini(self, prompt: str, image_type: str = "character") -> Optional[str]:
        """
        Gemini API로 이미지 생성
        Antigravity 환경에서는 직접 Gemini 호출 가능
        """
        
        # 이미지 생성을 위한 시스템 프롬프트
        system_prompt = f"""You are an anime character designer.
Generate a detailed image description that can be used for AI image generation.
Style: Japanese anime, high quality, detailed
Type: {image_type}

Respond with ONLY the enhanced prompt in English, optimized for image generation.
Include specific details about:
- Art style (anime, specific influences)
- Lighting and atmosphere
- Color palette
- Composition
- Quality descriptors (masterpiece, highly detailed, etc.)"""

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{system_prompt}\n\nOriginal prompt: {prompt}"}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 500
            }
        }
        
        endpoint = f"models/gemini-2.0-flash-exp:generateContent"
        result = self._make_request(endpoint, payload)
        
        if result and "candidates" in result:
            try:
                return result["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError):
                pass
        
        return prompt  # 실패시 원본 반환
    
    def generate_character_image(self, 
                                  character_name: str,
                                  visual_traits: str,
                                  style: str = "anime") -> GeneratedImage:
        """캐릭터 이미지 생성 (Whisk Subject용)"""
        
        print(f"\n🎨 캐릭터 이미지 생성: {character_name}")
        
        # 프롬프트 강화
        enhanced_prompt = f"""masterpiece, best quality, anime style character portrait,
{visual_traits},
{style} art style,
clean lineart, vibrant colors, detailed face and eyes,
white background for easy extraction,
full body or upper body shot,
professional anime character design sheet"""
        
        # Gemini로 프롬프트 최적화
        optimized_prompt = self.generate_with_gemini(enhanced_prompt, "character")
        
        # 이미지 ID 생성
        image_id = f"char_{character_name.lower().replace(' ', '_')}_{int(time.time())}"
        
        # 메타데이터 저장 (실제 이미지는 Whisk에서 생성)
        metadata = {
            "character_name": character_name,
            "original_traits": visual_traits,
            "optimized_prompt": optimized_prompt,
            "style": style,
            "usage": "whisk_subject",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # 프롬프트 파일 저장
        prompt_file = self.output_dir / f"{image_id}_prompt.json"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        return GeneratedImage(
            image_id=image_id,
            image_type="character",
            prompt=optimized_prompt,
            file_path=str(prompt_file),
            metadata=metadata
        )
    
    def generate_scene_image(self,
                              scene_number: int,
                              visual_prompt: str,
                              mood: str = "",
                              style_reference: str = "") -> GeneratedImage:
        """장면 배경 이미지 생성 (Whisk Scene용)"""
        
        print(f"\n🏞️ 장면 {scene_number} 배경 생성 중...")
        
        enhanced_prompt = f"""masterpiece, best quality, anime background art,
{visual_prompt},
{mood} atmosphere,
{style_reference} style influence,
detailed environment, beautiful lighting,
cinematic composition, no characters,
wide shot establishing scene"""
        
        optimized_prompt = self.generate_with_gemini(enhanced_prompt, "scene")
        
        image_id = f"scene_{scene_number:03d}_{int(time.time())}"
        
        metadata = {
            "scene_number": scene_number,
            "original_prompt": visual_prompt,
            "optimized_prompt": optimized_prompt,
            "mood": mood,
            "style_reference": style_reference,
            "usage": "whisk_scene",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        prompt_file = self.output_dir / f"{image_id}_prompt.json"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        return GeneratedImage(
            image_id=image_id,
            image_type="scene",
            prompt=optimized_prompt,
            file_path=str(prompt_file),
            metadata=metadata
        )
    
    def generate_style_reference(self,
                                  style_name: str,
                                  style_description: str) -> GeneratedImage:
        """스타일 레퍼런스 이미지 생성 (Whisk Style용)"""
        
        print(f"\n🎨 스타일 레퍼런스 생성: {style_name}")
        
        enhanced_prompt = f"""anime art style reference,
{style_description},
example of artistic style,
color palette showcase,
lighting and shading demonstration,
{style_name} aesthetic"""
        
        optimized_prompt = self.generate_with_gemini(enhanced_prompt, "style")
        
        image_id = f"style_{style_name.lower().replace(' ', '_')}_{int(time.time())}"
        
        metadata = {
            "style_name": style_name,
            "description": style_description,
            "optimized_prompt": optimized_prompt,
            "usage": "whisk_style",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        prompt_file = self.output_dir / f"{image_id}_prompt.json"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        return GeneratedImage(
            image_id=image_id,
            image_type="style",
            prompt=optimized_prompt,
            file_path=str(prompt_file),
            metadata=metadata
        )


class WhiskIntegration:
    """
    Google Whisk 통합 클래스
    Whisk는 브라우저 기반이므로, 이 클래스는:
    1. Whisk에 입력할 프롬프트/이미지 준비
    2. Whisk 사용 가이드 생성
    3. 결과물 관리
    """
    
    def __init__(self, output_dir: str = "scenes"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.whisk_url = "https://labs.google/fx/tools/whisk"
    
    def prepare_whisk_inputs(self, 
                              subject_prompt: str,
                              scene_prompt: str,
                              style_prompt: str,
                              animation_prompt: str,
                              scene_number: int) -> dict:
        """Whisk에 입력할 데이터 준비"""
        
        whisk_data = {
            "scene_number": scene_number,
            "whisk_url": self.whisk_url,
            "inputs": {
                "subject": {
                    "description": "캐릭터 이미지를 드래그하거나 Gemini로 생성",
                    "prompt": subject_prompt
                },
                "scene": {
                    "description": "배경 이미지",
                    "prompt": scene_prompt
                },
                "style": {
                    "description": "스타일 레퍼런스",
                    "prompt": style_prompt
                }
            },
            "animate": {
                "enabled": True,
                "prompt": animation_prompt,
                "duration": "8 seconds",
                "note": "ANIMATE 버튼 클릭 후 모션 프롬프트 입력"
            },
            "instructions": [
                f"1. {self.whisk_url} 접속",
                "2. Subject에 캐릭터 이미지 업로드",
                "3. Scene에 배경 이미지 업로드", 
                "4. Style에 스타일 레퍼런스 업로드",
                "5. Create 클릭하여 이미지 생성",
                "6. 결과물에서 ANIMATE 클릭",
                f"7. 애니메이션 프롬프트 입력: {animation_prompt}",
                "8. 8초 영상 다운로드"
            ]
        }
        
        # 저장
        output_file = self.output_dir / f"whisk_scene_{scene_number:03d}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(whisk_data, f, ensure_ascii=False, indent=2)
        
        return whisk_data
    
    def generate_batch_instructions(self, scenes: List[dict]) -> str:
        """배치 작업 가이드 생성"""
        
        instructions = """
╔══════════════════════════════════════════════════════════════╗
║           🎬 WHISK 배치 작업 가이드                           ║
╚══════════════════════════════════════════════════════════════╝

📌 사전 준비:
1. Google One AI Premium 구독 확인 (월 100개 영상 생성 가능)
2. https://labs.google/fx/tools/whisk 접속
3. 캐릭터 이미지들을 미리 생성/다운로드

📌 작업 순서:
"""
        for i, scene in enumerate(scenes, 1):
            instructions += f"""
─────────────────────────────────────────────────
장면 {scene.get('scene_number', i):03d}
─────────────────────────────────────────────────
• Scene 프롬프트: {scene.get('visual_prompt', 'N/A')[:50]}...
• Animation: {scene.get('animation_prompt', 'N/A')}
• 예상 소요: 2-3분
"""
        
        instructions += f"""
─────────────────────────────────────────────────
📊 총계:
• 총 장면 수: {len(scenes)}개
• 예상 총 소요 시간: {len(scenes) * 3}분 ~ {len(scenes) * 5}분
• 월간 크레딧 사용: {len(scenes)}/100
─────────────────────────────────────────────────

💡 팁:
- 캐릭터 Subject 이미지는 동일한 것을 계속 사용하여 일관성 유지
- Style 이미지도 고정하여 전체 영상 톤 통일
- 실패한 장면은 건너뛰고 나중에 재시도

🔗 Whisk URL: https://labs.google/fx/tools/whisk
"""
        return instructions


# Grok API 통합 (창의적 프롬프트 생성)
class GrokCreativeAssistant:
    """Grok API를 사용한 창의적 보조"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GROK_API_KEY") or os.getenv("XAI_API_KEY")
        self.base_url = "https://api.x.ai/v1"
    
    def enhance_visual_prompt(self, basic_prompt: str, mood: str) -> str:
        """Grok으로 시각적 프롬프트 강화"""
        
        if not self.api_key:
            return basic_prompt
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": "grok-beta",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a creative visual artist. Enhance the given prompt for anime image generation with vivid, artistic details. Keep it concise but evocative."
                },
                {
                    "role": "user",
                    "content": f"Enhance this anime scene prompt with mood '{mood}': {basic_prompt}"
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
                return result["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Grok API 오류: {e}")
        
        return basic_prompt


def process_script_for_images(script_path: str, output_dir: str = "/home/claude/anime-pipeline"):
    """스크립트를 읽고 모든 이미지 프롬프트 생성"""
    
    with open(script_path, 'r', encoding='utf-8') as f:
        script = json.load(f)
    
    # 생성기 초기화
    gemini_gen = GeminiImageGenerator(output_dir=f"{output_dir}/characters")
    whisk_int = WhiskIntegration(output_dir=f"{output_dir}/scenes")
    grok_assist = GrokCreativeAssistant()
    
    print("=" * 60)
    print("🎨 이미지 생성 파이프라인 시작")
    print("=" * 60)
    
    # 1. 캐릭터 이미지 생성
    print("\n📌 Phase 1: 캐릭터 레퍼런스 생성")
    character_images = []
    for char in script.get("characters", []):
        img = gemini_gen.generate_character_image(
            character_name=char["name"],
            visual_traits=char["visual_traits"],
            style=script.get("style_reference", "anime")
        )
        character_images.append(img)
        print(f"   ✓ {char['name']} 프롬프트 생성됨")
    
    # 2. 스타일 레퍼런스 생성
    print("\n📌 Phase 2: 스타일 레퍼런스 생성")
    style_img = gemini_gen.generate_style_reference(
        style_name=script.get("style_reference", "anime"),
        style_description=script.get("color_palette", "vibrant anime colors")
    )
    print(f"   ✓ 스타일 레퍼런스 생성됨")
    
    # 3. 장면별 Whisk 입력 준비
    print("\n📌 Phase 3: 장면별 Whisk 입력 준비")
    whisk_scenes = []
    for scene in script.get("scenes", []):
        # Grok으로 프롬프트 강화 (선택적)
        enhanced_visual = grok_assist.enhance_visual_prompt(
            scene["visual_prompt"],
            scene.get("mood", "")
        )
        
        whisk_data = whisk_int.prepare_whisk_inputs(
            subject_prompt=character_images[0].prompt if character_images else "",
            scene_prompt=enhanced_visual,
            style_prompt=style_img.prompt,
            animation_prompt=scene.get("animation_prompt", "subtle movement"),
            scene_number=scene["scene_number"]
        )
        whisk_scenes.append(whisk_data)
        print(f"   ✓ 장면 {scene['scene_number']} 준비됨")
    
    # 4. 배치 가이드 생성
    print("\n📌 Phase 4: 작업 가이드 생성")
    guide = whisk_int.generate_batch_instructions(script.get("scenes", []))
    guide_path = Path(output_dir) / "WHISK_WORKFLOW_GUIDE.txt"
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide)
    print(f"   ✓ 가이드 저장됨: {guide_path}")
    
    print("\n" + "=" * 60)
    print("✅ 이미지 생성 준비 완료!")
    print("=" * 60)
    
    return {
        "character_images": character_images,
        "style_image": style_img,
        "whisk_scenes": whisk_scenes,
        "guide_path": str(guide_path)
    }


if __name__ == "__main__":
    # 테스트 실행
    script_path = "/home/claude/anime-pipeline/scripts/sample_script.json"
    
    if Path(script_path).exists():
        result = process_script_for_images(script_path)
        print(f"\n생성된 항목:")
        print(f"  - 캐릭터 프롬프트: {len(result['character_images'])}개")
        print(f"  - Whisk 장면: {len(result['whisk_scenes'])}개")
        print(f"  - 가이드: {result['guide_path']}")
    else:
        print(f"스크립트 파일이 없습니다: {script_path}")
        print("먼저 step1_script_generator.py를 실행하세요.")
