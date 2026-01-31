# 🎬 Whisk 첫 테스트 가이드

## 테스트 장면: 장면 6번
**"혜완이 현관에서 신발 벗으며 뛰어 들어옴"**

---

## 🎯 테스트 목표

1. Whisk가 실제 사진과 잘 작동하는지 확인
2. 실사 스타일 애니메이션 품질 확인
3. 8초 영상 생성 프로세스 익히기

---

## 📝 준비물

✅ 혜완이 사진: `local_files/anime-pipeline/characters/hyewan_original.jpg`
✅ Whisk 계정: Google One AI Premium
✅ 인터넷 연결

---

## 🚀 Step-by-Step 가이드

### Step 1: Whisk 접속

```
https://labs.google/fx/tools/whisk
```

- Google 계정으로 로그인
- Whisk 메인 화면 확인

---

### Step 2: Subject (주인공) 업로드

**Whisk 화면 왼쪽 "Subject" 영역**:

1. **"Upload image"** 클릭
2. 혜완이 사진 선택:
   ```
   local_files/anime-pipeline/characters/hyewan_original.jpg
   ```
3. 업로드 완료 대기

**또는 프롬프트 입력** (이미지 없이 테스트):
```
photorealistic Korean child, young girl,
striped shirt, natural cheerful expression,
full body shot, white background
```

---

### Step 3: Scene (배경) 설정

**Whisk 화면 중앙 "Scene" 영역**:

**옵션 A: 밀양 집 사진 사용** (추천!)
1. **"Upload image"** 클릭
2. 밀양 집 외관 사진 선택:
   ```
   local_files/01-외부_01[1].jpg
   ```

**옵션 B: 프롬프트 입력**
```
photorealistic Korean house entrance interior,
genkan style entryway, door and doorway,
natural lighting, warm welcoming atmosphere,
detailed interior, 8K quality
```

---

### Step 4: Style (스타일) 설정

**Whisk 화면 오른쪽 "Style" 영역**:

**프롬프트 입력**:
```
warm family documentary style,
natural lighting, film grain,
cinematic photography,
photorealistic, 8K quality
```

**또는 스타일 이미지 업로드**:
- 따뜻한 가족 사진 느낌의 레퍼런스 이미지
- 영화 스틸컷 같은 이미지

---

### Step 5: Create 이미지 생성

1. **"Create"** 버튼 클릭
2. 생성 대기 (1-2분)
3. 결과 이미지 확인

**체크포인트**:
- [ ] 혜완이가 잘 나왔나요?
- [ ] 실사처럼 보이나요?
- [ ] 배경이 자연스러운가요?

**만족스럽지 않으면**:
- "Remix" 또는 다시 Create
- Subject/Scene/Style 조정

---

### Step 6: ANIMATE 클릭 (핵심!)

생성된 이미지 아래:

1. **"ANIMATE"** 버튼 클릭
2. 애니메이션 프롬프트 입력 창 열림

---

### Step 7: 애니메이션 프롬프트 입력

**장면 6번 애니메이션 프롬프트**:

```
child running excitedly into house entrance,
natural energetic movement,
realistic running motion,
shoes being removed,
joyful expression,
natural child behavior,
smooth camera following motion
```

**또는 한글로**:
```
아이가 신나게 집 입구로 뛰어 들어가는 모습,
자연스러운 활발한 움직임,
사실적인 달리기 동작,
신발 벗는 모습,
기쁜 표정,
자연스러운 아이 행동,
부드러운 카메라 팔로우
```

---

### Step 8: 영상 생성

1. **"Generate"** 또는 생성 버튼 클릭
2. **8초 영상 생성 대기** (2-5분)
3. 생성 완료!

---

### Step 9: 결과 확인 및 다운로드

**체크리스트**:
- [ ] 8초 길이인가요?
- [ ] 움직임이 자연스러운가요?
- [ ] 실사 같은 품질인가요?
- [ ] 혜완이가 잘 인식되었나요?

**만족스러우면**:
1. **다운로드** 버튼 클릭
2. 파일명: `scene_006_test.mp4`
3. 저장 위치: `local_files/anime-pipeline/scenes/clips/`

---

## ✅ 성공 기준

### 좋은 결과:
✓ 실사처럼 자연스러운 움직임
✓ 혜완이의 특징이 유지됨
✓ 8초 동안 부드러운 애니메이션
✓ 배경과 캐릭터가 잘 합성됨

### 개선 필요:
❌ 움직임이 부자연스러움
❌ 얼굴이 많이 변형됨
❌ 애니메이션이 끊김
❌ 배경과 캐릭터가 이질적

---

## 🔧 문제 해결

### 문제: 혜완이가 너무 많이 변형됨
**해결**: Subject 이미지를 더 명확한 것으로 교체

### 문제: 움직임이 부자연스러움
**해결**: 애니메이션 프롬프트를 더 구체적으로
```
예: "slow natural walking" → "realistic walking gait, natural footsteps"
```

### 문제: 배경과 캐릭터가 안 맞음
**해결**: Scene 이미지를 더 단순한 배경으로 변경

### 문제: 애니메이션이 생성 안 됨
**해결**:
- 프롬프트를 더 짧고 간단하게
- "움직임" 중심으로 단순화

---

## 📊 테스트 결과 기록

### 생성 정보:
```
날짜: [    ]
장면 번호: 6
Subject: 혜완이 실제 사진
Scene: 밀양 집 / 프롬프트
Style: 가족 다큐 스타일
소요 시간: [    ]분
```

### 품질 평가 (1-5):
```
실사 품질: [ / 5]
움직임 자연스러움: [ / 5]
캐릭터 일관성: [ / 5]
전체 만족도: [ / 5]
```

### 메모:
```
좋았던 점:


개선할 점:


다음 시도 시 변경사항:

```

---

## 🎯 다음 단계

### 테스트 성공 시:
1. ✅ 다른 간단한 장면 1-2개 더 테스트
2. ✅ 본격적으로 50개 장면 제작 시작
3. ✅ 제작 일정 수립

### 테스트 개선 필요 시:
1. 프롬프트 조정 후 재시도
2. 다른 장면으로 테스트 (더 단순한 것)
3. Whisk 설정 최적화

---

## 💡 추가 테스트 추천 장면

### 쉬운 장면 (움직임 적음):
- **장면 10**: 키보드 클로즈업 (손만 움직임)
- **장면 37**: 혜완이 졸린 표정 (얼굴 클로즈업)

### 중간 난이도:
- **장면 12**: 할아버지와 나란히 앉음
- **장면 30**: 공원에서 뛰어다님

---

## 🚀 준비되셨나요?

**지금 바로**:
1. Whisk 열기: https://labs.google/fx/tools/whisk
2. 혜완이 사진 준비
3. 위 가이드 따라하기

**5분 후면 첫 8초 영상이 완성됩니다!** 🎬✨

---

**테스트 시작하고 결과 알려주세요!**
