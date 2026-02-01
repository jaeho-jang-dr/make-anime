# Google Flow 완벽 사용 가이드

> 출처: Tom's Guide - How to use Google Flow

---

## Google Flow란?

Google Flow는 **영화 제작자를 위한 AI 비디오 생성기**입니다. 텍스트 프롬프트와 이미지를 결합하여 **대화와 음악이 포함된 일관되고 사실적인 영상**을 만들 수 있습니다.

---

## 접속 방법

**URL**: https://labs.google/flow/

1. 위 링크 접속
2. **"Create with Flow"** 클릭

---

## 핵심 기능 4가지

### 1. Text to Video (텍스트 → 비디오)
- 텍스트 프롬프트로 영상 생성
- **음향 효과, 배경 소음, 대사** 지원
- Veo 3 모델에서 음성(Speech) 사용 가능

### 2. Frames to Video (프레임 → 비디오)
- 시작 이미지와 끝 이미지 업로드
- 두 프레임 사이의 **전환 영상** 자동 생성
- 이미지 기반 애니메이션에 적합

### 3. Ingredients to Video (재료 → 비디오)
- 개별 요소들을 조합해서 장면 생성
- **AI Ultra 구독자 전용** ($249/월)
- 캐릭터, 배경 등을 별도로 생성 후 결합

### 4. Camera Controls (카메라 컨트롤)
- 카메라 움직임 선택 가능:
  - Dolly in (줌 인)
  - Pan left/right (좌/우 패닝)
  - Tilt up/down (상/하 틸트)
  - 기타 시네마틱 기법

---

## 모델 선택

| 모델 | 특징 | 크레딧 사용 |
|------|------|-------------|
| **Veo 3 – Fast** | 빠른 생성 | 표준 |
| **Veo 3 – Quality** | 고품질 | 5배 |

---

## 단계별 사용법

### Phase 1: 초기 설정
```
1. Flow 실행 → "New Project" 선택
2. 우측 상단 설정 아이콘 클릭
3. 드롭다운에서 원하는 모델 선택
```

### Phase 2: 비디오 생성
```
4. 상세한 프롬프트 작성 (비주얼, 오디오, 효과 포함)
5. 화살표 클릭하여 생성 (몇 분 소요)
6. 생성된 2개의 8초 비디오 중 선택
```

### Phase 3: 영화 만들기
```
7. 원하는 비디오에 마우스 올려 "Add to scene" 클릭
8. 타임라인에서 클립 확인 및 전체 시퀀스 재생
9. 새 프롬프트로 추가 장면 계속 생성
```

### Phase 4: 고급 편집
```
10. "Extend" - 기존 샷을 매끄럽게 연장
    → 다음에 일어날 일을 설명하면 이어서 생성

11. "Jump to" - 장면 전환
    → 이전 프레임의 컨텍스트 유지하면서 전환

12. "Arrange" 모드 - 클립 순서 재배열
    → 드래그 앤 드롭으로 순서 변경

13. 프레임 길이 조절
    → 프레임 클릭 후 핸들 드래그
```

### Phase 5: 내보내기
```
14. 완성된 비디오 다운로드:
    - GIF 형식
    - 원본 720p
    - 업스케일 1080p
```

---

## 베스트 프랙티스

### 프롬프트 작성 팁
- **구체적으로**: 비주얼, 음향 효과, 배경 소음, 대사 모두 포함
- **카메라 동작 명시**: "camera slowly pans left", "gentle zoom in"
- **분위기 설명**: "warm lighting", "nostalgic atmosphere"
- **스타일 지정**: "Studio Ghibli anime style", "cinematic"

### 워크플로우 팁
- **인내심**: Quality 모드는 특히 시간이 더 걸림
- **프레임 정밀 조정**: 핸들 드래그로 원하는 부분만 사용
- **실험**: 프롬프트 엔지니어링에 시간 투자 필요

---

## 제한사항

| 제한 | 설명 |
|------|------|
| Speech | Text to Video + Veo 3에서만 사용 가능 |
| Ingredients | AI Ultra 구독자 전용 ($249/월) |
| Scene Builder | 종료 시 리셋됨 (저장 기능 개발 중) |
| 생성 시간 | Fast 모드도 몇 분 소요 |
| 호환성 | 기능별로 호환되는 모델 자동 선택됨 |

---

## 혜완이 영상 제작 워크플로우

### 1단계: 씬 1 제작 (scene_001.jpeg)
```
1. Flow 접속 → New Project
2. Frames to Video 선택
3. scene_001.jpeg 업로드
4. 프롬프트 입력:
   "Studio Ghibli anime style. Family at train station,
   summer morning, warm sunlight. Camera slowly pans
   across the station. Gentle breeze, birds in sky."
5. Generate → 8초 클립 생성
6. "Add to scene" 클릭
```

### 2단계: Extend로 확장
```
7. 생성된 클립 선택
8. "Extend" 클릭
9. 다음 프롬프트 입력:
   "Boy looks excitedly at arriving train,
   parents smile beside him"
10. Generate → 연장된 클립 생성
11. 반복하여 ~60초까지 확장
```

### 3단계: 씬 2-4 반복
```
12. 각 씬 이미지로 동일 과정 반복
13. 모든 클립을 타임라인에 추가
```

### 4단계: 최종 편집
```
14. Arrange 모드로 순서 정리
15. 각 클립 길이 조절
16. 전체 재생하여 확인
17. 1080p로 다운로드
```

---

## 파일 위치 참고

```
D:\Projects\make-anime\
├── scenes\
│   ├── scene_001.jpeg  ← Flow에 업로드
│   ├── scene_002.png   ← Flow에 업로드
│   ├── scene_003.jpeg  ← Flow에 업로드
│   └── scene_004.png   ← Flow에 업로드
├── scripts\
│   ├── GOOGLE_FLOW_GUIDE.md (이 파일)
│   └── HYEWAN_FLOW_4MIN_GUIDE.md (상세 프롬프트)
└── videos\
    └── flow_clips\     ← 다운로드 저장 위치
```

---

*마지막 업데이트: 2026-02-01*
