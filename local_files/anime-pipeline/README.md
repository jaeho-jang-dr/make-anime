# 🎬 AI 애니메이션 파이프라인

**Claude CLI + Gemini + Grok + Google Whisk 통합 워크플로우**

10분 분량의 일본 애니메이션을 AI만으로 제작하는 파이프라인입니다.

---

## 📋 요구사항

### 필수
- Google Antigravity (Google IDX) 환경
- Google One AI Premium (Ultra) 구독 → Whisk Animate 월 100개
- Python 3.10+

### 선택 (기능 향상)
- Claude CLI (`claude` 명령어) → 고품질 스크립트 생성
- Gemini API Key → 프롬프트 최적화
- Grok API Key → 창의적 보조
- FFmpeg → 로컬 렌더링

---

## 🚀 빠른 시작

```bash
# 1. 프로젝트 디렉토리 이동
cd /home/claude/anime-pipeline

# 2. 전체 파이프라인 실행 (준비 단계)
python main_pipeline.py --mode full

# 3. Whisk에서 수동 작업 (아래 가이드 참조)

# 4. 클립 준비 후 렌더링
python main_pipeline.py --mode render
```

---

## 📁 디렉토리 구조

```
anime-pipeline/
├── main_pipeline.py          # 메인 실행 파일
├── config/
│   └── pipeline_config.json  # 설정 파일
├── scripts/
│   ├── step1_script_generator.py   # 스크립트 생성
│   ├── step2_image_generator.py    # 이미지 프롬프트
│   ├── step3_audio_generator.py    # 오디오 생성
│   ├── step4_render_final.py       # 최종 렌더링
│   └── anime_script.json           # 생성된 스크립트
├── characters/               # 캐릭터 프롬프트
├── scenes/
│   ├── clips/               # Whisk 영상 클립 (여기에 저장!)
│   └── backgrounds/         # 배경 이미지
├── audio/
│   ├── voice/              # 대사/나레이션
│   ├── bgm/                # 배경음악
│   └── sfx/                # 효과음
└── output/                 # 최종 출력
```

---

## 🔧 단계별 워크플로우

### Step 1: 스크립트 생성 (Claude)

```bash
# 샘플 스크립트 사용
python main_pipeline.py --mode script

# 새 스크립트 생성 (Claude CLI 필요)
python main_pipeline.py --mode script --genre SF --duration 5 --no-sample
```

**출력:**
- `scripts/anime_script.json` - 전체 스크립트
- 캐릭터 정보, 장면별 프롬프트 포함

---

### Step 2: 이미지 프롬프트 생성 (Gemini)

```bash
python main_pipeline.py --mode images
```

**출력:**
- `characters/` - 캐릭터 이미지 프롬프트
- `scenes/` - 장면별 Whisk 입력 데이터
- `WHISK_WORKFLOW_GUIDE.txt` - Whisk 작업 가이드

---

### Step 3: 오디오 생성 (Google TTS + Grok)

```bash
python main_pipeline.py --mode audio
```

**출력:**
- `audio/` - 음성 파일 또는 스크립트
- `SFX_GUIDE.txt` - 효과음 수집 가이드
- `BGM_GUIDE.txt` - 배경음악 추천

---

### Step 4: Whisk 작업 (수동) ⚠️

이 단계는 **수동으로** 진행해야 합니다.

#### 4-1. Whisk 접속
- https://labs.google/fx/tools/whisk

#### 4-2. 캐릭터 Subject 이미지 생성
1. `characters/` 폴더의 프롬프트 확인
2. Whisk의 Subject에 프롬프트로 이미지 생성
3. 이미지 다운로드 및 저장

#### 4-3. 장면별 이미지 생성
1. `scenes/whisk_scene_XXX.json` 파일 확인
2. Subject: 캐릭터 이미지 업로드 (일관성 유지!)
3. Scene: 배경 프롬프트 입력
4. Style: 스타일 레퍼런스 업로드
5. Create 클릭

#### 4-4. Whisk Animate
1. 생성된 이미지에서 **ANIMATE** 클릭
2. `animation_prompt` 입력 (예: "walking slowly, wind blowing")
3. 8초 영상 생성 및 다운로드
4. **파일명**: `scene_001.mp4`, `scene_002.mp4`, ...
5. **저장 위치**: `scenes/clips/`

#### 💡 팁
- 캐릭터 Subject 이미지는 모든 장면에서 **동일하게** 사용
- Style 이미지도 고정하여 톤 통일
- 월 100개 제한 → 75개 장면이면 충분

---

### Step 5: 최종 렌더링 (FFmpeg)

```bash
# 클립이 준비되면
python main_pipeline.py --mode render

# BGM 포함
python main_pipeline.py --mode render --bgm audio/bgm/my_bgm.mp3
```

---

## 🎮 명령어 요약

| 명령어 | 설명 |
|--------|------|
| `--mode status` | 프로젝트 상태 확인 |
| `--mode full` | 전체 파이프라인 (준비) |
| `--mode script` | 스크립트만 생성 |
| `--mode images` | 이미지 프롬프트만 |
| `--mode audio` | 오디오만 |
| `--mode render` | 최종 렌더링 |
| `--mode guide` | 어셈블리 가이드 |

---

## 💰 비용

| 항목 | 비용 |
|------|------|
| Claude Max | 구독 포함 |
| Gemini Ultra + Whisk | 구독 포함 |
| Google Cloud TTS | 무료 티어 |
| Grok API | 보유 중 |
| **총합** | **$0** |

---

## 📊 예상 소요 시간

| 단계 | 시간 |
|------|------|
| 스크립트 생성 | 5-10분 |
| 이미지 프롬프트 | 5분 |
| 오디오 준비 | 10분 |
| Whisk 작업 (75장면) | 3-5시간 |
| 렌더링 | 30분-1시간 |
| **총합** | **약 5-7시간** |

---

## 🔗 무료 리소스

### 효과음
- [Freesound](https://freesound.org)
- [Pixabay Sound Effects](https://pixabay.com/sound-effects/)
- [Mixkit](https://mixkit.co/free-sound-effects/)

### BGM
- [Pixabay Music](https://pixabay.com/music/)
- [YouTube Audio Library](https://studio.youtube.com/channel/audio)
- [Incompetech](https://incompetech.com/music/)

### 편집
- [CapCut](https://www.capcut.com/) (무료)
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) (무료)

---

## ❓ 문제 해결

### Whisk에서 캐릭터가 달라 보여요
→ 같은 Subject 이미지를 계속 사용하세요.
→ Style 이미지도 고정하세요.

### 클립 연결이 안 돼요
→ FFmpeg 설치 확인: `ffmpeg -version`
→ 클립 파일명이 올바른지 확인: `scene_001.mp4`

### TTS 음질이 안 좋아요
→ ElevenLabs 무료 플랜 사용 고려
→ 또는 직접 녹음

---

## 📝 라이선스

개인 프로젝트용. 생성된 콘텐츠의 저작권은 사용자에게 있습니다.
(단, 각 AI 서비스의 이용약관을 확인하세요)

---

Made with 🎬 Claude + Gemini + Grok + Whisk
