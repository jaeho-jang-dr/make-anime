# 🎬 애니메이션 제작 워크플로우 가이드

## 전체 프로세스 개요

```
[스토리 스크립트] → [Whisk 이미지 생성] → [Google Vids 영상 편집] → [최종 출력]
```

**예상 소요 시간**: 4-6시간
**최종 길이**: 10분 (600초)
**총 장면 수**: 30개

---

## 📌 1단계: Google Whisk로 장면 이미지 생성

### 접속
🔗 https://labs.google/fx/tools/whisk

### 기본 설정
1. Google 계정 로그인
2. 스타일 이미지 준비 (Ghibli 스타일 레퍼런스)

### 작업 순서

#### 1-1. 캐릭터 Subject 이미지 생성 (먼저!)

**루나 (Luna) - 주인공**
```
Subject: (빈 칸 또는 기본 애니메이션 소녀 이미지)
Scene: simple white background
Style: Ghibli anime style, Studio Ghibli character design

프롬프트 수정:
"anime girl, 16 years old, silver-white long flowing hair, deep ocean blue eyes,
pale porcelain skin, wearing midnight blue dress with silver star embroidery,
gentle expression, Ghibli style character design, full body"
```
→ **저장**: `characters/luna_subject.png`

**스텔라 (Stella) - 별의 정령**
```
Subject: (빈 칸)
Scene: simple dark background
Style: ethereal glowing style

프롬프트 수정:
"ethereal spirit child, glowing translucent golden body, star-shaped sparkling eyes,
hair made of flowing light particles, luminescent aura, anime style, magical being"
```
→ **저장**: `characters/stella_subject.png`

**할아버지 (Grandfather)**
```
Subject: (빈 칸)
Scene: simple warm background
Style: Ghibli anime style

프롬프트 수정:
"elderly Korean man, 75 years old, gentle white beard, warm caring eyes,
wearing traditional blue hanbok, wise expression, Ghibli style character"
```
→ **저장**: `characters/grandfather_subject.png`

---

#### 1-2. 장면별 이미지 생성

| 장면 | Subject | Scene 프롬프트 | Style |
|------|---------|---------------|-------|
| 001 | 빈 하늘 | traditional Korean village at night, no stars visible, only darkness above, dim lantern lights | Ghibli watercolor |
| 002 | luna_subject.png | cozy bedroom interior, Korean style, girl sitting by window looking at dark sky, candlelight | Ghibli warm interior |
| 003 | luna + grandfather | warm living room with ondol floor, fireplace glowing, old star maps on wall | Ghibli nostalgic |
| 004 | luna_subject.png | same living room, girl standing with determined expression, moonlight through window | Ghibli dramatic |
| 005 | luna_subject.png | village gate at night, walking towards dark forest, lantern in hand | Ghibli adventure |

*(전체 30개 장면은 anime_production_script.json 참조)*

### 이미지 저장 규칙
- 파일명: `scene_001.png`, `scene_002.png`, ...
- 저장 위치: `d:\Projects\make-anime\images\scenes\`
- 해상도: 가능한 최대 (1920x1080 권장)

---

## 📌 2단계: Google Vids로 영상 제작

### 접속
🔗 https://vids.google.com

### 2-1. 새 프로젝트 생성

1. **+ Create** 클릭
2. **Blank video** 선택
3. 프로젝트명: "별을 삼킨 소녀"
4. 화면비: **16:9** (유튜브용)

### 2-2. 장면 추가 (스토리보드 모드)

각 장면별로:

1. **+ Add scene** 클릭
2. **Upload media** → 해당 scene_XXX.png 업로드
3. **Duration** 설정 (스크립트의 duration_seconds 참조)
4. **Transition** 설정 (dissolve, fade, cut 등)

### 장면별 설정 표

| 장면 | 이미지 | 길이 | 전환효과 | 나레이션 |
|------|--------|------|----------|----------|
| 001 | scene_001.png | 20초 | fade_in | "옛날 옛적, 하늘의 별들이..." |
| 002 | scene_002.png | 15초 | dissolve | "마을에 사는 소녀 루나는..." |
| 003 | scene_003.png | 25초 | dissolve | "\"별들은 사라진 게 아니란다...\"" |
| 004 | scene_004.png | 15초 | cut | "루나는 그 순간 결심했습니다..." |
| 005 | scene_005.png | 20초 | dissolve | "작은 등불 하나를 들고..." |
| ... | ... | ... | ... | ... |

### 2-3. 나레이션 추가

**옵션 A: AI 음성 (Google Vids 내장)**
1. 장면 선택
2. **Add voiceover** 클릭
3. 텍스트 입력 (한국어 지원)
4. 음성 스타일 선택

**옵션 B: 직접 녹음**
1. **Upload audio** → 녹음 파일 업로드
2. 타이밍 조정

### 2-4. 배경음악 추가

1. **Audio** 탭 클릭
2. **Add music** 선택
3. Google Vids 라이브러리에서 선택 또는 업로드
4. 볼륨 조정 (나레이션 시 -10dB)

**추천 BGM 구간**:
- 00:00-02:00: 신비로운 피아노 (미스터리)
- 02:00-04:00: 모험 테마 (여정)
- 04:00-06:00: 긴장감 있는 오케스트라 (동굴)
- 06:00-08:00: 감동적인 피아노 (클라이맥스)
- 08:00-10:00: 따뜻한 엔딩 테마

### 2-5. 전환 효과 & 애니메이션

**Ken Burns 효과 (이미지에 움직임 추가)**:
- 장면 선택 → **Animate** 클릭
- Pan: 좌→우, 상→하
- Zoom: In/Out
- Duration: 장면 길이와 맞춤

**권장 설정**:
| 장면 유형 | 애니메이션 |
|-----------|-----------|
| 풍경 | Slow pan left/right |
| 클로즈업 | Subtle zoom in |
| 액션 | Quick pan + zoom |
| 감정 | Slow zoom in |

### 2-6. 자막 추가 (선택사항)

1. **Captions** 탭
2. **Add captions** → 수동 입력 또는 자동 생성
3. 스타일 설정 (폰트, 크기, 위치)

---

## 📌 3단계: 최종 출력

### Google Vids에서 내보내기

1. **Share** 버튼 클릭
2. **Download** 선택
3. 품질: **1080p** (Full HD)
4. 형식: **MP4**

### 출력 파일
- 파일명: `별을_삼킨_소녀_final.mp4`
- 저장 위치: `d:\Projects\make-anime\output\`

---

## 📋 체크리스트

### Whisk 이미지 생성
- [ ] 캐릭터 Subject 이미지 3개 생성
- [ ] 장면 001-010 이미지 생성 (Act 1-2 시작)
- [ ] 장면 011-020 이미지 생성 (Act 2-3)
- [ ] 장면 021-030 이미지 생성 (Act 3-4)
- [ ] 모든 이미지 다운로드 및 정리

### Google Vids 편집
- [ ] 프로젝트 생성
- [ ] 30개 장면 이미지 업로드
- [ ] 각 장면 길이 설정
- [ ] 전환 효과 적용
- [ ] 나레이션 추가
- [ ] 배경음악 추가
- [ ] Ken Burns 애니메이션 적용
- [ ] 전체 미리보기
- [ ] 최종 출력

---

## 💡 팁 & 트러블슈팅

### Whisk 팁
- **캐릭터 일관성**: 같은 Subject 이미지를 모든 장면에 사용
- **스타일 통일**: Style 슬롯에 동일한 레퍼런스 사용
- **배치 작업**: 비슷한 배경의 장면들을 연속으로 생성

### Google Vids 팁
- **장면 순서**: 드래그로 쉽게 재배치 가능
- **타이밍 조정**: 나레이션 길이에 맞춰 장면 길이 조정
- **미리보기**: 자주 미리보기로 흐름 확인

### 일반적인 문제
| 문제 | 해결책 |
|------|--------|
| 캐릭터가 달라 보임 | 같은 Subject 이미지 재사용 |
| 장면 연결이 어색함 | 전환 효과를 dissolve로 통일 |
| 나레이션 타이밍 안 맞음 | 장면 길이 조정 또는 나레이션 속도 변경 |
| 영상이 지루함 | Ken Burns 효과 추가, 전환 다양화 |

---

## 🔗 필요 링크

- **Whisk**: https://labs.google/fx/tools/whisk
- **Google Vids**: https://vids.google.com
- **무료 BGM**: https://pixabay.com/music/
- **무료 효과음**: https://freesound.org

---

*Made with Whisk + Google Vids*
