# 🎥 AI 실사 영상 제작 프로젝트

## 프로젝트 개요

AI를 활용한 **실사(Photorealistic) 스타일 영상 제작** 시스템입니다.

### ⚠️ 중요: 제작 방침

```
🎬 본 프로젝트는 만화/애니메이션 스타일을 지양합니다.
✅ 실사(Live-action) 스타일을 채택하여 동작의 완성도를 높입니다.
```

**핵심 목표**:
- 자연스럽고 사실적인 인물/배경
- 영화 같은 품질의 움직임
- 전문적인 시네마토그래피
- 실사 영화 수준의 최종 결과물

---

## 📁 프로젝트 구조

```
make-anime/
├── README.md                          # 이 파일
├── PRODUCTION_STYLE_GUIDE.md          # ⭐ 실사 스타일 제작 가이드 (필독!)
├── ANIMATION_PRODUCTION_PLAN.md       # 전체 제작 워크플로우
├── SCRIPT_OUTLINE_TEMPLATE.md         # 스크립트 작성 템플릿
│
└── local_files/
    ├── 일본 애니메이션 제작 앱 기술자료.md
    └── anime-pipeline/
        ├── main_pipeline.py           # 메인 실행 파일
        ├── config/
        │   └── pipeline_config.json
        ├── scripts/
        │   ├── step1_script_generator.py
        │   ├── step2_image_generator.py
        │   ├── step3_audio_generator.py
        │   └── step4_render_final.py
        ├── characters/                # 실사 캐릭터 이미지
        ├── scenes/
        │   ├── clips/                 # Whisk 생성 영상 클립
        │   └── backgrounds/           # 실사 배경
        ├── audio/
        │   ├── voice/
        │   ├── bgm/
        │   └── sfx/
        └── output/                    # 최종 출력
```

---

## 🚀 빠른 시작

### 1. 문서 읽기 (중요!)

제작을 시작하기 전에 반드시 읽어야 할 문서:

```
필수 순서:
1. PRODUCTION_STYLE_GUIDE.md     ← 실사 스타일 정의 (가장 중요!)
2. ANIMATION_PRODUCTION_PLAN.md  ← 전체 워크플로우
3. SCRIPT_OUTLINE_TEMPLATE.md    ← 스크립트 작성법
```

### 2. 제작 시작

```bash
# 프로젝트 디렉토리로 이동
cd local_files/anime-pipeline

# 전체 파이프라인 실행 (준비 단계)
python main_pipeline.py --mode full

# Whisk에서 실사 스타일로 영상 생성 (수동)
# → PRODUCTION_STYLE_GUIDE.md의 프롬프트 사용

# 최종 렌더링
python main_pipeline.py --mode render
```

---

## 📖 주요 문서 설명

### 1. PRODUCTION_STYLE_GUIDE.md ⭐

**가장 중요한 문서!** 실사 스타일 제작의 모든 것.

**포함 내용**:
- ❌ 지양할 것: 애니메이션/만화 스타일
- ✅ 추구할 것: 포토리얼리즘, 영화적 품질
- 실사 캐릭터/배경 생성 프롬프트
- 자연스러운 모션 프롬프트
- 영화적 조명/색보정 기법
- 카메라워크 (Dolly, Tracking, Crane 등)

**반드시 참고하세요!**

### 2. ANIMATION_PRODUCTION_PLAN.md

**전체 제작 프로세스** 상세 가이드.

**포함 내용**:
- 5단계 워크플로우 (프리프로덕션 → 포스트프로덕션)
- 시간/비용 관리
- Whisk 할당량 관리
- 기술적 고려사항
- 체크리스트

### 3. SCRIPT_OUTLINE_TEMPLATE.md

**스크립트 작성 템플릿**.

**포함 내용**:
- 스토리 구조 (3막 구조)
- 캐릭터 설정
- 장면별 스크립트 템플릿
- 프롬프트 예시

---

## 🎯 실사 스타일 핵심 원칙

### 프롬프트 작성 시

**필수 키워드**:
```
✓ photorealistic
✓ cinematic
✓ realistic
✓ natural
✓ film quality
✓ professional photography
✓ 8K resolution
```

**금지 키워드**:
```
❌ anime
❌ manga
❌ cartoon
❌ illustrated
❌ 2D art style
❌ cel shaded
```

### 움직임 생성 시

**자연스러운 모션**:
```
✓ "natural realistic walking motion"
✓ "subtle breathing movement"
✓ "realistic facial expressions"
✓ "smooth cinematic camera movement"
```

**지양할 것**:
```
❌ "anime-style movement"
❌ "exaggerated motion"
❌ "bouncy animation"
```

---

## 🛠️ 도구 & 기술 스택

### AI 생성 도구

```yaml
스크립트: Claude Code
캐릭터/배경:
  - Midjourney (포토리얼)
  - Stable Diffusion (Realistic models)
  - Leonardo.ai (PhotoReal)
  - Google Imagen 3
애니메이션: Google Whisk Animate
음성: Google Cloud TTS / ElevenLabs
렌더링: FFmpeg
색보정: DaVinci Resolve
```

### 영상 스펙

```yaml
해상도: 1920x1080 (Full HD) ~ 3840x2160 (4K)
프레임레이트: 24fps (영화 표준)
종횡비: 16:9 또는 2.39:1 (Cinemascope)
비트레이트: 4K 기준 50-100 Mbps
코덱: H.264 / H.265
```

---

## 📚 학습 리소스

### 영화 제작 기법
- "Cinematography: Theory and Practice"
- YouTube: Every Frame a Painting
- DaVinci Resolve 공식 트레이닝

### AI 실사 생성
- Midjourney 포토리얼 가이드
- Stable Diffusion Realistic Checkpoints
- Leonardo.ai PhotoReal 문서

### 색보정
- Teal & Orange Look
- Film Grain 추가
- LUT (Look-Up Table) 활용

---

## 🎬 제작 예시

### 좋은 예 (실사 스타일)

**캐릭터 프롬프트**:
```
medium shot photorealistic portrait,
woman in her late 20s, natural beauty,
brown hair, green eyes, realistic skin texture,
wearing dark blue coat,
natural lighting, soft shadows,
shot on Canon EOS R5, 50mm lens,
8K quality, film grain, cinematic
```

**애니메이션 프롬프트**:
```
natural walking motion, realistic gait,
subtle breathing, clothing physics,
cinematic camera dolly forward
```

### 나쁜 예 (애니메이션 스타일 - 지양)

**캐릭터 프롬프트**:
```
❌ anime style character portrait
❌ manga girl, vibrant colors
❌ Makoto Shinkai style
```

---

## 📝 체크리스트

제작 전 확인:

- [ ] PRODUCTION_STYLE_GUIDE.md를 읽었는가?
- [ ] 프롬프트에 "photorealistic" 키워드를 포함했는가?
- [ ] 애니메이션 키워드를 제거했는가?
- [ ] 영화적 카메라워크를 계획했는가?
- [ ] 색보정 방향을 정했는가? (Teal & Orange 등)

---

## 🎯 목표

**최종 결과물**:
- 실사 영화 같은 품질
- 자연스러운 인물 움직임
- 전문적인 시네마토그래피
- 영화 수준의 색감/조명

**이 프로젝트는 애니메이션이 아닌 실사 영화 제작입니다!**

---

## 📞 문의

질문이나 제안이 있다면 이슈를 등록해주세요.

Made with 🎥 Photorealistic AI Filmmaking
