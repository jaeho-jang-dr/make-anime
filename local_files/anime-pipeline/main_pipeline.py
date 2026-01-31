#!/usr/bin/env python3
"""
=============================================================================
🎬 AI 애니메이션 파이프라인 - 메인 실행기
=============================================================================
Google Antigravity + Claude CLI + Gemini + Grok + Whisk 통합 워크플로우

사용법:
    python main_pipeline.py --mode full      # 전체 파이프라인
    python main_pipeline.py --mode script    # 스크립트만 생성
    python main_pipeline.py --mode images    # 이미지 프롬프트만
    python main_pipeline.py --mode audio     # 오디오만
    python main_pipeline.py --mode render    # 렌더링만
    python main_pipeline.py --mode guide     # 가이드 출력
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# 프로젝트 경로 설정
PROJECT_DIR = Path("/home/claude/anime-pipeline")
SCRIPTS_DIR = PROJECT_DIR / "scripts"

# 모듈 임포트
sys.path.insert(0, str(SCRIPTS_DIR))

try:
    from step1_script_generator import ScriptGenerator, SAMPLE_SCRIPT
    from step2_image_generator import process_script_for_images, GeminiImageGenerator
    from step3_audio_generator import process_script_for_audio
    from step4_render_final import ProjectAssembler
except ImportError as e:
    print(f"⚠️ 모듈 임포트 오류: {e}")
    print("개별 스크립트를 직접 실행하세요.")


class AnimePipeline:
    """AI 애니메이션 제작 통합 파이프라인"""
    
    def __init__(self, project_dir: str = None):
        self.project_dir = Path(project_dir) if project_dir else PROJECT_DIR
        self.setup_directories()
        
        # 설정 로드
        self.config = self.load_config()
        
    def setup_directories(self):
        """디렉토리 구조 생성"""
        directories = [
            "scripts",
            "characters", 
            "scenes/clips",
            "scenes/backgrounds",
            "audio/voice",
            "audio/bgm",
            "audio/sfx",
            "output",
            "config"
        ]
        
        for dir_name in directories:
            (self.project_dir / dir_name).mkdir(parents=True, exist_ok=True)
    
    def load_config(self) -> dict:
        """설정 파일 로드"""
        config_path = self.project_dir / "config" / "pipeline_config.json"
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return {
            "project": {"name": "AI Anime", "target_duration_minutes": 10},
            "whisk_settings": {"monthly_limit": 100, "clip_length": 8}
        }
    
    def run_step1_script(self, 
                         genre: str = "판타지",
                         duration: int = 10,
                         theme: str = "모험과 성장",
                         use_sample: bool = True) -> str:
        """Step 1: 스크립트 생성"""
        
        print("\n" + "=" * 70)
        print("📖 STEP 1: 스토리 & 스크립트 생성")
        print("=" * 70)
        
        generator = ScriptGenerator(output_dir=str(self.project_dir / "scripts"))
        
        if use_sample:
            print("📌 샘플 스크립트 사용 (Claude CLI 없이 테스트)")
            script_path = generator.save_script(SAMPLE_SCRIPT, "anime_script.json")
        else:
            print(f"📌 Claude CLI로 새 스크립트 생성 중...")
            print(f"   장르: {genre}, 길이: {duration}분, 테마: {theme}")
            
            script = generator.generate_full_script(
                genre=genre,
                duration_minutes=duration,
                theme=theme
            )
            script_path = generator.save_script(script, "anime_script.json")
        
        print(f"\n✅ 스크립트 저장됨: {script_path}")
        return str(script_path)
    
    def run_step2_images(self, script_path: str) -> dict:
        """Step 2: 이미지 프롬프트 생성"""
        
        print("\n" + "=" * 70)
        print("🎨 STEP 2: 캐릭터 & 장면 이미지 준비")
        print("=" * 70)
        
        result = process_script_for_images(script_path, str(self.project_dir))
        
        print(f"\n✅ 이미지 프롬프트 준비 완료")
        print(f"   - 캐릭터: {len(result['character_images'])}개")
        print(f"   - Whisk 장면: {len(result['whisk_scenes'])}개")
        
        return result
    
    def run_step3_audio(self, script_path: str) -> dict:
        """Step 3: 오디오 생성"""
        
        print("\n" + "=" * 70)
        print("🎵 STEP 3: 오디오 생성")
        print("=" * 70)
        
        result = process_script_for_audio(script_path, str(self.project_dir))
        
        print(f"\n✅ 오디오 준비 완료")
        print(f"   - 음성 클립: {result['total_clips']}개")
        
        return result
    
    def run_step4_render(self, script_path: str, bgm_path: str = None) -> str:
        """Step 4: 최종 렌더링"""
        
        print("\n" + "=" * 70)
        print("🎬 STEP 4: 최종 렌더링")
        print("=" * 70)
        
        assembler = ProjectAssembler(str(self.project_dir))
        clips_dir = str(self.project_dir / "scenes" / "clips")
        
        result = assembler.full_assembly(script_path, clips_dir, bgm_path)
        
        if result:
            print(f"\n✅ 최종 영상: {result}")
        else:
            # 가이드 출력
            guide = assembler.generate_assembly_guide(script_path)
            print(guide)
        
        return result
    
    def run_full_pipeline(self,
                          genre: str = "판타지",
                          duration: int = 10,
                          theme: str = "모험과 성장",
                          use_sample: bool = True) -> dict:
        """전체 파이프라인 실행"""
        
        print("\n" + "█" * 70)
        print("█" + " " * 68 + "█")
        print("█" + "    🎬 AI 애니메이션 파이프라인 시작".center(66) + "█")
        print("█" + " " * 68 + "█")
        print("█" * 70)
        
        start_time = datetime.now()
        results = {}
        
        # Step 1: 스크립트
        script_path = self.run_step1_script(genre, duration, theme, use_sample)
        results["script_path"] = script_path
        
        # Step 2: 이미지
        image_result = self.run_step2_images(script_path)
        results["images"] = image_result
        
        # Step 3: 오디오
        audio_result = self.run_step3_audio(script_path)
        results["audio"] = audio_result
        
        # Step 4는 Whisk 작업 후 수동 실행
        print("\n" + "=" * 70)
        print("⏸️  STEP 4: 수동 작업 필요")
        print("=" * 70)
        print("""
다음 단계를 완료하세요:

1. 📷 Whisk에서 이미지 생성:
   - https://labs.google/fx/tools/whisk 접속
   - characters/ 폴더의 프롬프트로 캐릭터 생성
   - scenes/ 폴더의 프롬프트로 각 장면 생성

2. 🎥 Whisk Animate로 영상 생성:
   - 각 이미지에서 ANIMATE 클릭
   - animation_prompt 입력
   - 8초 클립 다운로드

3. 📁 클립 저장:
   - scenes/clips/ 폴더에 저장
   - 파일명: scene_001.mp4, scene_002.mp4, ...

4. 🎬 렌더링 실행:
   $ python main_pipeline.py --mode render
""")
        
        # 완료
        elapsed = datetime.now() - start_time
        print("\n" + "█" * 70)
        print(f"⏱️  준비 완료 (소요: {elapsed.seconds}초)")
        print("█" * 70)
        
        return results
    
    def print_project_status(self):
        """프로젝트 상태 출력"""
        
        print("\n" + "=" * 70)
        print("📊 프로젝트 상태")
        print("=" * 70)
        
        # 스크립트 확인
        script_path = self.project_dir / "scripts" / "anime_script.json"
        if script_path.exists():
            with open(script_path, 'r', encoding='utf-8') as f:
                script = json.load(f)
            print(f"✅ 스크립트: {script.get('title', 'N/A')}")
            print(f"   - 장면 수: {len(script.get('scenes', []))}")
            print(f"   - 캐릭터 수: {len(script.get('characters', []))}")
        else:
            print("❌ 스크립트: 없음")
        
        # 클립 확인
        clips_dir = self.project_dir / "scenes" / "clips"
        clips = list(clips_dir.glob("*.mp4")) if clips_dir.exists() else []
        print(f"\n📹 비디오 클립: {len(clips)}개")
        
        # 오디오 확인
        audio_dir = self.project_dir / "audio"
        audio_files = list(audio_dir.glob("**/*.mp3")) if audio_dir.exists() else []
        print(f"🔊 오디오 파일: {len(audio_files)}개")
        
        # 출력 확인
        output_dir = self.project_dir / "output"
        outputs = list(output_dir.glob("*.mp4")) if output_dir.exists() else []
        print(f"🎬 최종 출력: {len(outputs)}개")
        
        print("\n" + "=" * 70)


def main():
    """메인 함수"""
    
    parser = argparse.ArgumentParser(
        description="🎬 AI 애니메이션 파이프라인",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python main_pipeline.py --mode full           # 전체 파이프라인 (준비 단계까지)
  python main_pipeline.py --mode script         # 스크립트만 생성
  python main_pipeline.py --mode render         # 렌더링 (클립 준비 후)
  python main_pipeline.py --mode status         # 상태 확인
  
  # 커스텀 스크립트 생성 (Claude CLI 필요)
  python main_pipeline.py --mode script --genre SF --duration 5 --no-sample
        """
    )
    
    parser.add_argument("--mode", 
                        choices=["full", "script", "images", "audio", "render", "status", "guide"],
                        default="status",
                        help="실행 모드")
    parser.add_argument("--genre", default="판타지", help="장르")
    parser.add_argument("--duration", type=int, default=10, help="길이(분)")
    parser.add_argument("--theme", default="모험과 성장", help="테마")
    parser.add_argument("--no-sample", action="store_true", help="샘플 대신 새로 생성")
    parser.add_argument("--bgm", default=None, help="BGM 파일 경로")
    
    args = parser.parse_args()
    
    pipeline = AnimePipeline()
    script_path = str(pipeline.project_dir / "scripts" / "anime_script.json")
    
    if args.mode == "status":
        pipeline.print_project_status()
    
    elif args.mode == "full":
        pipeline.run_full_pipeline(
            genre=args.genre,
            duration=args.duration,
            theme=args.theme,
            use_sample=not args.no_sample
        )
    
    elif args.mode == "script":
        pipeline.run_step1_script(
            genre=args.genre,
            duration=args.duration,
            theme=args.theme,
            use_sample=not args.no_sample
        )
    
    elif args.mode == "images":
        if Path(script_path).exists():
            pipeline.run_step2_images(script_path)
        else:
            print("❌ 먼저 스크립트를 생성하세요: --mode script")
    
    elif args.mode == "audio":
        if Path(script_path).exists():
            pipeline.run_step3_audio(script_path)
        else:
            print("❌ 먼저 스크립트를 생성하세요: --mode script")
    
    elif args.mode == "render":
        if Path(script_path).exists():
            pipeline.run_step4_render(script_path, args.bgm)
        else:
            print("❌ 먼저 스크립트를 생성하세요: --mode script")
    
    elif args.mode == "guide":
        assembler = ProjectAssembler()
        if Path(script_path).exists():
            guide = assembler.generate_assembly_guide(script_path)
            print(guide)
        else:
            print("❌ 먼저 스크립트를 생성하세요: --mode script")


if __name__ == "__main__":
    main()
