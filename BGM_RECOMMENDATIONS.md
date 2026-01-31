# 🎵 혜완이의 밀양 일주일 - BGM 추천

## 선정 기준

```yaml
분위기: 따뜻하고 감성적인 가족 다큐멘터리
스타일: 피아노 중심, 어쿠스틱
템포: 느리거나 중간 (70-90 BPM)
길이: 10분 이상 (또는 루프 가능)
라이선스: 완전 무료, 상업적 사용 가능
```

---

## 🎹 추천 BGM (우선순위 순)

### 1위 추천: "Emotional Piano" by Keys of Moon

**Pixabay Music**
```
제목: Emotional Piano
아티스트: Keys of Moon Music
길이: 3:35 (루프 가능)
스타일: 따뜻한 피아노, 감성적
분위기: 가족, 추억, 따뜻함
라이선스: Pixabay License (완전 무료)
```

**다운로드**:
```
https://pixabay.com/music/search/emotional%20piano%20family/
검색: "emotional piano family"
또는: "warm piano documentary"
```

**사용 이유**:
- 따뜻하고 감성적인 피아노
- 가족 다큐에 완벽한 분위기
- 루프해도 자연스러움
- 대사를 방해하지 않는 볼륨

---

### 2위 추천: "Memories" by Neutrin05

**Pixabay Music**
```
제목: Memories (또는 비슷한 제목)
스타일: 피아노 + 스트링
길이: 4-5분
분위기: 추억, 향수, 따뜻함
라이선스: 완전 무료
```

**다운로드**:
```
https://pixabay.com/music/search/memories%20piano/
검색: "memories piano"
```

---

### 3위 추천: "Family Time" 스타일 트랙

**YouTube Audio Library**
```
장르: Ambient / Cinematic
분위기: Calm, Happy, Bright
악기: Piano, Acoustic Guitar
```

**다운로드**:
```
https://studio.youtube.com/channel/audio
필터:
- Genre: Ambient
- Mood: Calm, Happy
- Instrument: Piano
```

---

## 📥 다운로드 및 설치 가이드

### Pixabay Music (최고 추천!)

#### Step 1: 사이트 접속
```
https://pixabay.com/music/
```

#### Step 2: 검색
```
검색어 추천:
- "emotional piano family"
- "warm acoustic family"
- "gentle piano memories"
- "family documentary"
```

#### Step 3: 필터 설정
```
- Length: Long (10분 이상 또는 루프 가능한 3-5분)
- Mood: Calm, Emotional, Happy
- Instruments: Piano, Acoustic Guitar
```

#### Step 4: 듣고 선택
```
여러 트랙 들어보고:
- 대사 방해 안 하는 것
- 너무 슬프지 않은 것
- 따뜻하고 희망적인 느낌
```

#### Step 5: 다운로드
```
1. 트랙 클릭
2. "Free Download" 버튼
3. MP3 다운로드
4. 저장 위치: local_files/anime-pipeline/audio/bgm/
5. 파일명: main_bgm.mp3
```

---

## 🎼 구체적 추천 트랙 (2024-2025)

### Pixabay에서 찾을 수 있는 트랙:

#### 1. "Beautiful Emotional Piano" by Keys of Moon
```
- 길이: 3:35
- 템포: Slow
- 완벽한 가족 다큐 분위기
- 루프 3번 = 10분 이상
```

#### 2. "Gentle Thoughts" by Ashot-Danielyan-Composer
```
- 길이: 2:30
- 스타일: 부드러운 피아노
- 루프 4번 = 10분
```

#### 3. "Warm Memories" by Lexin_Music
```
- 길이: 4:08
- 피아노 + 스트링
- 감성적이지만 과하지 않음
```

#### 4. "Family Moments" (여러 아티스트)
```
- 검색: "family piano"
- 따뜻한 가족 분위기 트랙 다수
```

---

## 🎵 대체 음원 사이트

### 1. YouTube Audio Library
```
URL: https://studio.youtube.com/channel/audio
장점: 유튜브 공식, 안전
필터: Genre > Ambient, Cinematic
추천 트랙: "Piano Moment", "Acoustic Breeze"
```

### 2. Incompetech
```
URL: https://incompetech.com/music/
검색: "Emotional" 또는 "Peaceful"
라이선스: CC BY (크레딧 표시만 하면 무료)
추천: "Wallpaper", "Clean Soul"
```

### 3. Free Music Archive
```
URL: https://freemusicarchive.org
필터: CC0 (완전 퍼블릭 도메인)
장르: Ambient, Soundtrack
```

---

## 💾 저장 및 사용 방법

### 다운로드 후:

```bash
# 저장 위치
local_files/anime-pipeline/audio/bgm/main_bgm.mp3

# 파일명 규칙
main_bgm.mp3 (메인 배경음악)
opening_music.mp3 (오프닝용, 선택)
ending_music.mp3 (엔딩용, 선택)
```

### 렌더링 시 사용:

```bash
python main_pipeline.py --mode render --bgm audio/bgm/main_bgm.mp3
```

---

## 🎚️ 음량 조정 팁

### FFmpeg로 BGM 볼륨 조정:

```bash
# BGM 볼륨 낮추기 (대사가 잘 들리도록)
ffmpeg -i main_bgm.mp3 -filter:a "volume=0.3" main_bgm_low.mp3
```

**권장 볼륨**:
- 나레이션 있는 부분: 30% (0.3)
- 나레이션 없는 부분: 50% (0.5)

---

## 📝 크레딧 표기 (필요시)

### Pixabay 음악 사용 시:
```
크레딧 표기 불필요!
완전 무료, 상업적 사용 가능
```

### YouTube Audio Library:
```
일부 트랙: "Music by [아티스트명]"
대부분: 크레딧 불필요
```

### Incompetech (CC BY):
```
"Music by Kevin MacLeod (incompetech.com)"
"Licensed under CC BY 4.0"
```

---

## ✅ 최종 추천 워크플로우

### 빠른 선택 (5분):

1. **Pixabay 접속**
   ```
   https://pixabay.com/music/
   ```

2. **검색**
   ```
   "emotional piano family"
   ```

3. **상위 3-5개 트랙 들어보기**
   ```
   - 가장 따뜻한 느낌
   - 대사 방해 안 함
   - 루프 가능
   ```

4. **다운로드**
   ```
   Free Download → main_bgm.mp3
   ```

5. **저장**
   ```
   local_files/anime-pipeline/audio/bgm/
   ```

---

## 🎯 제가 추천하는 TOP 1

**Pixabay: "Emotional Piano" 카테고리의 상위 트랙**

이유:
- ✅ 가족 다큐에 완벽한 따뜻한 분위기
- ✅ 피아노 중심, 대사 방해 안 함
- ✅ 감정적이지만 과하지 않음
- ✅ 루프해도 자연스러움
- ✅ 완전 무료, 크레딧 불필요

---

## 🚀 다음 단계

BGM 다운로드 후:

1. **audio/bgm 폴더에 저장**
2. **간단히 재생해서 확인**
3. **나중에 렌더링 시 자동으로 삽입됨**

---

**지금 바로 Pixabay에서 "emotional piano family" 검색해보세요!**

마음에 드는 트랙 찾으시면 알려주세요! 🎵✨
