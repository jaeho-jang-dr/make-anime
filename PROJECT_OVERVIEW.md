# 🎬 혜완이의 밀양 일주일 - 프로젝트 개요

## 프로젝트 정보

```yaml
프로젝트명: 혜완이의 밀양 일주일
영문명: Hyewan's Week in Miryang
장르: 가족 다큐멘터리 / 실사 영상
목표 러닝타임: 10분 (현재 50장면 ≈ 6-7분, 확장 가능)
제작 스타일: Photorealistic Live-Action
타겟 뷰어: 혜완이 (현재 & 미래 20세)
제작 목적: 추억의 기록, 미래로의 선물
```

---

## 📁 프로젝트 파일 구조

```
make-anime/
├── PROJECT_OVERVIEW.md                    ← 이 파일 (프로젝트 개요)
├── README.md                              ← 프로젝트 소개
├── PRODUCTION_STYLE_GUIDE.md              ← 실사 스타일 가이드 ⭐
├── ANIMATION_PRODUCTION_PLAN.md           ← 제작 워크플로우
├── SCRIPT_OUTLINE_TEMPLATE.md             ← 스크립트 템플릿
├── STORY_혜완이의_밀양_일주일.md            ← 원본 스토리
│
└── local_files/
    ├── 일본 애니메이션 제작 앱 기술자료.md
    └── anime-pipeline/
        ├── main_pipeline.py
        ├── config/
        │   └── pipeline_config.json
        ├── scripts/
        │   ├── hyewan_milyang_script.json    ← 제작용 스크립트 ⭐⭐⭐
        │   ├── sample_script.json
        │   ├── step1_script_generator.py
        │   ├── step2_image_generator.py
        │   ├── step3_audio_generator.py
        │   └── step4_render_final.py
        ├── characters/                       ← 실사 캐릭터 이미지 (생성 예정)
        ├── scenes/
        │   ├── clips/                        ← Whisk 생성 영상 (생성 예정)
        │   └── backgrounds/                  ← 실사 배경
        ├── audio/
        │   ├── voice/                        ← 나레이션/대사
        │   ├── bgm/                          ← 배경음악
        │   └── sfx/                          ← 효과음
        └── output/                           ← 최종 영상
```

---

## 🎯 프로젝트 목표

### 핵심 목표

1. **추억의 기록**
   - 혜완이와 외할아버지, 외할머니의 일주일을 영상으로 기록
   - 코딩 배우기, 영어 배우기, 공원 산책 등 일상의 소중한 순간들

2. **미래로의 선물**
   - 혜완이가 20살이 되었을 때 볼 수 있는 타임캡슐
   - "너는 이렇게 사랑받았어"라는 메시지

3. **실사 품질**
   - 애니메이션이 아닌 실사 영화 같은 품질
   - 자연스러운 움직임과 감정 표현
   - 영화적 색감과 조명

### 제작 원칙

```
✅ 실사(Photorealistic) 스타일
✅ 자연스러운 감정 표현
✅ 과장되지 않은 연출
✅ 진정성 있는 기록
❌ 애니메이션 스타일 금지
❌ 과도한 연출 금지
❌ 자랑이나 과시 금지
```

---

## 📖 스토리 개요

### 줄거리

대전에 사는 혜완이가 밀양의 외할아버지, 외할머니 집을 방문합니다.
일주일 동안 할아버지께 코딩을 배우고, 할머니와 영어를 노래하며,
공원에서 뛰어놀고, 할머니 친구 집도 방문합니다.
짧지만 소중한 일주일의 기록입니다.

### 구성 (50개 장면)

```
프롤로그 (장면 1-4): 밀양으로 가는 길
밀양 도착 (장면 5-9): 외할아버지, 외할머니와의 재회
코딩 시간 (장면 10-15): 할아버지와 함께 배우는 코딩
AI와 놀기 (장면 16-19): 컴퓨터와 대화하기
영어 시간 (장면 20-24): 할머니와 영어 동요
할머니 친구 집 (장면 25-28): 어른들의 우정
공원 산책 (장면 29-34): 몸도 공부한다
마지막 밤 (장면 35-39): 일주일은 짧았다
에필로그 (장면 40-50): 이건 기록이다
```

---

## 🎨 제작 스타일

### 비주얼 스타일

**색감**:
```
- Warm golden tones (따뜻한 황금빛)
- Natural colors (자연스러운 색감)
- Slight desaturation (약간의 채도 낮춤)
- Film grain (필름 그레인)
```

**조명**:
```
- Natural lighting (자연광)
- Warm indoor lamp light (따뜻한 실내 조명)
- Golden hour for outdoor (야외는 골든 아워)
- Soft shadows (부드러운 그림자)
```

**카메라워크**:
```
- Cinematic movements (영화적 카메라 움직임)
- Dolly, tracking, pan (다양한 카메라 기법)
- Intimate close-ups (친밀한 클로즈업)
- Natural handheld (자연스러운 핸드헬드)
```

### 오디오 스타일

**음악**:
```
- 따뜻한 피아노
- 어쿠스틱 기타
- 부드러운 스트링
- 감정적이지만 과하지 않게
```

**효과음**:
```
- 키보드 타이핑 소리 (중요!)
- 발소리, 문소리
- 공원의 새소리
- 집안의 따뜻한 ambient
```

**음성**:
```
- 할아버지 나레이션 (따뜻하고 차분한)
- 자연스러운 대화
- 혜완이의 밝은 목소리
```

---

## 🔧 제작 기술 스펙

### 영상 사양

```yaml
해상도: 3840x2160 (4K)
프레임레이트: 24fps
종횡비: 16:9
비트레이트: 50-100 Mbps
비디오 코덱: H.265/HEVC
오디오 코덱: AAC
포맷: MP4
```

### AI 도구

```yaml
스크립트: 완료 (hyewan_milyang_script.json)
캐릭터 생성:
  - Midjourney (포토리얼)
  - Stable Diffusion
  - Leonardo.ai PhotoReal
이미지 생성: Google Gemini Imagen
애니메이션: Google Whisk Animate
음성: Google Cloud TTS / 직접 녹음
렌더링: FFmpeg
색보정: DaVinci Resolve
```

---

## 📋 제작 단계 (5 Phases)

### Phase 1: 프리프로덕션 ✅ (완료)

```
✅ 스토리 기획 완료
✅ 스크립트 작성 완료 (50장면)
✅ 실사 스타일 가이드 작성
✅ 프로젝트 구조 설정
```

---

### Phase 2: 에셋 준비 (진행 예정)

#### 2.1 캐릭터 이미지 생성

**필요한 캐릭터**:
1. 혜완이 (주인공)
2. 외할아버지
3. 외할머니
4. 엄마 (사진용)
5. 아빠 (사진용)
6. 할머니 친구

**생성 방법**:
```python
# Midjourney / Leonardo.ai 사용
# 각 캐릭터당 여러 각도/표정 생성
# 일관성 유지 중요!
```

**프롬프트 예시 (혜완이)**:
```
photorealistic portrait of Korean child,
young girl, bright curious eyes,
natural smile, casual comfortable clothing,
energetic and cheerful appearance,
natural lighting, warm atmosphere,
shot on Canon EOS R5, 50mm f/1.8 lens,
shallow depth of field, 8K quality,
professional photography, film grain
```

#### 2.2 배경 이미지 생성

**필요한 배경**:
1. 기차 내부
2. 밀양 집 외관
3. 밀양 집 거실
4. 컴퓨터 책상
5. 동네 공원
6. 할머니 친구 집

**생성 방법**:
```python
# Midjourney / Leonardo.ai / Stable Diffusion
# 실사 한국 배경 이미지
# 자연스러운 조명과 분위기
```

---

### Phase 3: Whisk 애니메이션 제작

#### 3.1 Whisk 작업 계획

**총 장면**: 50개 (약 6-7분)
**Whisk 월 한도**: 100개
**사용 예정**: 50개 (여유 있음)

#### 3.2 Whisk 워크플로우 (각 장면마다)

```
1. Whisk 접속: https://labs.google/fx/tools/whisk

2. Subject 설정
   └─ 혜완이 캐릭터 이미지 업로드 (일관성!)
   └─ 각 장면에 맞는 캐릭터 각도

3. Scene 설정
   └─ 배경 이미지 업로드 또는 프롬프트 입력
   └─ photorealistic 키워드 필수

4. Style 설정
   └─ 실사 영화 스타일 레퍼런스
   └─ Warm film look

5. Create 클릭
   └─ 정지 이미지 생성

6. ANIMATE 클릭
   └─ 애니메이션 프롬프트 입력
   └─ hyewan_milyang_script.json 참고
   └─ 8초 영상 생성

7. 다운로드
   └─ scene_001.mp4, scene_002.mp4, ...
   └─ scenes/clips/ 폴더에 저장
```

#### 3.3 실사 애니메이션 프롬프트 가이드

**좋은 프롬프트 예시**:
```
✓ "natural walking motion, realistic gait, subtle breathing"
✓ "grandfather talking with natural gestures, warm expression"
✓ "child typing on keyboard with concentration, realistic hand movement"
✓ "smooth dolly shot forward, cinematic camera movement"
```

**피해야 할 것**:
```
❌ "anime-style movement"
❌ "exaggerated motion"
❌ "cartoon effect"
❌ "illustrated style"
```

---

### Phase 4: 오디오 제작

#### 4.1 나레이션 녹음

**나레이션 스크립트** (할아버지 목소리):
```
장면 1: "혜완이는 대전에 산다."
장면 2: "엄마 아빠는 늘 바쁜 의사 선생님이다."
장면 3: "그래서 혜완이는 주로 할머니, 할아버지와 자란다."
장면 4: "하지만 밀양에는… 또 다른 할아버지, 할머니가 있다."
...
```

**녹음 방법**:
1. **직접 녹음** (권장)
   - 할아버지가 직접 녹음
   - 자연스럽고 감정이 담김
   - 스마트폰으로도 가능

2. **TTS 사용** (대안)
   - Google Cloud TTS
   - ElevenLabs (더 자연스러움)

#### 4.2 대사 녹음

**주요 대사**:
```
혜완: "여기 오면 시간이 빨리 가!"
할아버지: "코딩은 외우는 게 아니야. 생각을 글자로 적는 거야."
혜완: "그럼 생각 잘하면 코딩 잘해?"
혜완: "우와!"
할머니: "틀려도 괜찮아. 말하면 돼."
혜완: "다음엔 더 오래 있고 싶어."
```

#### 4.3 BGM 선곡

**추천 BGM**:
```
무료 음원 사이트:
- Pixabay Music: https://pixabay.com/music/
- YouTube Audio Library
- Incompetech

키워드:
- "warm piano family"
- "acoustic guitar gentle"
- "emotional cinematic"
- "peaceful family moment"
```

#### 4.4 효과음

**필요한 효과음**:
```
- 기차 소리
- 키보드 타이핑 (중요!)
- 발소리
- 문 소리
- 공원 새소리
- 바람 소리
- 아이스크림 먹는 소리
```

**무료 효과음 사이트**:
```
- Freesound.org
- Pixabay Sound Effects
- Mixkit
```

---

### Phase 5: 최종 편집 및 렌더링

#### 5.1 비디오 편집

**도구**: DaVinci Resolve (무료) 또는 FFmpeg

**작업 순서**:
```
1. 모든 scene_XXX.mp4 클립을 타임라인에 순서대로 배치
2. 장면 전환 추가 (부드러운 컷 또는 크로스 디졸브)
3. 타이밍 조정 (스크립트 기준)
4. 색보정 적용
```

#### 5.2 색보정 (Color Grading)

**목표 룩**:
```
- Warm family documentary look
- Slight golden tint
- Soft contrast
- Film grain
```

**DaVinci Resolve 설정**:
```
1. 모든 클립 선택
2. Color 탭 이동
3. LUT 적용 또는 수동 조정:
   - Lift (shadows): 약간 따뜻하게
   - Gamma (midtones): 부드럽게
   - Gain (highlights): 약간 golden
4. Film Grain 추가 (미묘하게)
5. Vignette (선택적)
```

#### 5.3 오디오 믹싱

**오디오 레이어**:
```
Layer 1: 나레이션/대사 (최우선, 명확하게)
Layer 2: 효과음 (적절한 볼륨)
Layer 3: BGM (배경, -20dB 정도)
```

**믹싱 팁**:
```
- 나레이션은 항상 명확하게
- BGM은 대사를 방해하지 않게
- 효과음은 자연스럽게
- 전체적으로 따뜻한 사운드
```

#### 5.4 최종 렌더링

**렌더링 설정**:
```yaml
Format: MP4
Resolution: 3840x2160 (4K)
Frame Rate: 24fps
Video Codec: H.265
Audio Codec: AAC
Bitrate: 50-100 Mbps
```

**출력 파일명**:
```
hyewan_milyang_week_final_[날짜].mp4
```

---

## 📊 제작 일정 (예상)

### 타임라인

```
Week 1: 에셋 준비
  - Day 1-2: 캐릭터 이미지 생성 (6명)
  - Day 3-4: 배경 이미지 생성 (주요 장소)
  - Day 5-7: 이미지 정리 및 Whisk 준비

Week 2-3: Whisk 애니메이션
  - 50개 장면 제작
  - 장면당 2-4분 소요
  - 총 3-5시간 (집중 작업)

Week 4: 오디오 제작
  - Day 1-2: 나레이션 녹음
  - Day 3: BGM 선곡
  - Day 4: 효과음 수집
  - Day 5: 오디오 정리

Week 5: 최종 편집
  - Day 1-2: 비디오 편집
  - Day 3: 색보정
  - Day 4: 오디오 믹싱
  - Day 5: 최종 렌더링 및 QA

총 예상 기간: 5주 (여유 있게)
집중 작업 시: 2-3주
```

---

## 💰 예산

### 예상 비용

```yaml
AI 구독:
  - Google One AI Premium: $20/월 (Whisk 100개/월)
  - Claude Max: $20/월 (스크립트 생성 완료)
  - Midjourney: $10/월 (Basic) 또는 무료 대안

음원/효과음: $0 (무료 사이트 이용)

소프트웨어:
  - DaVinci Resolve: 무료
  - FFmpeg: 무료

총 예상 비용: $50/월 (1개월 제작 기준)
```

---

## ✅ 체크리스트

### Pre-Production ✅
- [x] 스토리 기획
- [x] 스크립트 작성 (50장면)
- [x] 실사 스타일 가이드
- [x] 프로젝트 구조 설정

### Production - Assets 🔄
- [ ] 혜완이 캐릭터 이미지 생성
- [ ] 외할아버지 캐릭터 이미지
- [ ] 외할머니 캐릭터 이미지
- [ ] 기타 캐릭터 이미지
- [ ] 주요 배경 이미지 생성

### Production - Animation 📝
- [ ] Whisk에서 장면 1-10 생성
- [ ] Whisk에서 장면 11-20 생성
- [ ] Whisk에서 장면 21-30 생성
- [ ] Whisk에서 장면 31-40 생성
- [ ] Whisk에서 장면 41-50 생성
- [ ] 모든 클립 다운로드 및 정리

### Production - Audio 📝
- [ ] 나레이션 스크립트 최종화
- [ ] 나레이션 녹음
- [ ] 대사 녹음
- [ ] BGM 선곡 및 다운로드
- [ ] 효과음 수집

### Post-Production 📝
- [ ] 비디오 클립 결합
- [ ] 장면 전환 추가
- [ ] 색보정 적용
- [ ] 오디오 믹싱
- [ ] 최종 렌더링
- [ ] QA 및 검수

### Delivery 📝
- [ ] 최종 파일 백업
- [ ] 웹 버전 압축 (선택)
- [ ] 썸네일 제작
- [ ] 배포 (가족 공유)

---

## 🚀 다음 액션 아이템

### 즉시 시작 가능한 작업

1. **캐릭터 이미지 생성** (최우선)
   ```bash
   # Midjourney 또는 Leonardo.ai 사용
   # 프롬프트: PRODUCTION_STYLE_GUIDE.md 참고
   ```

2. **배경 이미지 생성**
   ```bash
   # 주요 장소 이미지 생성
   # 밀양 집, 공원, 기차 등
   ```

3. **나레이션 스크립트 정리**
   ```bash
   # hyewan_milyang_script.json에서 나레이션 추출
   # 녹음 준비
   ```

4. **BGM 선곡 시작**
   ```bash
   # Pixabay Music에서 적절한 BGM 찾기
   # 따뜻한 피아노 계열
   ```

### 다음 미팅 아젠다

1. 캐릭터 이미지 리뷰
2. 배경 이미지 리뷰
3. Whisk 테스트 (샘플 장면 1-2개)
4. 나레이션 녹음 계획
5. 일정 최종 확정

---

## 📝 참고 문서

### 필수 문서
1. **PRODUCTION_STYLE_GUIDE.md** - 실사 스타일 제작 가이드
2. **hyewan_milyang_script.json** - 제작용 스크립트 (50장면)
3. **STORY_혜완이의_밀양_일주일.md** - 원본 스토리

### 참고 문서
4. **ANIMATION_PRODUCTION_PLAN.md** - 전체 워크플로우
5. **SCRIPT_OUTLINE_TEMPLATE.md** - 스크립트 템플릿
6. **README.md** - 프로젝트 소개

---

## 🎯 성공 기준

이 프로젝트는 다음과 같을 때 성공입니다:

1. **감정적 공감**
   - 혜완이가 20살에 보고 감동받을 수 있는 영상
   - 가족의 사랑이 느껴지는 작품

2. **기술적 품질**
   - 실사 수준의 비주얼
   - 자연스러운 움직임
   - 영화적 색감과 조명

3. **진정성**
   - 과장되지 않은 일상
   - 진실된 순간들
   - 시간의 소중함

4. **완성도**
   - 10분 분량 완성
   - 모든 장면 일관성
   - 전문적인 마무리

---

## 💝 프로젝트의 의미

이 프로젝트는 단순한 영상 제작이 아닙니다.

- **사진 몇 장**보다
- **영상 하나**보다
- **"이야기"로 남긴 10분**이 훨씬 오래 갑니다

혜완이가 어른이 되어 이 영상을 볼 때,
"나는 이렇게 사랑받았구나"라고 느낄 수 있다면,
이 프로젝트는 성공입니다.

---

**Made with 💝 for Hyewan's future**

*"그냥... 같이 있었던 시간이다."*
