# 🚀 다음 단계 - 빠른 시작 가이드

## 현재 상태 ✅

```
✅ 프로젝트 구조 완성
✅ 스토리 완성
✅ 스크립트 완성 (50장면, 실사 스타일)
✅ 제작 가이드 완성
✅ 프로젝트 개요 완성
```

---

## 🎯 다음 작업 (우선순위 순)

### 1️⃣ 캐릭터 이미지 생성 (최우선)

**필요한 캐릭터**:
- 혜완이 (주인공) - 가장 중요!
- 외할아버지
- 외할머니
- 엄마 (사진용)
- 아빠 (사진용)
- 할머니 친구 (1명)

**도구 선택**:

Option 1: **Midjourney** (추천, 고품질)
```bash
# https://www.midjourney.com
# Discord에서 사용
# 프롬프트 예시는 아래 참고
```

Option 2: **Leonardo.ai** (무료 플랜 가능)
```bash
# https://leonardo.ai
# PhotoReal 모드 사용
# 하루 150 토큰 무료
```

Option 3: **Stable Diffusion** (완전 무료)
```bash
# https://stablediffusionweb.com
# 또는 로컬 설치
```

**프롬프트 템플릿**:

혜완이:
```
photorealistic portrait of Korean child,
young girl, 8-10 years old, bright curious eyes,
natural cheerful smile, casual comfortable clothing,
energetic and happy appearance,
natural window lighting, soft warm atmosphere,
shot on Canon EOS R5, 50mm f/1.8 lens,
shallow depth of field, bokeh background,
professional family photography style,
8K ultra quality, slight film grain,
white or neutral background for easy extraction
```

외할아버지:
```
photorealistic portrait of Korean elderly grandfather,
kind warm eyes, gentle loving expression,
comfortable casual home clothing,
natural skin texture with age,
sitting at computer desk pose,
warm indoor lamp lighting,
shot on Canon EOS R5, 85mm f/1.4 lens,
shallow depth of field,
professional portrait photography,
8K quality, film grain,
neutral background
```

외할머니:
```
photorealistic portrait of Korean elderly grandmother,
warm loving smile, cheerful expression,
comfortable home clothing,
natural skin texture with age,
standing or sitting in home environment,
natural afternoon lighting,
shot on Canon EOS R5, 85mm f/1.4 lens,
professional family photography,
8K quality, slight film grain,
neutral background
```

**생성 팁**:
```
1. 각 캐릭터당 여러 버전 생성 (3-5개)
2. 다양한 각도: 정면, 옆모습, 3/4 뷰
3. 다양한 표정: 미소, 집중, 생각하는 모습
4. 일관성 유지: 같은 프롬프트 기반으로
5. 배경은 neutral/white로 (합성 용이)
```

**저장 위치**:
```
local_files/anime-pipeline/characters/
├── hyewan_front.png
├── hyewan_side.png
├── hyewan_smile.png
├── grandfather_front.png
├── grandfather_typing.png
├── grandmother_front.png
└── ...
```

---

### 2️⃣ 배경 이미지 생성

**필요한 배경** (우선순위 순):

1. **밀양 집 거실**
   ```
   photorealistic Korean home interior living room,
   cozy family atmosphere, computer desk visible,
   warm afternoon sunlight through windows,
   traditional-modern mixed style,
   natural lighting, warm colors,
   professional interior photography,
   8K quality, film grain
   ```

2. **컴퓨터 책상 클로즈업**
   ```
   photorealistic computer desk setup,
   keyboard and monitor visible,
   warm desk lamp lighting,
   cozy home office environment,
   Korean home style,
   natural details, lived-in feel,
   professional photography, 8K quality
   ```

3. **동네 공원**
   ```
   photorealistic Korean neighborhood park,
   walking paths, trees, benches,
   natural daylight, peaceful atmosphere,
   suburban park setting,
   landscape photography,
   8K quality, natural colors
   ```

4. **기차 창문 뷰**
   ```
   photorealistic train window interior view,
   Korean countryside landscape outside,
   natural daylight, reflections on glass,
   travel photography style,
   8K quality, cinematic
   ```

5. **밀양 집 외관**
   ```
   photorealistic Korean traditional-modern house exterior,
   small yard, residential neighborhood,
   warm afternoon lighting,
   architectural photography,
   8K quality, natural atmosphere
   ```

**저장 위치**:
```
local_files/anime-pipeline/scenes/backgrounds/
├── milyang_house_exterior.png
├── living_room_interior.png
├── computer_desk.png
├── park_view.png
├── train_window.png
└── ...
```

---

### 3️⃣ Whisk 테스트 (샘플 장면)

**테스트 목적**: Whisk 워크플로우 익히기

**테스트할 장면**: 장면 10번 (키보드 클로즈업)

**Whisk 워크플로우**:

1. **Whisk 접속**
   ```
   https://labs.google/fx/tools/whisk
   ```

2. **Subject 업로드**
   ```
   - 혜완이 손 이미지 + 할아버지 손 이미지
   - 또는 키보드와 손 합성 이미지
   ```

3. **Scene 입력**
   ```
   photorealistic close-up of computer keyboard,
   child's small hands and elderly grandfather's hands together,
   natural skin texture, warm desk lamp lighting,
   macro photography style, 8K quality
   ```

4. **Style 레퍼런스**
   ```
   - 따뜻한 가족 사진 스타일 이미지 업로드
   - 또는 프롬프트:
     "warm family documentary style, film grain, golden tones"
   ```

5. **Create** 클릭
   ```
   - 정지 이미지 생성 대기
   ```

6. **ANIMATE** 클릭
   ```
   애니메이션 프롬프트 입력:
   "fingers typing on keyboard, realistic hand movements,
    natural typing rhythm, hands occasionally touching"
   ```

7. **다운로드**
   ```
   - 8초 영상 생성 대기
   - scene_010_test.mp4로 저장
   ```

**테스트 성공 기준**:
- [ ] 실사 같은 비주얼
- [ ] 자연스러운 손 움직임
- [ ] 따뜻한 색감 유지
- [ ] 8초 길이 확인

---

### 4️⃣ 나레이션 준비

**나레이션 스크립트 추출**:

```bash
# 아래 나레이션만 따로 정리
```

**나레이션 리스트**:
```
장면 1: "혜완이는 대전에 산다."
장면 2: "엄마 아빠는 늘 바쁜 의사 선생님이다."
장면 3: "그래서 혜완이는 주로 할머니, 할아버지와 자란다."
장면 4: "하지만 밀양에는… 또 다른 할아버지, 할머니가 있다."
장면 19: "기계는 똑똑해질 수 있지만, 질문하는 건 언제나 사람이다."
장면 27: "혜완이는 이날, 어른에게도 친구가 있다는 걸 배웠다."
장면 33: "머리만 크면 안 된다. 몸도 같이 커야지."
장면 40: "이 일주일은..."
장면 41: "공부도..."
장면 42: "놀이도..."
장면 43: "여행도 아니었다."
장면 47: "그냥... 같이 있었던 시간이다."
```

**녹음 방법**:

Option 1: **직접 녹음** (강력 추천!)
```
1. 스마트폰 녹음 앱 사용
2. 조용한 방에서 녹음
3. 자연스럽게, 손녀에게 말하듯이
4. 따뜻하고 차분한 톤
5. 여러 번 녹음해서 가장 좋은 것 선택
```

Option 2: **TTS 사용**
```
- ElevenLabs (가장 자연스러움, 월 10,000자 무료)
  https://elevenlabs.io
- Google Cloud TTS (무료 티어)
```

**저장 위치**:
```
local_files/anime-pipeline/audio/voice/
├── narration_scene_001.mp3
├── narration_scene_002.mp3
└── ...
```

---

### 5️⃣ BGM 선곡

**BGM 컨셉**: 따뜻한 가족 다큐멘터리

**추천 사이트**:

1. **Pixabay Music** (무료, 추천)
   ```
   https://pixabay.com/music/
   검색: "warm piano family", "gentle acoustic"
   ```

2. **YouTube Audio Library**
   ```
   https://studio.youtube.com/channel/audio
   필터: Genre - Ambient/Acoustic
   ```

3. **Incompetech**
   ```
   https://incompetech.com/music/
   검색: "emotional", "family"
   ```

**선곡 기준**:
```
✓ 따뜻한 피아노 또는 어쿠스틱 기타
✓ 템포가 느리거나 중간
✓ 감정적이지만 과하지 않게
✓ 대사를 방해하지 않는 잔잔한 곡
✓ 10분 이상 길이 (또는 루프 가능)
```

**추천 트랙 (Pixabay)**:
```
- "Peaceful Piano"
- "Warm Acoustic Guitar"
- "Family Moments"
- "Gentle Memories"
```

**저장 위치**:
```
local_files/anime-pipeline/audio/bgm/
└── main_bgm.mp3
```

---

## 📋 작업 순서 요약

```
Week 1: 이미지 생성
  Day 1: 혜완이 캐릭터 이미지 (여러 각도)
  Day 2: 할아버지, 할머니 캐릭터 이미지
  Day 3: 기타 캐릭터 이미지
  Day 4-5: 주요 배경 이미지 생성
  Day 6: Whisk 테스트 (샘플 장면)
  Day 7: 이미지 정리 및 검수

Week 2: 오디오 준비 + Whisk 시작
  Day 1-2: 나레이션 녹음
  Day 3: BGM 선곡
  Day 4-7: Whisk 장면 1-20 제작

Week 3: Whisk 계속
  Day 1-7: Whisk 장면 21-50 제작

Week 4: 편집 및 마무리
  Day 1-2: 비디오 편집
  Day 3: 색보정
  Day 4: 오디오 믹싱
  Day 5: 최종 렌더링
  Day 6-7: QA 및 수정
```

---

## 🛠️ 필요한 도구 설치

### 이미지 생성
- [ ] Midjourney 계정 (또는 Leonardo.ai)
- [ ] Discord (Midjourney 사용 시)

### 영상 제작
- [ ] Google One AI Premium 구독 (Whisk)
- [ ] Google 계정

### 오디오
- [ ] 스마트폰 녹음 앱 (직접 녹음 시)
- [ ] ElevenLabs 계정 (TTS 사용 시)

### 편집
- [ ] DaVinci Resolve 설치 (무료)
  ```
  https://www.blackmagicdesign.com/products/davinciresolve
  ```
- [ ] FFmpeg 설치 (대안)
  ```
  Windows: https://www.ffmpeg.org/download.html
  ```

---

## 📞 질문이 있다면?

각 단계별로 막히는 부분이 있으면:

1. **PRODUCTION_STYLE_GUIDE.md** 참고
2. **PROJECT_OVERVIEW.md** 참고
3. **hyewan_milyang_script.json** 에서 해당 장면 확인

---

## ✅ 시작 전 체크리스트

- [ ] 모든 문서를 읽었습니다
- [ ] 실사 스타일 가이드를 이해했습니다
- [ ] 이미지 생성 도구를 선택했습니다
- [ ] Google Whisk 계정이 있습니다
- [ ] 나레이션 녹음 방법을 결정했습니다
- [ ] 작업 일정을 확인했습니다

---

## 🚀 시작하기!

**지금 바로 시작할 수 있는 것**:

1. **Midjourney 또는 Leonardo.ai 계정 만들기**
2. **혜완이 첫 번째 이미지 생성해보기**
3. **BGM 찾아보기 (Pixabay Music)**
4. **나레이션 스크립트 읽어보기**

---

**준비되셨나요?**

첫 번째 작업으로 **혜완이 캐릭터 이미지**를 생성해봅시다! 🎨

---

Made with 💝 for Hyewan's memory
