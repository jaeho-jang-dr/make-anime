#!/usr/bin/env python3
"""
=============================================================================
STEP 4: 렌더링 & 최종 편집 (FFmpeg 기반)
=============================================================================
이 모듈은:
- Whisk에서 생성된 영상 클립들을 결합
- 오디오 트랙 믹싱 (대사, 나레이션, SFX, BGM)
- 자막 추가
- 최종 MP4 렌더링
"""

import os
import json
import subprocess
from pathlib import Path
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import time


@dataclass
class VideoClip:
    """비디오 클립 정보"""
    clip_id: str
    scene_number: int
    file_path: str
    duration_seconds: float
    has_audio: bool
    metadata: Dict[str, Any]


class FFmpegRenderer:
    """FFmpeg 기반 비디오 렌더러"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.output_settings = {
            "video_codec": "libx264",
            "audio_codec": "aac",
            "video_bitrate": "4000k",
            "audio_bitrate": "192k",
            "fps": 24,
            "resolution": "1280x720",
            "preset": "medium",
            "crf": 23
        }
    
    def check_ffmpeg(self) -> bool:
        """FFmpeg 설치 확인"""
        try:
            result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def create_concat_file(self, video_clips: List[VideoClip], output_path: str) -> str:
        """FFmpeg concat용 파일 리스트 생성"""
        concat_file = Path(output_path).parent / "concat_list.txt"
        
        with open(concat_file, 'w') as f:
            for clip in sorted(video_clips, key=lambda x: x.scene_number):
                if Path(clip.file_path).exists():
                    f.write(f"file '{clip.file_path}'\n")
        
        return str(concat_file)
    
    def concat_videos(self, video_clips: List[VideoClip], output_filename: str = "combined.mp4") -> Optional[str]:
        """비디오 클립들을 연결"""
        
        if not self.check_ffmpeg():
            print("⚠️ FFmpeg가 설치되지 않았습니다.")
            return None
        
        output_path = self.output_dir / output_filename
        concat_file = self.create_concat_file(video_clips, str(output_path))
        
        cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_file,
            "-c:v", self.output_settings["video_codec"],
            "-crf", str(self.output_settings["crf"]),
            "-preset", self.output_settings["preset"],
            "-c:a", "copy",
            str(output_path)
        ]
        
        print(f"🎬 비디오 연결 중...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"   ✓ 완료: {output_path}")
                return str(output_path)
            else:
                print(f"   ✗ 오류: {result.stderr}")
                return None
        except Exception as e:
            print(f"   ✗ 예외: {e}")
            return None
    
    def add_audio_track(self, video_path: str, audio_path: str, 
                        output_filename: str, audio_volume: float = 1.0) -> Optional[str]:
        """비디오에 오디오 트랙 추가"""
        
        output_path = self.output_dir / output_filename
        
        # 비디오에 오디오가 있는지 확인
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-filter_complex",
            f"[1:a]volume={audio_volume}[a1];[0:a][a1]amix=inputs=2:duration=first[aout]",
            "-map", "0:v",
            "-map", "[aout]",
            "-c:v", "copy",
            "-c:a", self.output_settings["audio_codec"],
            "-b:a", self.output_settings["audio_bitrate"],
            str(output_path)
        ]
        
        print(f"🔊 오디오 추가 중...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"   ✓ 완료: {output_path}")
                return str(output_path)
            else:
                # 오디오 트랙이 없는 비디오인 경우
                cmd_simple = [
                    "ffmpeg", "-y",
                    "-i", video_path,
                    "-i", audio_path,
                    "-map", "0:v",
                    "-map", "1:a",
                    "-c:v", "copy",
                    "-c:a", self.output_settings["audio_codec"],
                    "-shortest",
                    str(output_path)
                ]
                result2 = subprocess.run(cmd_simple, capture_output=True, text=True)
                if result2.returncode == 0:
                    print(f"   ✓ 완료: {output_path}")
                    return str(output_path)
                print(f"   ✗ 오류: {result2.stderr}")
                return None
        except Exception as e:
            print(f"   ✗ 예외: {e}")
            return None
    
    def add_subtitles(self, video_path: str, subtitle_path: str,
                      output_filename: str, style: str = "anime") -> Optional[str]:
        """비디오에 자막 추가 (burn-in)"""
        
        output_path = self.output_dir / output_filename
        
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-vf", f"subtitles={subtitle_path}",
            "-c:v", self.output_settings["video_codec"],
            "-crf", str(self.output_settings["crf"]),
            "-c:a", "copy",
            str(output_path)
        ]
        
        print(f"📝 자막 추가 중...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"   ✓ 완료: {output_path}")
                return str(output_path)
            else:
                print(f"   ✗ 오류: {result.stderr}")
                return None
        except Exception as e:
            print(f"   ✗ 예외: {e}")
            return None
    
    def create_final_render(self, video_path: str, title: str = "AI Anime") -> Optional[str]:
        """최종 렌더링 (품질 최적화)"""
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        safe_title = title.replace(" ", "_").replace("/", "-")
        output_filename = f"{safe_title}_{timestamp}.mp4"
        output_path = self.output_dir / output_filename
        
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-c:v", self.output_settings["video_codec"],
            "-preset", "slow",
            "-crf", "20",
            "-c:a", self.output_settings["audio_codec"],
            "-b:a", "256k",
            "-movflags", "+faststart",
            str(output_path)
        ]
        
        print(f"\n🎬 최종 렌더링 중...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                file_size = os.path.getsize(output_path) / (1024 * 1024)
                print(f"   ✓ 완료: {output_path}")
                print(f"   📦 파일 크기: {file_size:.1f} MB")
                return str(output_path)
            else:
                print(f"   ✗ 오류: {result.stderr}")
                return None
        except Exception as e:
            print(f"   ✗ 예외: {e}")
            return None


class SubtitleGenerator:
    """자막 파일 생성기"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def create_srt(self, scenes: List[dict], clip_duration: float = 8.0) -> str:
        """SRT 자막 파일 생성"""
        
        srt_content = ""
        subtitle_index = 1
        current_time = 0.0
        
        for scene in scenes:
            dialogue = scene.get("dialogue")
            narration = scene.get("narration")
            text = dialogue or narration
            
            if text:
                start_time = self._format_time(current_time + 0.5)
                end_time = self._format_time(current_time + clip_duration - 0.5)
                
                srt_content += f"{subtitle_index}\n"
                srt_content += f"{start_time} --> {end_time}\n"
                srt_content += f"{text}\n\n"
                subtitle_index += 1
            
            current_time += clip_duration
        
        srt_path = self.output_dir / "subtitles.srt"
        with open(srt_path, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        
        return str(srt_path)
    
    def create_ass(self, scenes: List[dict], clip_duration: float = 8.0) -> str:
        """ASS 자막 파일 생성 (고급 스타일링)"""
        
        ass_header = """[Script Info]
Title: AI Anime Subtitles
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Noto Sans CJK KR,28,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,1,2,10,10,30,1
Style: Dialogue,Noto Sans CJK KR,26,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,1,2,10,10,30,1
Style: Narration,Noto Sans CJK KR,24,&H00E0E0E0,&H000000FF,&H00000000,&H80000000,0,1,0,0,100,100,0,0,1,2,1,2,10,10,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        
        ass_content = ass_header
        current_time = 0.0
        
        for scene in scenes:
            dialogue = scene.get("dialogue")
            narration = scene.get("narration")
            
            if dialogue:
                start = self._format_time_ass(current_time + 0.3)
                end = self._format_time_ass(current_time + clip_duration - 0.3)
                ass_content += f"Dialogue: 0,{start},{end},Dialogue,,0,0,0,,{dialogue}\n"
            elif narration:
                start = self._format_time_ass(current_time + 0.3)
                end = self._format_time_ass(current_time + clip_duration - 0.3)
                ass_content += f"Dialogue: 0,{start},{end},Narration,,0,0,0,,{narration}\n"
            
            current_time += clip_duration
        
        ass_path = self.output_dir / "subtitles.ass"
        with open(ass_path, 'w', encoding='utf-8') as f:
            f.write(ass_content)
        
        return str(ass_path)
    
    def _format_time(self, seconds: float) -> str:
        """SRT 시간 형식"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
    
    def _format_time_ass(self, seconds: float) -> str:
        """ASS 시간 형식"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours:01d}:{minutes:02d}:{secs:05.2f}"


class ProjectAssembler:
    """프로젝트 최종 어셈블리"""
    
    def __init__(self, project_dir: str = "/home/claude/anime-pipeline"):
        self.project_dir = Path(project_dir)
        self.renderer = FFmpegRenderer(output_dir=f"{project_dir}/output")
        self.subtitle_gen = SubtitleGenerator(output_dir=f"{project_dir}/output")
    
    def scan_video_clips(self, clips_dir: str) -> List[VideoClip]:
        """생성된 비디오 클립 스캔"""
        
        clips = []
        clips_path = Path(clips_dir)
        
        if not clips_path.exists():
            print(f"⚠️ 클립 디렉토리가 없습니다: {clips_dir}")
            return clips
        
        for file in sorted(clips_path.glob("*.mp4")):
            scene_num = 0
            try:
                parts = file.stem.split("_")
                for part in parts:
                    if part.isdigit():
                        scene_num = int(part)
                        break
            except:
                pass
            
            clips.append(VideoClip(
                clip_id=file.stem,
                scene_number=scene_num,
                file_path=str(file),
                duration_seconds=8.0,
                has_audio=False,
                metadata={"source": "whisk_animate"}
            ))
        
        return clips
    
    def generate_assembly_guide(self, script_path: str) -> str:
        """어셈블리 가이드 생성"""
        
        with open(script_path, 'r', encoding='utf-8') as f:
            script = json.load(f)
        
        guide = f"""
╔══════════════════════════════════════════════════════════════╗
║           🎬 최종 어셈블리 가이드                              ║
╚══════════════════════════════════════════════════════════════╝

📌 프로젝트: {script.get('title', 'AI Anime')}
📌 총 길이: {script.get('total_duration_minutes', 10)}분
📌 장면 수: {len(script.get('scenes', []))}개

═══════════════════════════════════════════════════════════════
📂 필요한 파일들
═══════════════════════════════════════════════════════════════

1. 비디오 클립 (Whisk Animate에서 다운로드)
   └─ 위치: {self.project_dir}/scenes/clips/
   └─ 형식: scene_001.mp4, scene_002.mp4, ...
   └─ 총 필요: {len(script.get('scenes', []))}개

2. 오디오 파일
   └─ 대사/나레이션: {self.project_dir}/audio/*.mp3
   └─ BGM: {self.project_dir}/audio/bgm/
   └─ SFX: {self.project_dir}/audio/sfx/

3. 자막 파일
   └─ 자동 생성됨: {self.project_dir}/output/subtitles.ass

═══════════════════════════════════════════════════════════════
🔧 FFmpeg 명령어 (수동 실행용)
═══════════════════════════════════════════════════════════════

# 클립 연결
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy combined.mp4

# BGM 추가 (볼륨 30%)
ffmpeg -i combined.mp4 -i bgm.mp3 -filter_complex "[1:a]volume=0.3[a]" \\
       -map 0:v -map "[a]" -c:v copy -shortest output_with_bgm.mp4

# 자막 추가
ffmpeg -i output_with_bgm.mp4 -vf "subtitles=subtitles.ass" final.mp4

═══════════════════════════════════════════════════════════════
🎥 CapCut/DaVinci 수동 편집 순서
═══════════════════════════════════════════════════════════════

1. 새 프로젝트: 1280x720, 24fps
2. 클립 배치: 장면 순서대로 타임라인에
3. 오디오 트랙:
   - 트랙 1: 대사/나레이션
   - 트랙 2: BGM (볼륨 30-40%)
   - 트랙 3: SFX (볼륨 50%)
4. 자막: subtitles.srt 임포트
5. 전환: 크로스 디졸브 0.5초
6. 익스포트: MP4, H.264, 4000kbps

═══════════════════════════════════════════════════════════════
⏱️ 예상 소요 시간: 30분 ~ 1시간
═══════════════════════════════════════════════════════════════
"""
        return guide
    
    def full_assembly(self, script_path: str, clips_dir: str, 
                      bgm_path: Optional[str] = None) -> Optional[str]:
        """전체 어셈블리 파이프라인"""
        
        with open(script_path, 'r', encoding='utf-8') as f:
            script = json.load(f)
        
        print("=" * 60)
        print("🎬 최종 어셈블리 시작")
        print(f"   프로젝트: {script.get('title', 'AI Anime')}")
        print("=" * 60)
        
        # 1. 클립 스캔
        print("\n📌 Phase 1: 비디오 클립 스캔")
        video_clips = self.scan_video_clips(clips_dir)
        
        if not video_clips:
            print("   ⚠️ 비디오 클립이 없습니다!")
            print(f"   Whisk Animate에서 클립을 다운로드하여 저장하세요:")
            print(f"   {clips_dir}")
            return None
        
        print(f"   ✓ {len(video_clips)}개 클립 발견")
        
        # 2. 자막 생성
        print("\n📌 Phase 2: 자막 파일 생성")
        subtitle_path = self.subtitle_gen.create_ass(script.get("scenes", []), clip_duration=8.0)
        print(f"   ✓ 자막 저장됨: {subtitle_path}")
        
        # 3. 비디오 연결
        print("\n📌 Phase 3: 비디오 클립 연결")
        combined_video = self.renderer.concat_videos(video_clips, output_filename="combined_raw.mp4")
        
        if not combined_video:
            print("   ⚠️ 비디오 연결 실패")
            return None
        
        # 4. BGM 추가
        current_video = combined_video
        if bgm_path and Path(bgm_path).exists():
            print("\n📌 Phase 4: BGM 추가")
            video_with_bgm = self.renderer.add_audio_track(
                current_video, bgm_path, "combined_with_bgm.mp4", audio_volume=0.3
            )
            if video_with_bgm:
                current_video = video_with_bgm
        
        # 5. 자막 번인
        print("\n📌 Phase 5: 자막 추가")
        video_with_subs = self.renderer.add_subtitles(
            current_video, subtitle_path, "combined_with_subs.mp4"
        )
        if video_with_subs:
            current_video = video_with_subs
        
        # 6. 최종 렌더링
        print("\n📌 Phase 6: 최종 렌더링")
        final_output = self.renderer.create_final_render(
            current_video, title=script.get("title", "AI_Anime")
        )
        
        if final_output:
            print("\n" + "=" * 60)
            print("🎉 어셈블리 완료!")
            print("=" * 60)
            print(f"📁 최종 파일: {final_output}")
        
        return final_output


def main():
    """메인 실행"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AI 애니메이션 렌더링")
    parser.add_argument("--action", choices=["concat", "subtitles", "guide", "all"],
                        default="guide", help="실행할 작업")
    parser.add_argument("--script", default="/home/claude/anime-pipeline/scripts/sample_script.json")
    parser.add_argument("--clips", default="/home/claude/anime-pipeline/scenes/clips")
    parser.add_argument("--bgm", default=None, help="BGM 파일 경로")
    
    args = parser.parse_args()
    assembler = ProjectAssembler()
    
    if args.action == "guide":
        if Path(args.script).exists():
            guide = assembler.generate_assembly_guide(args.script)
            print(guide)
            
            guide_path = Path("/home/claude/anime-pipeline/output/ASSEMBLY_GUIDE.txt")
            guide_path.parent.mkdir(parents=True, exist_ok=True)
            with open(guide_path, 'w', encoding='utf-8') as f:
                f.write(guide)
            print(f"\n📄 가이드 저장됨: {guide_path}")
    
    elif args.action == "all":
        result = assembler.full_assembly(args.script, args.clips, args.bgm)
        if result:
            print(f"\n✅ 최종 출력: {result}")
    
    elif args.action == "subtitles":
        if Path(args.script).exists():
            with open(args.script, 'r', encoding='utf-8') as f:
                script = json.load(f)
            srt = assembler.subtitle_gen.create_srt(script.get("scenes", []))
            ass = assembler.subtitle_gen.create_ass(script.get("scenes", []))
            print(f"✓ SRT: {srt}")
            print(f"✓ ASS: {ass}")


if __name__ == "__main__":
    main()
