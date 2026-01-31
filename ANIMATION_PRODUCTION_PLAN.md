# 🎬 AI 애니메이션 제작 마스터 플랜

## 📋 프로젝트 개요

**목표**: AI 기반 도구를 활용한 10분 분량 일본 애니메이션 자동 제작 시스템

**핵심 기술 스택**:
- Claude Code (스토리/스크립트 생성)
- Google Gemini (캐릭터/장면 디자인)
- Google Whisk (이미지 생성 & 애니메이션)
- Grok (음악/창의적 보조)
- FFmpeg (최종 렌더링)

**예상 제작 기간**: 5-7시간 (1개 에피소드 기준)

---

## 🎯 제작 워크플로우 (5단계)

### Phase 1: 프리프로덕션 (기획 단계)

#### 1.1 스토리 컨셉 정의
```
- 장르 선택 (판타지, SF, 일상, 액션 등)
- 타겟 길이 (5분, 10분, 15분)
- 핵심 테마 (모험과 성장, 우정, 사랑, 복수 등)
- 톤앤매너 (밝고 경쾌, 어둡고 진지, 코믹 등)
```

#### 1.2 세계관 설정
```
- 시대/배경 (현대, 미래, 판타지 세계 등)
- 핵심 설정 (마법 시스템, 기술 수준, 사회 구조)
- 비주얼 스타일 (신카이 마코토, 지브리, 쿄애니 등)
```

#### 1.3 캐릭터 디자인
```
- 주인공 설정 (이름, 나이, 성격, 외모)
- 서브 캐릭터 (2-3명)
- 캐릭터 관계도
- 캐릭터별 비주얼 키워드
```

---

### Phase 2: 스크립트 생성 (AI 기반)

**사용 도구**: Claude Code CLI

**프로세스**:
```bash
# 방법 1: 샘플 스크립트 사용 (빠른 테스트)
python main_pipeline.py --mode script

# 방법 2: 커스텀 스크립트 생성 (Claude CLI 필요)
python main_pipeline.py --mode script \
  --genre "다크 판타지" \
  --duration 10 \
  --theme "상실한 별을 되찾는 여정" \
  --no-sample
```

**출력물**:
- `scripts/anime_script.json`
  - 전체 시놉시스
  - 캐릭터 정보
  - 장면별 스크립트 (75개 @ 8초/장면)
  - 대사/나레이션
  - 카메라 지시사항

**스크립트 구조**:
```json
{
  "title": "애니메이션 제목",
  "genre": "장르",
  "synopsis": "전체 줄거리",
  "characters": [
    {
      "name": "캐릭터명",
      "age": 16,
      "appearance": "비주얼 설명",
      "personality": "성격 특징"
    }
  ],
  "scenes": [
    {
      "scene_number": 1,
      "location": "장소",
      "time": "시간대",
      "description": "장면 설명",
      "dialogue": "대사",
      "camera": "카메라 움직임",
      "mood": "분위기"
    }
  ]
}
```

---

### Phase 3: 비주얼 에셋 준비

#### 3.1 캐릭터 이미지 생성

**사용 도구**: Google Gemini + Whisk

```bash
python main_pipeline.py --mode images
```

**프로세스**:
1. Gemini가 각 캐릭터의 상세 프롬프트 생성
2. `characters/` 폴더에 프롬프트 저장
3. Whisk에서 Subject 이미지로 캐릭터 생성
4. 일관성 유지를 위해 동일 캐릭터 이미지 재사용

**출력물**:
- `characters/char_[이름]_[타임스탬프]_prompt.json`

**캐릭터 프롬프트 예시**:
```
masterpiece, best quality, anime style character portrait,
young girl, 16 years old, long silver hair, bright blue eyes,
wearing a dark blue cloak with star patterns,
holding a glowing lantern, determined expression,
Makoto Shinkai style - vibrant colors and light expression,
clean lineart, detailed face and eyes,
white background for easy extraction,
full body shot, professional anime character design sheet
```

#### 3.2 장면 이미지 & 애니메이션 생성

**사용 도구**: Google Whisk (수동 작업)

**한도**: 월 100개 (Google One AI Premium)

**프로세스** (각 장면마다):

```
1. Whisk 접속: https://labs.google/fx/tools/whisk

2. 3개 입력 요소 설정:

   [Subject] - 캐릭터
   └─ 미리 생성한 캐릭터 이미지 업로드 (일관성 유지!)

   [Scene] - 배경
   └─ 장면 설명 프롬프트 입력
      예: "dark fantasy village at night, misty atmosphere"

   [Style] - 스타일 레퍼런스
   └─ 색상/스타일 샘플 이미지 업로드
      예: "Makoto Shinkai style, deep blue and gold palette"

3. [Create] 클릭 → 정지 이미지 생성

4. [ANIMATE] 버튼 클릭
   └─ 모션 프롬프트 입력:
      예: "slow pan across village, mist moving, flickering lights"
   └─ 8초 영상 생성

5. 다운로드
   └─ 파일명: scene_001.mp4, scene_002.mp4, ...
   └─ 저장 위치: scenes/clips/
```

**출력물**:
- `scenes/whisk_scene_001.json` (작업 가이드)
- `scenes/clips/scene_001.mp4` (최종 비디오)
- `WHISK_WORKFLOW_GUIDE.txt` (배치 작업 가이드)

**최적화 팁**:
- 캐릭터 Subject 이미지는 모든 장면에서 동일하게 사용
- Style 이미지도 고정하여 전체 톤 통일
- 실패한 장면은 스킵 후 나중에 재시도
- 75개 장면 = 월 할당량의 75% 사용

---

### Phase 4: 오디오 제작

**사용 도구**: Google Cloud TTS, Grok, 무료 음원 사이트

```bash
python main_pipeline.py --mode audio
```

#### 4.1 음성 (Voice)

**대사/나레이션**:
- Google Cloud TTS (무료 티어)
- 또는 ElevenLabs (월 10,000자 무료)

**프로세스**:
1. 스크립트에서 대사 추출
2. TTS API로 음성 파일 생성
3. `audio/voice/` 폴더에 저장

**출력물**:
- `audio/dialogue_001_[타임스탬프]_script.txt`
- `audio/narration_001_[타임스탬프]_script.txt`

#### 4.2 배경음악 (BGM)

**무료 음원 사이트**:
- Pixabay Music (https://pixabay.com/music/)
- YouTube Audio Library
- Incompetech (CC 라이선스)

**가이드 문서**:
- `audio/BGM_GUIDE.txt`

**추천 키워드**:
```
- 판타지 → "epic orchestral", "fantasy adventure"
- SF → "futuristic", "synthwave"
- 일상 → "peaceful piano", "slice of life"
- 액션 → "intense battle", "dramatic"
```

#### 4.3 효과음 (SFX)

**무료 효과음 사이트**:
- Freesound.org
- Pixabay Sound Effects
- Mixkit

**가이드 문서**:
- `audio/SFX_GUIDE.txt`

**필요한 효과음 예시**:
```
- 발소리 (footsteps)
- 문 열림/닫힘 (door open/close)
- 마법 효과 (magic spell, whoosh)
- 환경음 (wind, rain, crowd)
```

---

### Phase 5: 포스트프로덕션 (최종 렌더링)

**사용 도구**: FFmpeg

```bash
# 기본 렌더링
python main_pipeline.py --mode render

# BGM 포함 렌더링
python main_pipeline.py --mode render \
  --bgm audio/bgm/epic_fantasy.mp3
```

#### 5.1 비디오 편집

**프로세스**:
1. 모든 scene_XXX.mp4 클립을 순서대로 결합
2. 트랜지션 추가 (페이드, 컷)
3. 타이밍 조정 (스크립트 기준)

#### 5.2 오디오 믹싱

**레이어 구성**:
```
[Layer 1] 대사/나레이션 (최우선)
[Layer 2] 효과음
[Layer 3] 배경음악 (볼륨 -20dB)
```

**출력 설정**:
```json
{
  "format": "mp4",
  "resolution": "1280x720 (720p)",
  "fps": 24,
  "video_codec": "libx264",
  "audio_codec": "aac",
  "bitrate": "4000k"
}
```

#### 5.3 최종 출력

**출력물**:
- `output/final_anime_[날짜].mp4`

**검수 체크리스트**:
- [ ] 모든 장면이 순서대로 연결되었는가?
- [ ] 대사와 립싱크가 맞는가?
- [ ] BGM 볼륨이 대사를 방해하지 않는가?
- [ ] 색감과 톤이 일관적인가?
- [ ] 오프닝/엔딩 크레딧이 있는가?

---

## 📊 리소스 관리

### 시간 배분 (10분 애니메이션 기준)

| 단계 | 예상 소요 시간 | 비고 |
|------|----------------|------|
| 1. 기획 & 컨셉 | 30분 | 수동 작업 |
| 2. 스크립트 생성 | 5-10분 | Claude 자동 |
| 3. 이미지 프롬프트 | 5분 | Gemini 자동 |
| 4. Whisk 작업 (75장면) | 3-5시간 | 수동 (장면당 2-4분) |
| 5. 오디오 준비 | 10분 | 반자동 |
| 6. 최종 렌더링 | 30-60분 | FFmpeg 자동 |
| **총합** | **5-7시간** | |

### 비용 분석 (월간)

| 항목 | 비용 | 노트 |
|------|------|------|
| Claude Max 구독 | $20 | 무제한 스크립트 생성 |
| Google One AI Premium | $20 | Gemini + Whisk 100개/월 |
| Google Cloud TTS | $0 | 무료 티어 (월 100만자) |
| Grok API | $5 | 프리 크레딧 포함 |
| 음원/효과음 | $0 | 무료 사이트 이용 |
| **총 월간 비용** | **$45** | **1-2개 에피소드 제작 가능** |

### Whisk 할당량 관리

**월 100개 제한 전략**:
```
- 10분 애니메이션 = 75 장면 (8초/장면)
- 5분 애니메이션 = 37 장면
- 3분 애니메이션 = 22 장면

→ 전략 1: 10분 1개 + 3분 1개 (97개)
→ 전략 2: 5분 2개 (74개)
→ 전략 3: 3분 4개 (88개)
```

---

## 🛠️ 기술적 고려사항

### 일관성 유지 전략

**캐릭터 일관성**:
1. 첫 장면에서 생성한 캐릭터 이미지를 모든 Whisk Subject로 재사용
2. 캐릭터별 프롬프트를 고정하고 문서화
3. 각도/표정 변화가 필요하면 애니메이션 프롬프트로 제어

**스타일 일관성**:
1. 스타일 레퍼런스 이미지 1개로 고정
2. 색상 팔레트 문서화 (예: "deep blue #1a2844, gold #ffd700")
3. 조명 설정 일관성 유지 (시간대 고정)

**시간적 연속성**:
1. 장면 전환 시 유사한 구도로 시작
2. 캐릭터 의상/소지품 일관성 체크
3. 배경 시간대/날씨 연속성

### 애니메이션 품질 향상 팁

**Whisk 애니메이션 프롬프트 작성법**:

```
좋은 예:
✓ "girl walking slowly forward, wind gently blowing hair and cloak"
✓ "camera slowly panning left to right, mist moving across ground"
✓ "lantern light flickering, shadows dancing on walls"

나쁜 예:
✗ "epic action scene" (너무 추상적)
✗ "character doing many things" (복잡함)
✗ "fast movement" (8초 제약에 부적합)
```

**모션 타입별 키워드**:
```
- 느린 움직임: slowly, gently, subtle
- 카메라 움직임: pan, zoom, dolly, crane
- 환경 효과: wind blowing, mist moving, light flickering
- 캐릭터 동작: walking, turning head, breathing, blinking
```

### FFmpeg 렌더링 최적화

**고품질 설정**:
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset slow -crf 18 \
  -c:a aac -b:a 192k \
  output.mp4
```

**빠른 프리뷰**:
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset ultrafast -crf 23 \
  preview.mp4
```

---

## 📚 애니메이션 제작 원칙

### Disney 12원칙 적용

1. **Squash & Stretch** (압축과 늘림)
   - Whisk에서 "squashing down" / "stretching up" 프롬프트

2. **Anticipation** (예비 동작)
   - "preparing to jump" / "winding up before action"

3. **Staging** (연출)
   - 카메라 각도와 구도에 집중
   - "wide shot" / "close-up on face"

4. **Timing** (타이밍)
   - 8초 제약 고려
   - 중요한 순간에 시간 할애

5. **Arcs** (호 궤적)
   - "moving in smooth arc" / "graceful motion"

6. **Secondary Action** (부수 동작)
   - "hair flowing while walking" / "cloak billowing"

7. **Appeal** (매력)
   - 캐릭터 디자인 단계에서 고려
   - "charming expression" / "appealing pose"

### 일본 애니메이션 스타일링

**프레임 레이트**:
- 24fps 기준
- Limited animation (정지화 활용)

**색상 팔레트**:
```
신카이 마코토 스타일:
- 선명한 색감
- 강한 대비
- 따뜻한/차가운 색 대비
- 빛의 표현 강조

지브리 스타일:
- 자연스러운 색감
- 파스텔 톤
- 따뜻한 분위기
- 손그림 느낌
```

**카메라워크**:
```
- 긴 정적 샷 (contemplative scenes)
- 느린 패닝 (landscape shots)
- 클로즈업 (감정적 순간)
- 로우 앵글 (dramatic moments)
```

---

## 🎯 프로젝트 체크리스트

### 프리프로덕션
- [ ] 장르/테마/컨셉 확정
- [ ] 캐릭터 설정 작성 (3명 이상)
- [ ] 러프 줄거리 작성
- [ ] 비주얼 스타일 레퍼런스 수집

### 프로덕션
- [ ] Claude로 스크립트 생성 완료
- [ ] Gemini로 이미지 프롬프트 생성
- [ ] Whisk에서 캐릭터 Subject 생성
- [ ] Whisk에서 75개 장면 애니메이션 생성
- [ ] 모든 클립 다운로드 및 정리

### 오디오
- [ ] 대사/나레이션 TTS 생성
- [ ] BGM 선곡 및 다운로드
- [ ] 필요한 효과음 수집

### 포스트프로덕션
- [ ] FFmpeg로 비디오 결합
- [ ] 오디오 믹싱 및 싱크 조정
- [ ] 오프닝/엔딩 추가
- [ ] 최종 품질 검수
- [ ] 출력 및 백업

---

## 🚀 다음 단계

### 지금 바로 시작하기

```bash
# 1. 프로젝트 상태 확인
cd local_files/anime-pipeline
python main_pipeline.py --mode status

# 2. 샘플로 테스트 (빠른 시작)
python main_pipeline.py --mode full

# 3. 또는 커스텀 스크립트 생성
python main_pipeline.py --mode script \
  --genre "당신의 장르" \
  --duration 10 \
  --theme "당신의 테마" \
  --no-sample

# 4. Whisk 작업 가이드 확인
cat WHISK_WORKFLOW_GUIDE.txt

# 5. 클립 준비 후 렌더링
python main_pipeline.py --mode render
```

### 추가 학습 리소스

**애니메이션 이론**:
- Disney Animation: The Illusion of Life (책)
- Animator's Survival Kit (Richard Williams)
- Clip Studio Tips (일본 애니메이터 실전 팁)

**AI 도구 활용**:
- Google Whisk 공식 가이드
- Gemini 프롬프팅 베스트 프랙티스
- Claude Code 문서

**무료 에셋**:
- itch.io (애니메이션 에셋)
- OpenGameArt (배경/스프라이트)
- Freesound (효과음)

---

## 📝 마무리

이 파이프라인은 **완전 자동화된 AI 애니메이션 제작 시스템**입니다.

**핵심 장점**:
- 전문 애니메이터 없이도 고품질 애니메이션 제작 가능
- 반복 작업은 AI가 자동화
- 창의적인 부분에만 집중 가능
- 비용 효율적 ($45/월로 1-2개 에피소드)

**시작하세요!** 당신의 상상력만 있으면 됩니다.

Made with 🎬 Claude + Gemini + Grok + Whisk
