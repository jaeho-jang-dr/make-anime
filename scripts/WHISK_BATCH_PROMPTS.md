# 🎨 Whisk 배치 작업 프롬프트 목록

## 사전 준비

### 공통 Style 이미지 (모든 장면에 동일하게 사용)
```
Studio Ghibli anime style, soft watercolor texture, warm color palette,
hand-painted look, cinematic composition, detailed backgrounds
```
→ Ghibli 스타일 레퍼런스 이미지를 다운로드하여 사용

### 작업 URL
🔗 https://labs.google/fx/tools/whisk

---

## 캐릭터 Subject 이미지 (먼저 생성!)

### CHAR-01: 루나 (Luna)
```
[Subject]: 빈 칸
[Scene]: plain white studio background, soft lighting
[Style]: Ghibli character design reference

[프롬프트 수정]:
"Beautiful anime girl, 16 years old, long silver-white flowing hair reaching waist,
deep ocean blue eyes with gentle expression, pale porcelain skin, wearing midnight
blue dress with silver star embroidery patterns, standing pose, full body view,
Studio Ghibli character design style, detailed anime illustration"
```
**저장**: `characters/luna_subject.png`

---

### CHAR-02: 스텔라 (Stella)
```
[Subject]: 빈 칸
[Scene]: dark space background with soft glow
[Style]: ethereal magical style reference

[프롬프트 수정]:
"Ethereal spirit child, appears 12 years old, translucent glowing golden body,
star-shaped sparkling eyes, hair made of flowing light particles and stardust,
luminescent aura surrounding body, floating pose, anime style magical being,
gentle innocent expression, fantasy illustration"
```
**저장**: `characters/stella_subject.png`

---

### CHAR-03: 할아버지 (Grandfather)
```
[Subject]: 빈 칸
[Scene]: warm indoor lighting background
[Style]: Ghibli character design reference

[프롬프트 수정]:
"Elderly Korean man, 75 years old, kind gentle face with smile wrinkles,
white beard well-groomed, warm caring eyes, wearing traditional blue hanbok
with white trim, wise grandfatherly expression, sitting pose,
Studio Ghibli character design style"
```
**저장**: `characters/grandfather_subject.png`

---

## ACT 1: 프롤로그 & 여정의 시작 (장면 001-005)

### SCENE-001: 별이 사라진 밤
```
[Subject]: empty dark sky (또는 빈 칸)
[Scene]: Traditional Korean village at night, completely dark sky with no stars,
        only dim lantern lights from houses, misty foggy atmosphere,
        thatched roof houses, dirt paths, mysterious empty sky above
[Style]: Ghibli anime style, melancholic mood

[프롬프트 수정]:
"Panoramic view of traditional Korean village at night, starless dark sky,
dim orange lantern lights glowing from windows, misty atmosphere,
thatched roof hanok houses, melancholic mood, Ghibli anime style,
watercolor texture, dark blue and purple tones, establishing shot"
```
**저장**: `scenes/scene_001.png` | **길이**: 20초

---

### SCENE-002: 루나의 방
```
[Subject]: luna_subject.png 업로드
[Scene]: Cozy Korean bedroom interior, girl sitting by window looking at dark sky,
        soft candlelight, books scattered around, wooden furniture,
        traditional but with modern touches
[Style]: Ghibli anime style, warm interior

[프롬프트 수정]:
"Anime girl with silver-white hair sitting by window in cozy Korean bedroom,
looking at dark starless sky outside, soft candlelight illuminating room,
books and scrolls scattered on wooden floor, traditional ondol room,
warm intimate atmosphere, Ghibli anime style, detailed interior"
```
**저장**: `scenes/scene_002.png` | **길이**: 15초

---

### SCENE-003: 할아버지의 이야기
```
[Subject]: luna_subject.png + grandfather_subject.png (또는 합성)
[Scene]: Traditional Korean living room with ondol floor heating,
        grandfather sitting with granddaughter, warm fireplace glow,
        old astronomical maps and star charts on walls
[Style]: Ghibli anime style, nostalgic warm

[프롬프트 수정]:
"Elderly Korean man in hanbok sitting with young anime girl with silver hair,
warm traditional living room with ondol floor, fireplace with orange glow,
old star maps hanging on wooden walls, intimate family moment,
nostalgic atmosphere, Ghibli anime style, warm color palette"
```
**저장**: `scenes/scene_003.png` | **길이**: 25초

---

### SCENE-004: 루나의 결심
```
[Subject]: luna_subject.png 업로드
[Scene]: Same living room, girl standing up with determined expression,
        dramatic moonlight streaming through window,
        heroic composition, low angle view
[Style]: Ghibli anime style, dramatic lighting

[프롬프트 수정]:
"Anime girl with silver-white hair standing with determined expression,
traditional Korean living room, dramatic moonlight streaming through window,
heroic pose, fists clenched with resolve, low angle composition,
emotional dramatic moment, Ghibli anime style"
```
**저장**: `scenes/scene_004.png` | **길이**: 15초

---

### SCENE-005: 여정의 시작
```
[Subject]: luna_subject.png 업로드
[Scene]: Village gate at night, small girl with paper lantern walking
        towards dark mysterious forest, warm village lights behind,
        dark forest path ahead, adventure beginning
[Style]: Ghibli anime style, adventure atmosphere

[프롬프트 수정]:
"Small anime girl with silver hair holding paper lantern, walking through
village gate towards dark forest, warm orange village lights behind her,
mysterious dark forest path ahead, adventure beginning composition,
contrast between warmth and unknown darkness, Ghibli anime style"
```
**저장**: `scenes/scene_005.png` | **길이**: 20초

---

## ACT 2: 신비로운 여정 (장면 006-013)

### SCENE-006: 신비로운 숲
```
[Subject]: luna_subject.png 업로드
[Scene]: Enchanted forest with bioluminescent mushrooms, glowing fireflies,
        twisted ancient trees, magical fantasy atmosphere,
        girl walking through with lantern
[Style]: Ghibli anime style, fantasy bioluminescent

[프롬프트 수정]:
"Anime girl walking through enchanted magical forest at night,
giant bioluminescent mushrooms glowing blue and purple,
swarms of golden fireflies, ancient twisted trees with glowing moss,
paper lantern illuminating path, fantasy atmosphere, Ghibli anime style,
detailed magical nature, mystical colors"
```
**저장**: `scenes/scene_006.png` | **길이**: 20초

---

### SCENE-007: 스텔라와의 만남
```
[Subject]: stella_subject.png (형성 중인 모습)
[Scene]: Forest clearing, spirit materializing from starlight,
        girl stepping back in surprise, magical particles swirling,
        dramatic magical manifestation
[Style]: Ghibli anime style, magical ethereal

[프롬프트 수정]:
"Glowing spirit child materializing from starlight particles in forest clearing,
anime girl with silver hair stepping back in surprise,
magical sparkles and light particles swirling around,
ethereal manifestation scene, wonder and surprise,
Ghibli anime style, beautiful light effects"
```
**저장**: `scenes/scene_007.png` | **길이**: 25초

---

### SCENE-008: 스텔라의 정체
```
[Subject]: luna_subject.png + stella_subject.png
[Scene]: Forest clearing at night, spirit child floating before girl,
        gentle conversation, soft ethereal light, peaceful atmosphere
[Style]: Ghibli anime style, gentle ethereal

[프롬프트 수정]:
"Glowing translucent spirit child floating before anime girl with silver hair,
gentle conversation in moonlit forest clearing,
soft ethereal golden light from spirit illuminating both,
peaceful magical encounter, friendship forming,
Ghibli anime style, intimate moment"
```
**저장**: `scenes/scene_008.png` | **길이**: 20초

---

### SCENE-009: 어둠의 동굴 입구
```
[Subject]: luna_subject.png + stella_subject.png (작게)
[Scene]: Massive dark cave entrance shaped like monster mouth,
        swirling ominous darkness inside, two small figures at entrance,
        intimidating scale contrast
[Style]: Ghibli anime style, ominous dramatic

[프롬프트 수정]:
"Massive ominous cave entrance shaped like monster mouth,
swirling purple-black darkness inside, two tiny figures at entrance,
anime girl with lantern and glowing spirit child,
dramatic scale showing how small they are, intimidating atmosphere,
Ghibli anime style, dark fantasy"
```
**저장**: `scenes/scene_009.png` | **길이**: 15초

---

### SCENE-010: 동굴 속으로
```
[Subject]: luna_subject.png 업로드
[Scene]: Inside dark cave tunnel, girl with small lantern and glowing spirit,
        vast darkness surrounding them, strange patterns on cave walls
[Style]: Ghibli anime style, dark atmospheric

[프롬프트 수정]:
"Anime girl walking inside dark cave tunnel holding lantern,
small glowing spirit child beside her, vast darkness surrounding,
strange ancient patterns carved on cave walls,
small circle of light in immense darkness, brave atmosphere,
Ghibli anime style, dramatic light contrast"
```
**저장**: `scenes/scene_010.png` | **길이**: 20초

---

### SCENE-011: 갇힌 별들
```
[Subject]: trapped glowing orbs
[Scene]: Vast underground cavern, hundreds of dim glowing star orbs
        trapped in dark crystalline cages, sad fading starlight,
        melancholic beautiful scene
[Style]: Ghibli anime style, sad beautiful

[프롬프트 수정]:
"Vast underground cavern filled with hundreds of stars trapped in
dark crystalline cages, dim fading golden starlight from each orb,
sad melancholic atmosphere, beautiful yet heartbreaking scene,
huge scale cavern with countless imprisoned stars,
Ghibli anime style, detailed fantasy environment"
```
**저장**: `scenes/scene_011.png` | **길이**: 20초

---

### SCENE-012: 어둠의 괴물 등장
```
[Subject]: shadow monster forming
[Scene]: Massive shadow creature made of pure darkness emerging,
        glowing red eyes, formless shifting body,
        small girl facing it bravely
[Style]: Ghibli anime style, dramatic villain

[프롬프트 수정]:
"Massive shadow monster made of swirling pure darkness emerging,
glowing menacing red eyes, formless shifting tentacle body,
small anime girl standing bravely before it,
dramatic scale contrast, terrifying yet artistic design,
Ghibli anime style, epic confrontation scene"
```
**저장**: `scenes/scene_012.png` | **길이**: 25초

---

### SCENE-013: 대치
```
[Subject]: luna_subject.png 업로드
[Scene]: Small girl standing bravely before massive shadow creature,
        Stella glowing beside her, tense dramatic standoff,
        David vs Goliath composition
[Style]: Ghibli anime style, heroic dramatic

[프롬프트 수정]:
"Anime girl with silver hair standing bravely before massive shadow monster,
glowing spirit child floating protectively beside her,
dramatic standoff in dark cavern, heroic pose despite fear,
low angle shot emphasizing girl's courage against giant enemy,
Ghibli anime style, epic confrontation"
```
**저장**: `scenes/scene_013.png` | **길이**: 15초

---

## ACT 3: 클라이맥스 (장면 014-021)

### SCENE-014: 괴물의 공격
```
[Subject]: shadow tentacles + luna + stella
[Scene]: Dark tendrils shooting towards girl, spirit creating light shield,
        dynamic action scene, desperate defense
[Style]: Ghibli anime style, action dynamic

[프롬프트 수정]:
"Dark shadow tentacles shooting towards anime girl,
glowing spirit child creating protective light shield,
dynamic action pose, desperate defense moment,
swirling darkness vs golden light, intense battle scene,
Ghibli anime style, dramatic action"
```
**저장**: `scenes/scene_014.png` | **길이**: 20초

---

### SCENE-015: 스텔라의 희생
```
[Subject]: stella protecting luna
[Scene]: Spirit child spreading arms to shield girl, taking damage,
        light fading, emotional sacrifice scene
[Style]: Ghibli anime style, emotional sacrifice

[프롬프트 수정]:
"Glowing spirit child spreading arms protectively in front of anime girl,
taking darkness damage, golden light fading and flickering,
emotional sacrifice moment, tears forming in girl's eyes,
heartbreaking scene, spirit's body becoming translucent,
Ghibli anime style, emotional peak"
```
**저장**: `scenes/scene_015.png` | **길이**: 25초

---

### SCENE-016: 루나의 눈물
```
[Subject]: luna crying
[Scene]: Girl kneeling, holding fading spirit in arms, tears falling,
        emotional breakdown in dark cave
[Style]: Ghibli anime style, emotional climax

[프롬프트 수정]:
"Anime girl with silver hair kneeling on cave floor,
holding fading translucent spirit child in her arms,
tears streaming down her face, emotional breakdown,
dim fading golden light from dying spirit,
Ghibli anime style, heartbreaking moment, grief"
```
**저장**: `scenes/scene_016.png` | **길이**: 20초

---

### SCENE-017: 기적의 시작
```
[Subject]: glowing tears
[Scene]: Tears transforming into starlight, magical transformation beginning,
        girl surrounded by gentle glow, hope emerging
[Style]: Ghibli anime style, magical hope

[프롬프트 수정]:
"Anime girl's tears transforming into glowing starlight droplets,
magical sparkles forming around her, golden light emerging from grief,
hope beginning to manifest, beautiful magical transformation,
dark cave slowly illuminating, miracle beginning,
Ghibli anime style, magical realism"
```
**저장**: `scenes/scene_017.png` | **길이**: 20초

---

### SCENE-018: 빛의 폭발
```
[Subject]: luna radiating light
[Scene]: Girl standing up, brilliant light exploding from her heart,
        darkness being pushed back, powerful magical moment
[Style]: Ghibli anime style, climactic power

[프롬프트 수정]:
"Anime girl standing up with brilliant starlight exploding from her chest,
massive light burst pushing back all darkness,
powerful magical transformation, hair and dress flowing with energy,
darkness retreating from overwhelming light,
Ghibli anime style, climactic power moment, epic"
```
**저장**: `scenes/scene_018.png` | **길이**: 20초

---

### SCENE-019: 괴물의 소멸
```
[Subject]: shadow monster dissolving
[Scene]: Darkness creature being dissolved by brilliant starlight,
        fragments of darkness scattering, victory moment
[Style]: Ghibli anime style, villain defeat

[프롬프트 수정]:
"Massive shadow monster being dissolved by overwhelming starlight,
creature screaming silently as darkness fragments scatter,
brilliant golden light consuming darkness completely,
dramatic defeat of evil, triumphant moment,
Ghibli anime style, light conquering darkness"
```
**저장**: `scenes/scene_019.png` | **길이**: 20초

---

### SCENE-020: 별들의 해방
```
[Subject]: stars breaking free
[Scene]: Thousands of stars breaking free from crystalline cages,
        brilliant lights rising, cavern filling with starlight
[Style]: Ghibli anime style, joyful liberation

[프롬프트 수정]:
"Thousands of golden stars breaking free from crystalline cages,
brilliant lights rising upward like fireflies,
dark cavern transforming into sea of starlight,
joyful liberation, magical celebration of freedom,
Ghibli anime style, beautiful light spectacle"
```
**저장**: `scenes/scene_020.png` | **길이**: 25초

---

### SCENE-021: 스텔라의 부활
```
[Subject]: stella reviving
[Scene]: Starlight gathering around faded spirit, gradual revival,
        girl watching hopefully, magical restoration
[Style]: Ghibli anime style, resurrection hope

[프롬프트 수정]:
"Freed starlight converging around faded spirit child,
spirit gradually regaining golden glow and form,
anime girl watching with hopeful tearful eyes,
magical revival scene, life returning,
Ghibli anime style, resurrection moment"
```
**저장**: `scenes/scene_021.png` | **길이**: 20초

---

## ACT 4: 해피엔딩 (장면 022-030)

### SCENE-022: 하늘로 돌아가는 별들
```
[Subject]: stars rising
[Scene]: Stream of stars flying up through cave opening into night sky,
        beautiful river of light, triumphant return
[Style]: Ghibli anime style, triumphant

[프롬프트 수정]:
"Thousands of golden stars streaming upward through cave opening,
beautiful river of light ascending to night sky,
magnificent view from inside cave looking up,
triumphant return of stars to their home,
Ghibli anime style, breathtaking spectacle"
```
**저장**: `scenes/scene_022.png` | **길이**: 25초

---

### SCENE-023: 별이 빛나는 하늘
```
[Subject]: starry night sky
[Scene]: Magnificent night sky filled with countless stars,
        Milky Way visible, breathtaking celestial view
[Style]: Ghibli anime style, Van Gogh inspired

[프롬프트 수정]:
"Magnificent night sky completely filled with countless sparkling stars,
Milky Way galaxy clearly visible stretching across,
Van Gogh starry night inspired, swirling cosmic beauty,
breathtaking celestial panorama, starlight illuminating land below,
Ghibli anime style, magical night sky"
```
**저장**: `scenes/scene_023.png` | **길이**: 20초

---

### SCENE-024: 마을의 기쁨
```
[Subject]: villagers looking up
[Scene]: Korean village with people coming outside, looking up at starry sky,
        joyful expressions, lanterns mixing with starlight
[Style]: Ghibli anime style, celebration

[프롬프트 수정]:
"Korean villagers coming out of their homes looking up at starry sky,
joyful surprised expressions, children pointing at stars,
warm lantern light mixing with cool starlight,
community celebration moment, happiness returning,
Ghibli anime style, heartwarming scene"
```
**저장**: `scenes/scene_024.png` | **길이**: 20초

---

### SCENE-025: 루나의 귀환
```
[Subject]: luna_subject.png + stella_subject.png
[Scene]: Girl walking back to village with spirit friend,
        starry sky above, village lights ahead
[Style]: Ghibli anime style, heroic return

[프롬프트 수정]:
"Anime girl with silver hair walking towards village at dawn,
glowing spirit child floating happily beside her,
magnificent starry sky above, warm village lights ahead,
heroic return after adventure, friendship and triumph,
Ghibli anime style, journey's end"
```
**저장**: `scenes/scene_025.png` | **길이**: 20초

---

### SCENE-026: 할아버지와의 재회
```
[Subject]: grandfather hugging luna
[Scene]: Elderly man embracing young girl at village gate,
        spirit floating nearby, emotional reunion
[Style]: Ghibli anime style, emotional reunion

[프롬프트 수정]:
"Elderly Korean man in hanbok embracing young anime girl at village gate,
tears of joy, glowing spirit child floating nearby smiling,
starlight overhead, emotional family reunion,
grandfather proud and relieved, heartwarming moment,
Ghibli anime style, family love"
```
**저장**: `scenes/scene_026.png` | **길이**: 20초

---

### SCENE-027: 스텔라의 선물
```
[Subject]: stella giving pendant
[Scene]: Spirit child giving glowing star pendant to girl,
        magical gift exchange, friendship moment
[Style]: Ghibli anime style, magical gift

[프롬프트 수정]:
"Glowing spirit child presenting star-shaped pendant to anime girl,
pendant made of crystallized starlight, magical glow,
girl receiving gift with grateful expression,
friendship token exchange, beautiful moment,
Ghibli anime style, magical gift scene"
```
**저장**: `scenes/scene_027.png` | **길이**: 25초

---

### SCENE-028: 스텔라의 승천
```
[Subject]: stella ascending
[Scene]: Spirit child rising into sky, transforming into brightest star,
        girl waving goodbye, bittersweet farewell
[Style]: Ghibli anime style, ascension

[프롬프트 수정]:
"Spirit child rising gracefully into night sky,
body transforming into the brightest star,
anime girl waving goodbye from below with smile and tears,
bittersweet beautiful farewell, not goodbye forever,
Ghibli anime style, magical ascension"
```
**저장**: `scenes/scene_028.png` | **길이**: 25초

---

### SCENE-029: 별을 바라보는 루나
```
[Subject]: luna_subject.png 업로드
[Scene]: Girl on rooftop holding pendant, looking at brightest star,
        peaceful expression, beautiful starry night
[Style]: Ghibli anime style, peaceful

[프롬프트 수정]:
"Anime girl sitting on traditional Korean rooftop,
holding glowing star pendant close to heart,
looking up at the brightest star in sky with peaceful smile,
beautiful starry night, serene ending moment,
Ghibli anime style, contemplative"
```
**저장**: `scenes/scene_029.png` | **길이**: 20초

---

### SCENE-030: 에필로그 - 별빛 아래
```
[Subject]: peaceful village panorama
[Scene]: Panoramic view of Korean village under magnificent starry sky,
        brightest star twinkling, peaceful night, story ending
[Style]: Ghibli anime style, credits scene

[프롬프트 수정]:
"Panoramic view of traditional Korean village under magnificent starry sky,
one star shining brightest among thousands,
peaceful serene night, soft warm lights from houses,
story ending atmosphere, beautiful final frame,
Ghibli anime style, credits scene composition"
```
**저장**: `scenes/scene_030.png` | **길이**: 30초

---

## 📊 작업 요약

| 항목 | 수량 |
|------|------|
| 캐릭터 이미지 | 3개 |
| 장면 이미지 | 30개 |
| **총 Whisk 작업** | **33개** |
| 예상 소요 시간 | 2-3시간 |

### 저장 폴더 구조
```
d:\Projects\make-anime\
├── characters\
│   ├── luna_subject.png
│   ├── stella_subject.png
│   └── grandfather_subject.png
├── images\
│   └── scenes\
│       ├── scene_001.png
│       ├── scene_002.png
│       └── ... (scene_030.png)
└── scripts\
    └── (이 파일들)
```

---

**작업 시작하세요!** 🎬
