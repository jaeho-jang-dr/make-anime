# 🎥 제작 스타일 가이드 - 실사 기반 영상 제작

## 📌 핵심 제작 방침

**본 프로젝트는 만화/애니메이션 스타일을 지양하고, 실사(Photorealistic) 스타일을 채택합니다.**

### 스타일 방향성

```yaml
스타일: 실사/포토리얼리스틱 (Photorealistic / Live-action style)
목표: 애니메이션보다 높은 동작 완성도와 자연스러운 움직임
접근: AI 생성 실사 영상 + 자연스러운 모션
품질 우선순위: 움직임의 사실감 > 과장된 연출
```

---

## 🎯 실사 스타일 vs 애니메이션 스타일

### ❌ 지양할 것 (애니메이션 스타일)

```
- 만화/애니메이션 캐릭터 디자인
- 과장된 표정/동작
- 셀 음영 (cel shading)
- 비현실적인 색상 팔레트
- 만화적 연출 기법
- 애니메이션 특유의 프레임 제한
```

### ✅ 추구할 것 (실사 스타일)

```
- 사실적인 인물/배경
- 자연스러운 움직임과 표정
- 실제 조명과 물리 법칙
- 현실적인 색감과 질감
- 영화적 촬영 기법
- 부드러운 프레임 (24fps 풀 모션)
```

---

## 🎬 실사 스타일 제작 원칙

### 1. 비주얼 스타일

#### 1.1 캐릭터 디자인

**실사 인물 접근법**:
```
✓ 실제 사람처럼 보이는 얼굴과 체형
✓ 자연스러운 피부 텍스처와 질감
✓ 현실적인 헤어스타일과 의상
✓ 사실적인 조명과 그림자
✓ 미묘한 표정 변화
```

**프롬프트 예시 (실사 스타일)**:
```
photorealistic portrait, cinematic quality,
young woman, 25 years old, natural appearance,
long flowing brown hair, realistic skin texture,
wearing modern dark blue coat with subtle details,
holding realistic LED lantern,
natural lighting, soft shadows,
shallow depth of field,
professional photography quality,
8K resolution, detailed facial features
```

**피해야 할 키워드**:
```
❌ anime, manga, cartoon, illustrated
❌ cel shaded, 2D art style
❌ Makoto Shinkai style, Studio Ghibli
❌ vibrant colors (과도하게 선명한 색)
```

#### 1.2 배경/환경

**실사 환경 접근법**:
```
✓ 실제 장소처럼 보이는 배경
✓ 자연스러운 조명 (자연광/인공광)
✓ 현실적인 날씨 효과
✓ 사실적인 질감 (돌, 나무, 금속 등)
✓ 물리적으로 정확한 공간
```

**배경 프롬프트 예시**:
```
photorealistic medieval village at night,
cinematic photography, realistic architecture,
natural moonlight, practical street lamps,
atmospheric fog, detailed stone textures,
professional cinematography, 8K quality,
shot on ARRI Alexa, film grain
```

#### 1.3 조명

**영화적 조명 설정**:
```
- 자연광: 실제 태양/달빛의 특성
- 인공광: 실제 램프/촛불/네온의 색온도
- 3점 조명: Key Light, Fill Light, Back Light
- 드라마틱한 명암 대비 (chiaroscuro)
- 골든 아워, 블루 아워 활용
```

**조명 키워드**:
```
- natural lighting, soft shadows
- cinematic lighting, dramatic contrast
- golden hour, blue hour
- volumetric lighting, god rays
- practical lights, motivated lighting
```

---

### 2. 모션/애니메이션

#### 2.1 동작 완성도 향상

**실사 스타일의 움직임 특징**:
```
✓ 자연스러운 걷기/달리기 (실제 인간의 보행)
✓ 미묘한 몸짓 (손동작, 고개 기울임)
✓ 자연스러운 눈 깜빡임
✓ 호흡에 따른 가슴/어깨 움직임
✓ 중력을 느끼게 하는 무게감
✓ 옷/머리카락의 물리적으로 정확한 움직임
```

**Whisk 애니메이션 프롬프트 (실사 스타일)**:
```
좋은 예:
✓ "natural walking motion, realistic gait, subtle body sway"
✓ "slow head turn with natural eye movement, realistic hair physics"
✓ "breathing naturally, chest rising and falling, wind in hair"
✓ "realistic hand gesture, natural finger movement"

피해야 할 예:
❌ "anime-style movement"
❌ "exaggerated motion"
❌ "bouncy animation"
```

#### 2.2 카메라워크 (영화 촬영 기법)

**영화적 카메라 움직임**:
```
- Dolly Shot: 부드러운 전진/후진
- Tracking Shot: 캐릭터를 따라가는 움직임
- Crane Shot: 상하 움직임
- Handheld: 미묘한 흔들림 (현장감)
- Steadicam: 안정적이면서 역동적
- Slider: 좌우 슬라이딩
```

**카메라 프롬프트**:
```
- "smooth dolly shot forward, cinematic camera movement"
- "handheld camera, slight natural shake, documentary style"
- "crane shot rising up, revealing environment"
- "tracking shot following character, shallow depth of field"
```

#### 2.3 프레임레이트 & 모션 블러

**설정**:
```
- 프레임레이트: 24fps (영화 표준)
- 셔터 스피드: 1/48s (자연스러운 모션 블러)
- 모션 블러: 활성화 (움직임의 부드러움)
```

---

### 3. 색상 & 그레이딩

#### 3.1 컬러 팔레트

**실사 영화 스타일 색감**:
```
✓ 자연스러운 색온도 (Warm/Cool balance)
✓ 미묘한 채도 (과도한 채도 지양)
✓ 영화적 색보정 (Color Grading)
✓ 실제 환경의 색상 반영
```

**색상 레퍼런스**:
```
- 블레이드 러너 2049: 따뜻한 오렌지 vs 차가운 블루
- 인터스텔라: 자연스러운 색감, 우주의 어두움
- 반지의 제왕: 판타지지만 사실적인 색감
- 매드 맥스: 강렬한 오렌지-블루 대비
```

#### 3.2 영화 등급별 룩 (Film Look)

**장르별 색보정**:
```
드라마:
- 자연스러운 피부톤
- 미묘한 contrast
- 약간 desaturated

액션/SF:
- Teal and Orange look
- 높은 contrast
- 냉색 계열 그림자

판타지:
- 따뜻한 골든 톤
- 부드러운 하이라이트
- 마법적 분위기 (빛의 강조)

공포/스릴러:
- 차가운 블루-그린 톤
- 어두운 그림자
- 높은 contrast
```

**색보정 키워드**:
```
- cinematic color grading
- teal and orange
- warm golden tones
- desaturated look
- film grain
- LUT (Look-Up Table) style
```

---

## 🛠️ 실사 스타일 제작 워크플로우

### Phase 1: 컨셉 & 스크립트

**실사 영상 기획**:
```
1. 장르 선택 (SF, 판타지, 드라마, 액션)
2. 영화적 레퍼런스 수집
   - 비슷한 장르의 영화 스틸컷
   - 색감/조명 레퍼런스
3. 실사 캐릭터 컨셉 아트
4. 로케이션/세트 레퍼런스
```

**스크립트 접근**:
```
- 애니메이션보다 느린 템포 (실사는 긴 호흡)
- 대사보다 표정/몸짓으로 전달
- 영화적 장면 구성
```

---

### Phase 2: 비주얼 에셋 생성 (실사)

#### 2.1 캐릭터 생성

**AI 도구 선택**:
```
- Midjourney: 고품질 포토리얼리즘
- Stable Diffusion (Realistic models)
- Leonardo.ai (PhotoReal 모드)
- Google Imagen 3 (실사 특화)
```

**프롬프트 템플릿**:
```
[Shot type] photorealistic portrait,
[Person description], [age], natural appearance,
[Hair], [Eyes], realistic skin texture,
[Clothing details],
natural lighting, soft shadows,
shot on [Camera model], [Lens],
shallow depth of field, bokeh,
professional photography, 8K quality,
film grain, cinematic
```

**예시**:
```
medium shot photorealistic portrait,
young woman, 28 years old, natural appearance,
long flowing brown hair with natural highlights,
hazel eyes with realistic iris details,
subtle makeup, realistic skin pores and texture,
wearing dark navy peacoat with wool texture,
holding vintage brass lantern with warm glow,
golden hour lighting, soft rim light,
shot on ARRI Alexa, 85mm lens,
shallow depth of field, creamy bokeh,
professional cinematography, 8K resolution,
slight film grain, cinematic look
```

#### 2.2 배경/환경 생성

**실사 배경 프롬프트**:
```
[Location type] photorealistic environment,
[Detailed description of place],
[Time of day], [Weather conditions],
[Lighting setup],
professional architectural photography,
8K resolution, ultra detailed,
shot on [Camera], [Lens],
film grain, cinematic
```

**예시 (판타지 마을)**:
```
medieval village street photorealistic environment,
cobblestone roads with realistic stone texture,
timber-framed buildings with aged wood,
warm amber light from practical lanterns,
atmospheric fog rolling through street,
nighttime, overcast sky with subtle moonlight,
moody cinematic lighting, practical light sources,
professional location photography,
8K ultra detailed, shot on RED Dragon,
35mm lens, film grain, dark fantasy aesthetic
```

---

### Phase 3: Whisk 실사 애니메이션

#### 3.1 Subject (캐릭터) 설정

**일관성 유지**:
```
1. 첫 장면에서 실사 캐릭터 이미지 생성
2. 모든 장면에서 동일한 이미지 재사용
3. 각도/표정 변화는 Animation prompt로 제어
```

**Subject 프롬프트 팁**:
```
- "photorealistic full body portrait" (전신)
- "photorealistic upper body portrait" (상반신)
- "photorealistic close-up portrait" (클로즈업)
- 배경은 neutral/white background
- 조명은 even lighting (그림자 최소화)
```

#### 3.2 Scene (배경) 설정

**실사 배경 입력**:
```
- 생성한 실사 배경 이미지 업로드
- 또는 Scene 프롬프트에 실사 키워드 사용
```

**Scene 프롬프트 예시**:
```
photorealistic medieval village at night,
cinematic environment, practical lighting,
fog and atmosphere, detailed architecture,
film quality, 8K
```

#### 3.3 Style (스타일) 설정

**영화적 스타일 레퍼런스**:
```
- 영화 스틸컷 사용
- 색보정 레퍼런스 (Teal & Orange 등)
- 조명 스타일 레퍼런스
```

**Style 프롬프트**:
```
cinematic film style reference,
teal and orange color grading,
dramatic lighting with soft shadows,
film grain texture,
professional cinematography aesthetic,
[영화명] movie color palette
```

#### 3.4 Animation (실사 모션)

**자연스러운 움직임 프롬프트**:

**걷기/이동**:
```
✓ "realistic walking motion, natural gait, subtle body sway,
   breathing movement, natural arm swing"
✓ "slow realistic walk forward, natural footsteps,
   clothing moving with physics"
```

**미묘한 동작**:
```
✓ "person standing still, subtle breathing,
   natural micro-movements, blinking eyes,
   wind gently moving hair"
✓ "slow head turn with natural eye movement,
   realistic facial micro-expressions"
```

**카메라 움직임 중심**:
```
✓ "smooth dolly shot moving forward,
   subject standing naturally,
   cinematic camera movement"
✓ "slow pan across scene from left to right,
   revealing environment, film-like motion"
```

**환경 효과**:
```
✓ "realistic fog slowly rolling,
   practical lights flickering naturally,
   leaves falling with realistic physics"
```

---

### Phase 4: 후반 작업 (Post-Production)

#### 4.1 색보정 (Color Grading)

**도구**:
```
- DaVinci Resolve (무료, 전문가급)
- Adobe Premiere Pro
- Final Cut Pro
```

**색보정 단계**:
```
1. 화이트 밸런스 조정
2. Exposure/Contrast 조정
3. 색온도 통일
4. 영화적 LUT 적용
   - Teal & Orange
   - Bleach Bypass
   - Film Emulation
5. Film Grain 추가 (미묘하게)
6. Vignette (선택적)
```

#### 4.2 모션 블러 & 프레임 보간

**부드러운 움직임 강화**:
```
- AI 프레임 보간 (Topaz Video AI, RIFE)
- 모션 블러 추가 (ReelSmart Motion Blur)
- 안정화 (필요시)
```

#### 4.3 사운드 디자인

**실사 영상의 사운드**:
```
✓ 자연스러운 환경음 (Ambient Sound)
✓ 사실적인 효과음 (Foley)
✓ 영화 같은 BGM (Orchestral, Cinematic)
✓ 적절한 다이나믹 레인지
```

**사운드 레이어**:
```
Layer 1: 대사/나레이션 (가장 명확)
Layer 2: Foley/효과음 (발소리, 옷 스치는 소리)
Layer 3: 환경음 (바람, 빗소리, 도시 소음)
Layer 4: BGM (배경, 볼륨 낮춤)
```

---

## 📐 기술 스펙 (실사 영상)

### 해상도 & 프레임레이트

```yaml
해상도:
  - 최소: 1920x1080 (Full HD)
  - 권장: 3840x2160 (4K)
  - 최상: 7680x4320 (8K, 다운샘플링)

종횡비:
  - 영화: 2.39:1 (Cinemascope)
  - 표준: 16:9 (1.78:1)
  - 드라마: 1.85:1

프레임레이트:
  - 24fps (영화 표준)
  - 30fps (TV 표준, 부드러움)
  - 60fps (액션/슬로우모션 소스)

비트레이트:
  - HD: 8-12 Mbps
  - 4K: 50-100 Mbps
  - 8K: 150-300 Mbps
```

### 코덱 & 포맷

```yaml
비디오 코덱:
  - H.264 (범용, 호환성 높음)
  - H.265/HEVC (고압축, 고품질)
  - ProRes (편집용, 무손실)

오디오 코덱:
  - AAC (일반)
  - Dolby Digital (영화)
  - Uncompressed PCM (편집용)

컨테이너:
  - MP4 (배포용)
  - MOV (편집/중간 파일)
  - MKV (고품질 아카이브)
```

---

## 🎨 실사 스타일 프롬프트 라이브러리

### 캐릭터 프롬프트 (실사)

**여성 주인공 (현대)**:
```
medium shot photorealistic portrait,
woman in her late 20s, natural beauty,
shoulder-length brown hair with subtle highlights,
expressive green eyes with realistic iris details,
minimal makeup, natural skin texture with subtle pores,
wearing casual dark blue denim jacket,
soft natural window lighting from left,
shot on Canon EOS R5, 50mm f/1.8 lens,
shallow depth of field, soft bokeh,
professional photography quality, 8K resolution,
slight film grain, neutral color grading
```

**남성 주인공 (판타지)**:
```
full body photorealistic portrait,
rugged man in his early 30s, warrior appearance,
short dark hair, stubble beard, intense gaze,
realistic skin texture, weathered face,
wearing detailed leather armor with metal accents,
holding realistic medieval sword,
dramatic side lighting, moody atmosphere,
shot on ARRI Alexa Mini, 35mm lens,
cinematic depth of field, dark fantasy aesthetic,
8K ultra detailed, film grain, desaturated color grading
```

**노인 캐릭터 (드라마)**:
```
close-up photorealistic portrait,
elderly man, 70s, wise expression,
white hair, deep wrinkles showing life experience,
realistic age spots and skin texture,
warm brown eyes with kindness,
wearing simple linen clothing,
soft diffused golden hour lighting,
shot on Sony A7S III, 85mm f/1.4 lens,
shallow depth of field, warm color grading,
professional cinematography, 8K quality
```

---

### 배경 프롬프트 (실사)

**도시 거리 (현대)**:
```
photorealistic urban street environment,
modern city at dusk, wet asphalt after rain,
neon signs reflecting on puddles,
realistic architectural details, glass and steel,
streetlights creating pools of warm light,
light traffic, few pedestrians in distance,
cinematic environmental lighting,
shot on RED Monstro, 24mm lens,
8K ultra detailed, film grain,
teal and orange color grading, blade runner aesthetic
```

**숲 속 (판타지)**:
```
photorealistic ancient forest environment,
massive old-growth trees with realistic bark texture,
dappled sunlight filtering through canopy,
volumetric god rays, atmospheric haze,
moss and ferns with detailed texture,
mystical but realistic atmosphere,
cinematic natural lighting,
shot on ARRI Alexa 65, 28mm lens,
8K ultra detailed, shallow depth of field,
warm green color grading, film grain
```

**우주선 내부 (SF)**:
```
photorealistic spaceship interior environment,
futuristic but functional design,
realistic metal panels with wear and tear,
practical lighting from LED strips and monitors,
control panels with detailed buttons and screens,
subtle steam/fog effects,
cinematic sci-fi aesthetic,
shot on RED Komodo, 18mm lens,
8K ultra detailed, cool blue color grading,
film grain, Interstellar movie style
```

---

### 애니메이션 프롬프트 (실사 모션)

**인물 동작**:
```
캐릭터 걷기:
"natural realistic walking motion, proper human gait cycle,
 subtle weight shift, arms swinging naturally,
 clothing physics, breathing movement visible"

서 있는 자세:
"person standing still with natural micro-movements,
 subtle breathing causing chest to rise and fall,
 occasional blinking, slight weight shifting,
 realistic idle animation"

대화 중:
"person talking with natural facial expressions,
 realistic lip movement, subtle head gestures,
 hand gestures while speaking,
 natural eye blinking and micro-expressions"

감정 표현:
"slow realization dawning on face,
 subtle eyebrow raise, eyes widening naturally,
 realistic emotional progression,
 micro-expressions changing gradually"
```

**카메라 워크**:
```
Dolly:
"smooth dolly shot moving forward steadily,
 cinematic camera movement, film-like motion,
 maintaining focus on subject, professional cinematography"

Tracking:
"smooth tracking shot following subject from side,
 steady camera keeping subject in frame,
 realistic handheld stability, cinema quality"

Crane:
"graceful crane shot rising upward,
 revealing environment as camera ascends,
 smooth cinematic movement, epic establishing shot"

Handheld:
"subtle handheld camera shake, documentary feel,
 realistic natural camera movement,
 slight bobbing, maintains framing"
```

**환경 효과**:
```
자연 효과:
"realistic wind blowing through trees,
 leaves rustling naturally, branches swaying,
 grass bending with wind physics"

날씨:
"natural rainfall, realistic water droplets,
 puddles forming, atmospheric fog,
 weather effects with proper physics"

조명:
"practical lights flickering naturally,
 candle flames dancing realistically,
 light and shadow playing on surfaces,
 realistic caustics and light scatter"
```

---

## 📊 제작 체크리스트 (실사 스타일)

### Pre-Production
- [ ] 영화적 레퍼런스 수집 (스틸컷, 색감)
- [ ] 실사 캐릭터 컨셉 확정
- [ ] 촬영 스타일 결정 (카메라, 조명)
- [ ] 색보정 방향 설정 (LUT 선택)
- [ ] 장면별 카메라워크 기획

### Production
- [ ] 실사 캐릭터 이미지 생성 (포토리얼)
- [ ] 실사 배경 이미지 생성
- [ ] 영화적 스타일 레퍼런스 준비
- [ ] Whisk에서 자연스러운 모션으로 애니메이션
- [ ] 모든 클립에 일관된 실사 톤 유지

### Post-Production
- [ ] 색보정 (LUT 적용, Teal & Orange 등)
- [ ] Film Grain 추가
- [ ] 모션 블러 확인/강화
- [ ] 사운드 디자인 (Foley, Ambient)
- [ ] 최종 마스터링 (영화 품질)

---

## 🎯 실사 스타일의 장점

**애니메이션 대비 실사의 강점**:
```
✓ 더 자연스럽고 사실적인 움직임
✓ 높은 몰입감 (현실감)
✓ 미묘한 감정 표현 가능
✓ 영화적 품질감
✓ 범용적인 수용성 (애니메이션 편견 없음)
✓ AI 생성 시 더 높은 품질 (현재 기술 수준)
```

**Whisk/AI 도구에서 실사의 이점**:
```
✓ 포토리얼 모델의 성능이 더 좋음
✓ 움직임 생성 시 물리 법칙 적용 용이
✓ 일관성 유지가 더 쉬움
✓ 레퍼런스 이미지가 풍부 (실제 사진/영화)
```

---

## 📚 추가 학습 리소스

### 영화 촬영 기법
- "Cinematography: Theory and Practice" (Blain Brown)
- "The Visual Story" (Bruce Block)
- YouTube: Every Frame a Painting
- YouTube: Indy Mogul

### 색보정
- DaVinci Resolve 공식 트레이닝
- "The Art and Technique of Digital Color Correction"
- YouTube: Casey Faris (DaVinci Tutorials)

### 실사 AI 생성
- Midjourney 포토리얼 프롬프트 가이드
- Stable Diffusion Realistic Checkpoints
- Leonardo.ai PhotoReal 문서

---

## 마무리

**이 프로젝트는 실사 스타일 AI 영상 제작을 지향합니다.**

- 애니메이션이 아닌 **영화 같은 품질**
- 자연스러운 **실제 사람 같은 움직임**
- 영화적 **색감과 조명**
- 전문적인 **시네마토그래피**

모든 제작 과정에서 "만화"가 아닌 "실사 영화"를 기준으로 삼으세요.

**Keywords to Remember**:
- photorealistic, cinematic, film quality
- natural movement, realistic physics
- practical lighting, color grading
- professional cinematography, 8K

---

Made with 🎥 Real-world style AI filmmaking
