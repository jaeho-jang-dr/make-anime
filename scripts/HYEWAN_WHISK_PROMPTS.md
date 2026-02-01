# 🎨 혜완이의 밀양 일주일 - Whisk 프롬프트 가이드

## 작업 URL
🔗 https://labs.google/fx/tools/whisk

## 총 작업량
- **캐릭터**: 6개
- **장면**: 38개
- **합계**: 44개 이미지
- **예상 시간**: 3-4시간

---

# PART 1: 캐릭터 이미지 (먼저 생성!)

## CHAR-01: 혜완이 (주인공) - 남자아이
```
[Subject]: 혜완이 실제 사진 업로드 (김해완1학년.jpg)
[Scene]: plain white background, soft lighting
[Style]: Ghibli anime style reference

[프롬프트]:
Cute 8-year-old Korean boy, short black hair with neat bangs covering forehead,
big round dark eyes, adorable innocent face, soft gentle smile,
wearing gray striped long sleeve shirt with navy and orange stripes,
gentle and curious expression, full body standing pose,
Studio Ghibli character design style, warm pastel colors
```
**저장**: `characters/hyewan.png`

💡 **팁**: Subject에 실제 사진을 업로드하면 얼굴 특징을 유지하면서 애니메이션 스타일로 변환됩니다!

---

## CHAR-02: 할머니 (55세, 영어 선생님)
```
[Subject]: 빈 칸
[Scene]: warm indoor background
[Style]: Ghibli anime style reference

[프롬프트]:
Kind Korean grandmother, 55 years old, neat short permed hair,
round reading glasses, warm gentle smile with laugh lines,
wearing comfortable cream blouse and brown long skirt,
teacher-like elegant but approachable appearance,
standing pose, Studio Ghibli character design style
```
**저장**: `characters/grandmother.png`

---

## CHAR-03: 할아버지 (60세, 코딩 선생님)
```
[Subject]: 빈 칸
[Scene]: neutral background
[Style]: Ghibli anime style reference

[프롬프트]:
Gentle Korean grandfather, 60 years old, slightly gray short hair,
kind eyes with smile wrinkles, warm fatherly smile,
wearing navy polo shirt and khaki pants,
modern and tech-savvy yet warm appearance,
standing pose, Studio Ghibli character design style
```
**저장**: `characters/grandfather.png`

---

## CHAR-04: 엄마 (30세)
```
[Subject]: 빈 칸
[Scene]: bright background
[Style]: Ghibli anime style reference

[프롬프트]:
Young Korean mother, 30 years old, long black hair in ponytail,
gentle loving eyes, warm caring smile,
wearing light blue summer dress,
elegant and modern appearance,
standing pose, Studio Ghibli character design style
```
**저장**: `characters/mother.png`

---

## CHAR-05: 아빠 (30세)
```
[Subject]: 빈 칸
[Scene]: bright background
[Style]: Ghibli anime style reference

[프롬프트]:
Young Korean father, 30 years old, short neat black hair,
friendly warm smile, dependable appearance,
wearing white casual shirt and jeans,
kind and reliable look,
standing pose, Studio Ghibli character design style
```
**저장**: `characters/father.png`

---

## CHAR-06: 홍시 (검은 진돗개)
```
[Subject]: 빈 칸
[Scene]: outdoor grass background
[Style]: Ghibli anime style reference

[프롬프트]:
Beautiful black Korean Jindo dog, shiny pure black fur,
alert pointed ears standing up, intelligent friendly brown eyes,
pink tongue out happily, fluffy curled tail,
healthy muscular athletic build, loyal and playful expression,
sitting pose looking at camera,
Studio Ghibli anime style, warm friendly atmosphere
```
**저장**: `characters/hongsi.png`

---

# PART 2: 장면 이미지 (38개)

## DAY 0: 여행 & 도착 (001-006)

### SCENE-001: 대전역
```
[Subject]: hyewan.png + mother.png + father.png
[Scene]: Modern Daejeon train station exterior, sunny summer morning,
        Korean family with luggage waiting for train, bright blue sky
[Style]: Ghibli anime, warm summer travel atmosphere

[프롬프트]:
Korean family at Daejeon train station, little boy with parents,
modern station building, sunny summer morning, luggage beside them,
excited travel atmosphere, blue sky with white clouds,
Studio Ghibli anime style, warm colors, adventure beginning
```
**저장**: `scenes/scene_001.png` | **15초**

---

### SCENE-002: KTX 안
```
[Subject]: hyewan.png
[Scene]: Inside KTX train, boy looking out window excitedly,
        countryside passing by in blur, comfortable seats
[Style]: Ghibli anime, travel excitement

[프롬프트]:
Little Korean boy excitedly looking out KTX train window,
pressing face against glass, green countryside blurring past,
parents smiling beside her, comfortable train interior,
sunlight streaming through window, motion blur outside,
Studio Ghibli anime style, joyful travel scene
```
**저장**: `scenes/scene_002.png` | **18초**

---

### SCENE-003: 밀양역 도착
```
[Subject]: grandmother.png + grandfather.png
[Scene]: Miryang station platform, elderly couple waving happily,
        small town station, summer afternoon
[Style]: Ghibli anime, heartwarming reunion

[프롬프트]:
Korean grandparents waiting at Miryang station platform,
waving happily at arriving train, small town station atmosphere,
warm afternoon sunlight, excited expressions,
Studio Ghibli anime style, heartwarming reunion scene
```
**저장**: `scenes/scene_003.png` | **15초**

---

### SCENE-004: 반가운 포옹
```
[Subject]: hyewan.png + grandmother.png
[Scene]: Station platform, boy running into grandmother's arms,
        joyful hug, family watching
[Style]: Ghibli anime, emotional reunion

[프롬프트]:
Little boy running into grandmother's open arms on train platform,
joyful tight hug, grandmother bending down to embrace,
parents and grandfather watching with happy smiles,
warm golden sunlight, emotional reunion moment,
Studio Ghibli anime style
```
**저장**: `scenes/scene_004.png` | **12초**

---

### SCENE-005: 할머니 집
```
[Subject]: 집 외관
[Scene]: Cozy Korean house in Miryang, small flower garden,
        traditional-modern mix, evening golden hour
[Style]: Ghibli anime, warm home feeling

[프롬프트]:
Cozy Korean house in Miryang countryside, small front yard with
colorful flowers, mix of traditional and modern architecture,
warm evening golden hour light, welcoming home atmosphere,
family arriving with luggage, Studio Ghibli anime style
```
**저장**: `scenes/scene_005.png` | **18초**

---

### SCENE-006: 저녁 식사
```
[Subject]: 가족 모두
[Scene]: Korean family dinner table, delicious home-cooked meal,
        warm kitchen, happy conversation
[Style]: Ghibli anime, warm family scene

[프롬프트]:
Korean family gathered around dinner table, grandmother serving
delicious home-cooked Korean food, multiple dishes on table,
warm kitchen lighting, everyone smiling and chatting happily,
cozy family dinner atmosphere, Studio Ghibli anime style,
detailed food illustration
```
**저장**: `scenes/scene_006.png` | **18초**

---

## DAY 1: 부모님 작별 & 홍시 (007-011)

### SCENE-007: 부모님 떠나는 아침
```
[Subject]: mother.png + father.png
[Scene]: House doorway, parents with bags, early morning,
        bittersweet farewell atmosphere
[Style]: Ghibli anime, morning farewell

[프롬프트]:
Korean parents at house doorway with travel bags, early morning light,
preparing to leave for work in Daejeon, slightly sad but understanding
expressions, grandmother and boy seeing them off,
bittersweet morning atmosphere, Studio Ghibli anime style
```
**저장**: `scenes/scene_007.png` | **15초**

---

### SCENE-008: 씩씩한 작별
```
[Subject]: hyewan.png
[Scene]: Front of house, boy waving bravely, parents in car,
        grandmother supporting
[Style]: Ghibli anime, brave farewell

[프롬프트]:
Little boy standing bravely waving goodbye to parents in car,
trying to be strong, grandmother holding her hand supportively,
morning sunlight, parents waving back through car window,
emotional but brave farewell, Studio Ghibli anime style
```
**저장**: `scenes/scene_008.png` | **15초**

---

### SCENE-009: 홍시 등장!
```
[Subject]: hongsi.png
[Scene]: Front yard, black Jindo dog trotting over from next door,
        tail wagging, sunny morning
[Style]: Ghibli anime, cute dog introduction

[프롬프트]:
Beautiful black Korean Jindo dog trotting happily into front yard,
coming from neighbor's house, tail wagging enthusiastically,
tongue out, friendly curious expression, sunny morning light,
boy noticing with surprise in background,
Studio Ghibli anime style, cheerful scene
```
**저장**: `scenes/scene_009.png` | **18초**

---

### SCENE-010: 홍시와 첫 인사
```
[Subject]: hyewan.png + hongsi.png
[Scene]: Garden, boy kneeling to pet dog, dog sniffing her hand,
        grandmother watching
[Style]: Ghibli anime, friendship beginning

[프롬프트]:
Little boy kneeling down to meet black Jindo dog at eye level,
dog sniffing her hand gently, boy smiling with delight,
grandmother watching with warm smile in background,
garden setting with flowers, friendship forming moment,
Studio Ghibli anime style
```
**저장**: `scenes/scene_010.png` | **18초**

---

### SCENE-011: 홍시와 뛰어놀기
```
[Subject]: hyewan.png + hongsi.png
[Scene]: Garden, boy and dog running playfully, joyful energy,
        summer sunshine
[Style]: Ghibli anime, playful energy

[프롬프트]:
Little boy and black Jindo dog running together in garden,
dog chasing boy playfully, both full of energy and joy,
summer sunshine, grandmother watching from porch with smile,
dynamic playful movement, Studio Ghibli anime style
```
**저장**: `scenes/scene_011.png` | **15초**

---

## DAY 2: 영어 & 코딩 (012-016)

### SCENE-012: 영어 수업
```
[Subject]: grandmother.png + hyewan.png
[Scene]: Living room with books, grandmother teaching English,
        ABC books, warm learning atmosphere
[Style]: Ghibli anime, educational scene

[프롬프트]:
Grandmother with reading glasses teaching English to grandson,
living room with bookshelves, ABC picture books on table,
warm educational atmosphere, boy listening attentively,
soft indoor lighting, Studio Ghibli anime style
```
**저장**: `scenes/scene_012.png` | **18초**

---

### SCENE-013: 영어 노래
```
[Subject]: grandmother.png + hyewan.png
[Scene]: Same room, singing together, musical notes floating,
        fun learning
[Style]: Ghibli anime, musical joy

[프롬프트]:
Grandmother and grandson singing English ABC song together,
musical notes floating in air, both with happy expressions,
clapping hands rhythmically, fun learning moment,
playful educational atmosphere, Studio Ghibli anime style
```
**저장**: `scenes/scene_013.png` | **15초**

---

### SCENE-014: 할아버지 퇴근
```
[Subject]: grandfather.png + hyewan.png + hongsi.png
[Scene]: House entrance, grandfather arriving home, boy and dog
        running to greet him, evening light
[Style]: Ghibli anime, homecoming

[프롬프트]:
Grandfather arriving home from work in evening, little boy and
black Jindo dog running excitedly to greet him at door,
grandfather smiling warmly with open arms, golden sunset light,
happy homecoming scene, Studio Ghibli anime style
```
**저장**: `scenes/scene_014.png` | **15초**

---

### SCENE-015: 코딩 수업
```
[Subject]: grandfather.png + hyewan.png
[Scene]: Study room with computer, teaching coding, colorful code
        on screen, dog nearby
[Style]: Ghibli anime, modern learning

[프롬프트]:
Grandfather teaching coding to grandson at computer desk,
colorful simple code on screen, boy watching with curiosity,
black dog lying peacefully nearby, warm desk lamp light,
modern technology meets family warmth, Studio Ghibli anime style
```
**저장**: `scenes/scene_015.png` | **20초**

---

### SCENE-016: 첫 코드 성공
```
[Subject]: hyewan.png
[Scene]: Computer screen with program running, boy's eyes sparkling,
        achievement moment
[Style]: Ghibli anime, success joy

[프롬프트]:
Little boy's face lit up with joy and amazement looking at computer screen,
simple program running successfully, eyes sparkling with achievement,
grandfather smiling proudly beside her, screen glow on face,
magical discovery moment, Studio Ghibli anime style
```
**저장**: `scenes/scene_016.png` | **15초**

---

## DAY 3: 공원 나들이 (017-020)

### SCENE-017: 공원 가는 길
```
[Subject]: grandmother.png + hyewan.png + hongsi.png
[Scene]: Neighborhood street, walking to park with dog on leash,
        sunny summer day
[Style]: Ghibli anime, peaceful walk

[프롬프트]:
Grandmother and grandson walking down Korean neighborhood street,
black Jindo dog on leash walking beside them, tree-lined street,
sunny summer day, peaceful small town atmosphere,
heading to park, Studio Ghibli anime style
```
**저장**: `scenes/scene_017.png` | **15초**

---

### SCENE-018: 놀이터
```
[Subject]: hyewan.png
[Scene]: Park playground, boy on swing, grandmother and dog
        watching from bench
[Style]: Ghibli anime, childhood joy

[프롬프트]:
Little boy swinging high on playground swing with big smile,
hair flowing in wind, grandmother sitting on park bench watching,
black dog sitting obediently beside grandmother,
bright sunny park, childhood joy, Studio Ghibli anime style
```
**저장**: `scenes/scene_018.png` | **18초**

---

### SCENE-019: 홍시와 공놀이
```
[Subject]: hyewan.png + hongsi.png
[Scene]: Park grass field, playing fetch with dog, summer sunshine
[Style]: Ghibli anime, playful energy

[프롬프트]:
Little boy throwing ball for black Jindo dog on park grass field,
dog running to catch ball with joy, dynamic playful movement,
bright summer sunshine, green grass, trees in background,
energetic playtime, Studio Ghibli anime style
```
**저장**: `scenes/scene_019.png` | **18초**

---

### SCENE-020: 아이스크림 휴식
```
[Subject]: grandmother.png + hyewan.png + hongsi.png
[Scene]: Park bench under tree, eating ice cream, dog resting
[Style]: Ghibli anime, sweet moment

[프롬프트]:
Grandmother and grandson sitting on park bench under shady tree,
eating ice cream cones happily, black dog resting at their feet,
dappled sunlight through leaves, peaceful summer break,
sweet bonding moment, Studio Ghibli anime style
```
**저장**: `scenes/scene_020.png` | **15초**

---

## DAY 4: 할머니 친구 집 (021-024)

### SCENE-021: 친구 집 가는 길
```
[Subject]: grandmother.png + hyewan.png
[Scene]: Walking through neighborhood, carrying gift, dressed nicely
[Style]: Ghibli anime, visiting

[프롬프트]:
Grandmother and grandson walking through Miryang neighborhood,
nicely dressed for visit, carrying small wrapped gift,
traditional Korean residential area, afternoon sunshine,
anticipation of visit, Studio Ghibli anime style
```
**저장**: `scenes/scene_021.png` | **12초**

---

### SCENE-022: 친구 할머니 집
```
[Subject]: 친구 할머니
[Scene]: Traditional house doorway, friendly elderly woman greeting,
        cat visible inside
[Style]: Ghibli anime, warm hospitality

[프롬프트]:
Friendly elderly Korean woman at doorway of traditional house,
warmly greeting grandmother and grandson, welcoming gesture,
fluffy cat peeking from inside, traditional home entrance,
Korean hospitality atmosphere, Studio Ghibli anime style
```
**저장**: `scenes/scene_022.png` | **15초**

---

### SCENE-023: 맛있는 간식
```
[Subject]: hyewan.png
[Scene]: Traditional living room, Korean sweets and fruits on table,
        grandmothers chatting
[Style]: Ghibli anime, Korean hospitality

[프롬프트]:
Little boy happily eating Korean traditional sweets at low table,
colorful rice cakes and fresh fruit arranged beautifully,
two grandmothers chatting warmly in background,
traditional Korean living room, cozy afternoon,
Studio Ghibli anime style, detailed food
```
**저장**: `scenes/scene_023.png` | **15초**

---

### SCENE-024: 고양이와 놀기
```
[Subject]: hyewan.png + 고양이
[Scene]: Living room floor, playing with fluffy cat, cat toy,
        afternoon sunlight
[Style]: Ghibli anime, cute animal scene

[프롬프트]:
Little boy lying on floor playing with fluffy cat,
dangling cat toy, cat batting at it playfully,
both having fun, afternoon sunlight streaming in,
cute animal interaction, Studio Ghibli anime style
```
**저장**: `scenes/scene_024.png` | **18초**

---

## DAY 5: 게임 만들기 (025-028)

### SCENE-025: 게임 아이디어
```
[Subject]: grandfather.png + hyewan.png
[Scene]: Computer desk, discussing game ideas, sketch paper,
        dog watching
[Style]: Ghibli anime, creative process

[프롬프트]:
Grandfather and grandson at desk brainstorming game ideas,
sketch paper with doodles, excited discussion,
black dog watching curiously from floor,
creative atmosphere, Studio Ghibli anime style
```
**저장**: `scenes/scene_025.png` | **18초**

---

### SCENE-026: 캐릭터 그리기
```
[Subject]: hyewan.png
[Scene]: Drawing cute dog character, colored pencils,
        creative expression
[Style]: Ghibli anime, child's creativity

[프롬프트]:
Little boy concentrating on drawing game character,
cute black dog character on paper that looks like Hongsi,
colored pencils scattered around, tongue out in concentration,
proud artistic creation, Studio Ghibli anime style
```
**저장**: `scenes/scene_026.png` | **15초**

---

### SCENE-027: 게임 완성!
```
[Subject]: grandfather.png + hyewan.png
[Scene]: Computer showing game with dog character, celebration,
        playing together
[Style]: Ghibli anime, achievement

[프롬프트]:
Computer screen showing simple game with cute black dog character jumping,
boy and grandfather playing together excitedly, high-five moment,
achievement celebration, screen glow,
Studio Ghibli anime style
```
**저장**: `scenes/scene_027.png` | **18초**

---

### SCENE-028: 홍시의 반응
```
[Subject]: hongsi.png
[Scene]: Dog looking at screen curiously, tilting head,
        family laughing
[Style]: Ghibli anime, funny moment

[프롬프트]:
Black Jindo dog sitting in front of computer screen,
tilting head curiously at cartoon dog on screen,
confused cute expression, family laughing in background,
funny adorable moment, Studio Ghibli anime style
```
**저장**: `scenes/scene_028.png` | **12초**

---

## DAY 6: 마지막 밤 (029-030)

### SCENE-029: 별 보기
```
[Subject]: 할머니 할아버지 + hyewan.png + hongsi.png
[Scene]: House yard at night, looking at starry sky,
        peaceful night
[Style]: Ghibli anime, magical night

[프롬프트]:
Family in house yard at night looking up at beautiful starry sky,
boy pointing at stars, grandparents smiling, black dog sitting beside them,
magical night atmosphere, countless stars,
peaceful evening, Studio Ghibli anime style
```
**저장**: `scenes/scene_029.png` | **15초**

---

### SCENE-030: 할머니 무릎 베개
```
[Subject]: grandmother.png + hyewan.png + hongsi.png
[Scene]: Living room at night, boy on grandmother's lap,
        dog sleeping nearby, warm lamp
[Style]: Ghibli anime, tender moment

[프롬프트]:
Little boy lying on grandmother's lap in cozy living room,
grandmother gently stroking her hair, boy's eyes closing sleepily,
black dog curled up sleeping nearby, warm lamp light,
tender loving moment, Studio Ghibli anime style
```
**저장**: `scenes/scene_030.png` | **15초**

---

## DAY 7: 작별 & 귀가 (031-038)

### SCENE-031: 마지막 아침
```
[Subject]: hyewan.png + hongsi.png
[Scene]: Guest room, packing bag, dog watching from doorway,
        bittersweet morning
[Style]: Ghibli anime, last day

[프롬프트]:
Little boy packing small bag in guest room, slightly sad expression,
black dog watching from doorway with understanding eyes,
morning light through window, last day atmosphere,
bittersweet moment, Studio Ghibli anime style
```
**저장**: `scenes/scene_031.png` | **12초**

---

### SCENE-032: 부모님 도착
```
[Subject]: mother.png + father.png
[Scene]: Car arriving at house, parents getting out,
        excited reunion
[Style]: Ghibli anime, joyful arrival

[프롬프트]:
Car arriving at grandmother's house, parents getting out waving,
boy running out with dog beside her to greet them,
excited happy reunion, sunny morning,
joyful atmosphere, Studio Ghibli anime style
```
**저장**: `scenes/scene_032.png` | **12초**

---

### SCENE-033: 엄마 품으로
```
[Subject]: hyewan.png + mother.png
[Scene]: Girl running to mother, emotional embrace,
        family watching
[Style]: Ghibli anime, emotional reunion

[프롬프트]:
Little boy running with open arms into mother's embrace,
tight emotional hug, father watching with warm smile,
grandparents and dog in background, happy tears,
reunion moment, Studio Ghibli anime style
```
**저장**: `scenes/scene_033.png` | **12초**

---

### SCENE-034: 홍시와 작별
```
[Subject]: hyewan.png + hongsi.png
[Scene]: Girl hugging dog tightly, dog licking her face,
        emotional goodbye
[Style]: Ghibli anime, friendship farewell

[프롬프트]:
Little boy kneeling and hugging black Jindo dog tightly,
dog licking her cheek affectionately, both saying goodbye,
emotional farewell between friends, family watching touched,
friendship goodbye, Studio Ghibli anime style
```
**저장**: `scenes/scene_034.png` | **18초**

---

### SCENE-035: 할머니 할아버지께 인사
```
[Subject]: hyewan.png + grandmother.png + grandfather.png
[Scene]: Doorway, hugging grandparents, tearful happy goodbye
[Style]: Ghibli anime, loving farewell

[프롬프트]:
Little boy hugging grandmother tightly at doorway,
grandfather patting her head lovingly, tearful but happy goodbye,
black dog sitting nearby, emotional family farewell,
love and gratitude, Studio Ghibli anime style
```
**저장**: `scenes/scene_035.png` | **15초**

---

### SCENE-036: 차에서 손 흔들기
```
[Subject]: hyewan.png
[Scene]: Girl waving from car window, grandparents and dog
        waving back, car departing
[Style]: Ghibli anime, bittersweet departure

[프롬프트]:
Little boy in back seat of car waving through window,
grandparents and black dog waving goodbye from house,
car slowly pulling away, bittersweet departure,
hands waving until out of sight, Studio Ghibli anime style
```
**저장**: `scenes/scene_036.png` | **15초**

---

### SCENE-037: 추억 몽타주
```
[Subject]: 여러 장면 콜라주
[Scene]: Memory montage - English class, coding, park, dog,
        cat, game, stargazing
[Style]: Ghibli anime, dreamy memories

[프롬프트]:
Dreamy memory collage of happy moments: English lesson with grandmother,
coding with grandfather, playing at park, running with black dog,
playing with cat, making game, watching stars together,
soft glowing edges, nostalgic filter, Studio Ghibli anime style
```
**저장**: `scenes/scene_037.png` | **18초**

---

### SCENE-038: 엔딩 - 홍시가 기다려
```
[Subject]: hongsi.png + 할머니 집
[Scene]: House at sunset, dog sitting in yard looking at road,
        waiting for friend, warm ending
[Style]: Ghibli anime, nostalgic ending

[프롬프트]:
Miryang house at golden sunset hour, black Jindo dog sitting in
front yard looking down the road, waiting for friend to return,
grandparents on porch watching sunset, warm lights from windows,
hopeful waiting, beautiful ending scene,
Studio Ghibli anime style, credits atmosphere
```
**저장**: `scenes/scene_038.png` | **20초**

---

# 📊 작업 요약

| 구분 | 수량 | 예상 시간 |
|------|------|----------|
| 캐릭터 | 6개 | 30분 |
| Day 0 장면 | 6개 | 30분 |
| Day 1 장면 | 5개 | 25분 |
| Day 2 장면 | 5개 | 25분 |
| Day 3 장면 | 4개 | 20분 |
| Day 4 장면 | 4개 | 20분 |
| Day 5 장면 | 4개 | 20분 |
| Day 6 장면 | 2개 | 10분 |
| Day 7 장면 | 8개 | 40분 |
| **총합** | **44개** | **약 3-4시간** |

---

# 💡 작업 팁

1. **캐릭터 먼저**: 6개 캐릭터 이미지를 먼저 만들어 저장
2. **Subject 재사용**: 같은 캐릭터는 저장한 이미지를 계속 업로드
3. **Style 통일**: 모든 장면에 같은 Ghibli 스타일 레퍼런스 사용
4. **순서대로**: Scene 001부터 순서대로 작업
5. **파일명 규칙**: `scene_001.png`, `scene_002.png` 형식으로 저장

---

**작업 시작!** 🎬
