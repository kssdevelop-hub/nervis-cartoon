# МУЛЬТИК "МИШКА И ПЕРВЫЙ СВЕТ" — ПИЛОТНЫЙ ПРОЕКТ
# Первые 2 сцены, ~1:30 длительности
# Для генерации через Runway API

PROJECT_METADATA = {
    "title": "Мишка и первый свет",
    "episode": "Пилот",
    "duration": "1:30",
    "target_fps": 24,
    "style": "soft 2D/3D hybrid cartoon, warm forest colors",
    "target_audience": "семейный",
}

# ============================================================================
# СЦЕНА 1: "ПРОБУЖДЕНИЕ ЛЕСА" (0:00–0:45)
# ============================================================================

SCENE_1 = {
    "name": "Пробуждение леса",
    "duration": 45,
    "shots": [
        {
            "id": "S1_K1",
            "name": "Берлога в темном лесу на рассвете",
            "duration": 5,
            "timecode": "0:00–0:05",
            "description": "Берлога, снег, темный лес, рассвет. Камера: медленный план с дрона. Движение: долгая панорама над берлогой.",
            "image_prompt": "misty pine forest at dawn, dark forest with snow, bear den entrance barely visible, cold winter atmosphere, soft blue light breaking through, cinematic wide shot, fog and mist, magical forest lighting, high detail",
            "video_prompt": "Camera pans slowly over snowy forest, misty dawn breaking through trees, soft blue light growing warmer, snow glistens faintly, peaceful forest awakening, smooth cinematic motion, 3-5 seconds",
            "character": None,
            "background": "Forest - Winter to Spring Transition",
            "music_note": "Soft ambient forest sounds, wind, minimal music",
            "status": "pending",
        },
        {
            "id": "S1_K2",
            "name": "Мишка просыпается в берлоге",
            "duration": 7,
            "timecode": "0:05–0:12",
            "description": "Мишка спит, шевелится, зевает, потягивается. Слышно хруст снега. Нос начинает шевелиться. Он открывает глаза.",
            "image_prompt": "young brown bear sleeping in cozy den, soft fur, round gentle face, warm honey brown colors, peaceful expression, snow visible at den entrance, golden morning light, cartoon style, highly detailed, soft animation ready",
            "video_prompt": "Bear slowly wakes up inside cozy den, stretches sleepily, yawns wide showing big teeth, gentle motion, smoke of breath visible in cold air, soft golden light from outside, opens eyes slowly, sleepy expression becomes alert, smooth cinematic animation, 3-5 seconds",
            "character": "Mishka (Bear)",
            "background": "Bear Den - Inside",
            "music_note": "Soft wake-up sounds, gentle forest ambience",
            "status": "pending",
        },
        {
            "id": "S1_K3",
            "name": "Мишка выходит из берлоги",
            "duration": 8,
            "timecode": "0:12–0:20",
            "description": "Мишка выходит из берлоги. Слегка растерян, оглядыва��тся. Видит, что снег уже тает, на деревьях пахнет весной. В воздухе появляются первые капли воды.",
            "image_prompt": "young brown bear standing at den entrance, looking out at spring forest, surprised curious expression, warm brown fur, standing on hind legs or four legs, misty dawn light, snow melting around den, first signs of spring, cinematic lighting, cartoon animation style, warm and cool colors blending, highly detailed",
            "video_prompt": "Bear emerges from den, stretches and looks around confused but happy, sniffs the air, camera pulls back showing melting snow and spring forest, soft golden light increases, bear's expression changes from sleepy to alert and joyful, gentle motion, cinematic camera movement, 4-5 seconds",
            "character": "Mishka (Bear)",
            "background": "Forest - Den Entrance - Melting Snow",
            "music_note": "First birds chirping, water dripping, soft music beginning",
            "status": "pending",
        },
        {
            "id": "S1_K4",
            "name": "Мишка идёт по лесной тропе",
            "duration": 8,
            "timecode": "0:20–0:28",
            "description": "Мишка идёт по лесной тропе. Он останавливается, вдохновляется запахом мокрой земли. Первая птица кричит. Мишка улыбается.",
            "image_prompt": "young brown bear walking on forest path through melting snow, warm spring atmosphere, first green shoots emerging, golden morning light, happy expression, cartoon animation style, cinematic composition, detailed forest environment, soft colors, high detail",
            "video_prompt": "Bear walks carefully through forest on melting snow path, stops to sniff the air deeply, closes eyes in joy, small forest bird flies past or calls, bear smiles warmly, camera follows from side angle, smooth natural walking motion, warm golden light, peaceful forest awakening mood, 4-5 seconds",
            "character": "Mishka (Bear)",
            "background": "Forest Path - Spring Melting",
            "music_note": "Bird calls, forest awakening, soft orchestral music theme",
            "status": "pending",
        },
        {
            "id": "S1_K5",
            "name": "Мишка у ручья с водой",
            "duration": 9,
            "timecode": "0:28–0:38",
            "description": "Он замечает маленький серебристый поток, который бежит быстрее обычного. Он подходит к воде и видит, как она течёт. Похоже, лес ожил.",
            "image_prompt": "young brown bear kneeling by crystal clear spring stream, water flowing fast with melting snow, warm golden sunlight reflecting on water, lush green forest, bear's expression full of wonder and joy, detailed spring forest environment, cartoon animation style, cinematic lighting, warm tones",
            "video_prompt": "Bear approaches small stream, kneels down carefully watching water flow rapidly, dips paw gently in water, splashes playfully, looks up amazed at the rushing water, camera shows wide shot of spring forest coming alive, light beams through trees, bear's joyful expression, smooth motion, cinematic framing, 4-5 seconds",
            "character": "Mishka (Bear)",
            "background": "Forest Stream - Spring Water Flow",
            "music_note": "Rushing water, bird songs intensifying, music building",
            "status": "pending",
        },
        {
            "id": "S1_K6",
            "name": "Финал сцены: Мишка поднимает голову к солнцу",
            "duration": 8,
            "timecode": "0:38–0:45",
            "description": "Мишка поднимает голову к солнцу. Он понимает: 'Весна пришла.' Финальный момент сцены с максимальным светом.",
            "image_prompt": "young brown bear standing with raised head looking at golden sunrise sun, forest background full of spring light, warm colors, expression of realization and joy, majestic forest landscape, cinematic wide shot, golden hour lighting, cartoon animation style, triumph moment, highly detailed",
            "video_prompt": "Bear slowly raises head toward rising sun, stands up tall with paws spread, warm golden light floods forest, realization spreads across bear's face, transitions to joy and understanding, camera pulls back to show vast spring forest coming alive, music swells, cinematic moment of triumph and awakening, smooth camera movement, 4-5 seconds",
            "character": "Mishka (Bear)",
            "background": "Forest - Full Spring Sunrise",
            "music_note": "Music theme crescendo, birds chorus, forest full of life",
            "status": "pending",
        },
    ],
}

# ============================================================================
# СЦЕНА 2: "ПЕРВЫЕ ШАГИ В СВЕТЛОМ ЛЕСУ" (0:45–1:30)
# ============================================================================

SCENE_2 = {
    "name": "Первые шаги в светлом лесу",
    "duration": 45,
    "shots": [
        {
            "id": "S2_K1",
            "name": "Лес становится ярче, зелёные ростки",
            "duration": 10,
            "timecode": "0:45–0:55",
            "description": "Мишка идет по тропинке. Лес становится ярче. Под снегом появляются первые зелёные ростки. Далеко слышен шум ручья.",
            "image_prompt": "young brown bear walking through spring forest with melting snow, first green shoots and flowers emerging everywhere, bright warm sunlight, forest details rich with life, animated motion, cartoon style, cinematic composition, magical spring awakening, vibrant but soft colors, high detail",
            "video_prompt": "Bear walks deeper into forest, camera follows from behind, sunlight gets brighter, first flowers and green shoots visible through melting snow, distant sound of rushing water, forest transitions from winter to spring visually, rich detailed environment, smooth camera follow, natural walking pace, 4-5 seconds",
            "character": "Mishka (Bear)",
            "background": "Forest - Deep Path - Spring Transition",
            "music_note": "Water sounds growing, more birds, music tempo increasing",
            "status": "pending",
        },
        {
            "id": "S2_K2",
            "name": "Следы на снегу, Мишка замечает",
            "duration": 10,
            "timecode": "0:55–1:05",
            "description": "Мишка замечает маленький след на снегу. Идёт по следам. Он останавливается. Из кустов выходит лисичка или зайчик, который выглядит обеспокоенным.",
            "image_prompt": "young brown bear examining small animal tracks in melting snow, curious focused expression, small paw prints visible, warm spring forest background, detailed close-up of snow and tracks, cinematic lighting, cartoon animation style, mysterious curious mood, high detail",
            "video_prompt": "Bear spots small animal tracks in snow, kneels down to investigate, gently touches tracks with paw, follows tracks carefully, suspenseful music note, camera close to snow showing details, bear's curious expression, stops as small animal (fox or rabbit) appears from bushes looking scared or curious, smooth cinematic motion, 4-5 seconds",
            "character": "Mishka (Bear)",
            "secondary_character": "Small Animal (Fox or Rabbit) - Appears at end",
            "background": "Forest Path - Snow Tracks",
            "music_note": "Mystery music builds, animals sounds",
            "status": "pending",
        },
        {
            "id": "S2_K3",
            "name": "Встреча с маленьким зверьком",
            "duration": 10,
            "timecode": "1:05–1:15",
            "description": "Лисичка или зайчик выходит из кустов. Мишка пытается понять, что случилось. Внизу видит маленького птенца или что-то заблудившееся.",
            "image_prompt": "young brown bear meeting small scared animal (red fox kit or rabbit), forest glade, first spring flowers blooming, warm sunlight, gentle interaction, cartoon animation style, emotional warm moment, detailed forest glade, soft colors, cinematic composition, high detail",
            "video_prompt": "Small animal appears from bushes looking scared or confused, bear makes gentle approach, shows non-threatening body language, they look at each other, bear notices something small on ground (baby bird or small creature), bear's protective caring instincts activate, gentle music, emotional moment, smooth character interaction animation, soft golden light, 4-5 seconds",
            "character": "Mishka (Bear)",
            "secondary_character": "Small Forest Animal (Fox Kit or Rabbit) and Baby Creature",
            "background": "Forest Glade - Spring Flowers",
            "music_note": "Tender emotional music, nature sounds, minimal dialogue sounds",
            "status": "pending",
        },
        {
            "id": "S2_K4",
            "name": "Мишка помогает маленькому зверьку",
            "duration": 10,
            "timecode": "1:15–1:25",
            "description": "Мишка осторожно помогает маленькому зверьку выбраться из сугроба или найти дорогу. Лес вокруг наполняется теплом. В кадре много мягкого света, капель воды, зелёных тонов.",
            "image_prompt": "young brown bear gently helping small animal, protective caring pose, forest glade filled with spring flowers and green shoots, warm golden sunlight beams, water droplets sparkling, rich spring forest detail, emotional heartwarming moment, cartoon animation style, cinematic composition, soft warm color palette, high detail",
            "video_prompt": "Bear gently helps small creature out of snow or to safety, uses big paws carefully, small animal looks grateful or relieved, warm light increases, camera shows forest coming alive with spring, flowers blooming in time-lapse effect, water droplets catch sunlight, emotional caring animation, smooth helping motion, warm music swells, cinematic nature detail shots, 4-5 seconds",
            "character": "Mishka (Bear)",
            "secondary_character": "Small Forest Animal (Fox Kit or Rabbit) and Baby Creature",
            "background": "Forest Glade - Full Spring Bloom",
            "music_note": "Music reaches tender emotional peak, nature symphony",
            "status": "pending",
        },
        {
            "id": "S2_K5",
            "name": "Финал: Мишка смотрит в камеру",
            "duration": 5,
            "timecode": "1:25–1:30",
            "description": "Кадр на Мишку, смотрящего в камеру. Он улыбается. Солнце выше, лес оживает. Финальный кадр пилота.",
            "image_prompt": "young brown bear smiling warmly at camera, surrounded by vibrant spring forest in full bloom, golden bright sunlight, forest animals visible in background, happy peaceful expression, majestic spring landscape, cinematic close-up, cartoon animation style, triumphant joyful mood, beautiful warm colors, high detail",
            "video_prompt": "Bear turns toward camera with warm genuine smile, holds pose looking directly at viewer, camera pushes in slightly, spring forest in full bloom behind, sunlight golden and warm, small animals visible in background also happy, final triumphant moment, music theme concludes beautifully, peaceful joyful ending, smooth final camera move, 3-4 seconds",
            "character": "Mishka (Bear)",
            "background": "Forest - Full Spring Glory",
            "music_note": "Music theme conclusion, triumphant peaceful end",
            "status": "pending",
        },
    ],
}

# ============================================================================
# ПЕРСОНАЖИ
# ============================================================================

CHARACTERS = {
    "Mishka": {
        "id": "mishka_main",
        "name": "Мишка / Mishka",
        "type": "Bear",
        "age": "Young adult",
        "personality": "Kind, curious, protective, slightly clumsy, loves nature",
        "appearance": "Soft brown fur, round gentle face, big kind eyes, large paws, expressive",
        "style": "Cartoon - soft 2D/3D hybrid",
        "key_prompts": [
            "young brown bear, cartoon style, soft fur, round face, big kind eyes, large paws, warm brown honey colors, friendly expressive, cinematic lighting, high detail, clean animation shapes",
            "brown bear sleeping peacefully in cozy den, soft fur details, gentle face, warm golden morning light, cartoon animation ready",
            "brown bear stretching and yawning, full body motion, happy wake-up animation, warm colors",
            "brown bear walking through forest, natural gait, curious expression, dynamic motion",
            "brown bear kneeling by stream, wonder-struck expression, water reflections, cinematic",
            "brown bear standing tall with head raised, triumphant joyful expression, golden sunlight",
            "brown bear helping small creature gently, caring protective pose, warm light",
            "brown bear smiling directly at camera, warm genuine happy expression, forest background",
        ],
        "status": "ready_for_generation",
    },
    "Small_Animal": {
        "id": "small_animal",
        "name": "Маленький зверёк / Small Animal",
        "type": "Fox Kit or Rabbit",
        "appearance": "Red fox kit or rabbit, small scared but curious",
        "style": "Cartoon - matching main character style",
        "key_prompts": [
            "small cute red fox kit, cartoon style, scared curious expression, soft fur, detailed face, forest setting, cinematic lighting",
            "small cute rabbit or fox emerging from bushes, cautious expression, spring forest, detailed animation style",
        ],
        "status": "ready_for_generation",
    },
}

# ============================================================================
# ЛОКАЦИИ / ФОНЫ
# ============================================================================

BACKGROUNDS = {
    "Forest_Winter_Dawn": {
        "id": "bg_forest_winter_dawn",
        "name": "Лес зимой на рассвете",
        "description": "Snowy pine forest at dawn, dark, misty, cold blue tones",
        "prompt": "misty dark pine forest at dawn, snow covered ground and trees, cold blue winter light, fog and mist thick, bear den barely visible, cinematic wide landscape shot, detailed forest environment, magical misty atmosphere, no animals or characters",
        "status": "pending",
    },
    "Bear_Den_Interior": {
        "id": "bg_bear_den",
        "name": "Берлога медведя изнутри",
        "description": "Cozy bear den interior, warm lighting from outside",
        "prompt": "cozy warm bear den interior, wooden logs and earth walls, golden morning light coming from entrance, soft comfortable den, no bear, cinematic interior lighting, detailed den environment, welcoming warm atmosphere",
        "status": "pending",
    },
    "Forest_Den_Entrance": {
        "id": "bg_forest_den_entrance",
        "name": "Вход из берлоги в лес",
        "description": "Forest at den entrance, spring transition",
        "prompt": "forest den entrance at spring dawn, melting snow, first green shoots, golden morning light breaking through trees, transition from winter to spring visible, detailed forest environment, cinematic landscape composition, magical spring beginning",
        "status": "pending",
    },
    "Forest_Path_Spring": {
        "id": "bg_forest_path_spring",
        "name": "Лесная тропа весной",
        "description": "Deep forest path with spring awakening",
        "prompt": "forest path winding through spring forest, melting snow, first flowers and green shoots everywhere, golden warm sunlight through trees, vibrant awakening nature, detailed forest flora, cinematic composition, rich spring colors, magical spring atmosphere",
        "status": "pending",
    },
    "Forest_Stream": {
        "id": "bg_forest_stream",
        "name": "Лесной ручей",
        "description": "Crystal clear spring stream with flowing water",
        "prompt": "clear spring stream flowing fast from melting snow, crystal water reflecting golden sunlight, smooth river rocks, lush green forest around, detailed water effects, cinematic landscape, peaceful spring water sounds, magical fresh water environment",
        "status": "pending",
    },
    "Forest_Glade_Spring_Bloom": {
        "id": "bg_forest_glade_bloom",
        "name": "Лесная поляна в полном цветении",
        "description": "Forest glade with spring in full bloom",
        "prompt": "beautiful forest glade full of spring flowers blooming, green shoots, golden warm sunlight beams through trees, water droplets sparkling, rich detailed spring flora, butterflies and birds in air, cinematic magical landscape, vibrant warm spring colors, peaceful nature symphony feeling",
        "status": "pending",
    },
}

# ============================================================================
# ШАГИ ГЕНЕРАЦИИ В ПОРЯДКЕ
# ============================================================================

GENERATION_WORKFLOW = [
    {
        "step": 1,
        "name": "Generate Background Images",
        "priority": "HIGH",
        "items": [
            "Forest_Winter_Dawn",
            "Bear_Den_Interior",
            "Forest_Den_Entrance",
            "Forest_Path_Spring",
            "Forest_Stream",
            "Forest_Glade_Spring_Bloom",
        ],
    },
    {
        "step": 2,
        "name": "Generate Main Character - Mishka (Multiple Angles/Expressions)",
        "priority": "HIGH",
        "items": [
            ("Mishka", "sleeping in den"),
            ("Mishka", "waking up stretching"),
            ("Mishka", "exiting den"),
            ("Mishka", "walking"),
            ("Mishka", "at stream surprised"),
            ("Mishka", "head raised to sun"),
            ("Mishka", "helping small animal"),
            ("Mishka", "smiling at camera"),
        ],
    },
    {
        "step": 3,
        "name": "Generate Secondary Characters",
        "priority": "MEDIUM",
        "items": [
            ("Small_Animal", "scared from bushes"),
            ("Small_Animal", "grateful to bear"),
        ],
    },
    {
        "step": 4,
        "name": "Generate Video Sequences - Scene 1",
        "priority": "HIGH",
        "items": [
            ("S1_K1", "Forest dawn panning"),
            ("S1_K2", "Bear waking in den"),
            ("S1_K3", "Bear exiting den"),
            ("S1_K4", "Bear walking forest path"),
            ("S1_K5", "Bear at stream"),
            ("S1_K6", "Bear looking at sun"),
        ],
    },
    {
        "step": 5,
        "name": "Generate Video Sequences - Scene 2",
        "priority": "HIGH",
        "items": [
            ("S2_K1", "Walking through spring forest"),
            ("S2_K2", "Finding tracks in snow"),
            ("S2_K3", "Meeting small animal"),
            ("S2_K4", "Helping small creature"),
            ("S2_K5", "Final camera shot smiling"),
        ],
    },
    {
        "step": 6,
        "name": "Compile Video Sequences",
        "priority": "HIGH",
        "items": [
            "Scene 1 - Full (45 seconds)",
            "Scene 2 - Full (45 seconds)",
            "Pilot - Full (90 seconds)",
        ],
    },
    {
        "step": 7,
        "name": "Add Audio & Music",
        "priority": "MEDIUM",
        "items": [
            "Forest ambience track",
            "Birds and nature sounds",
            "Background music theme",
            "Sound effects (footsteps, water, wind)",
        ],
    },
    {
        "step": 8,
        "name": "Final Render & Export",
        "priority": "HIGH",
        "items": [
            "Pilot video 1920x1080 @24fps",
            "Pilot video promotional cut 30sec",
        ],
    },
]

# ============================================================================
# СВОДКА ДЛЯ ГЕНЕРАЦИИ
# ============================================================================

GENERATION_SUMMARY = """
МУЛЬТИК "МИШКА И ПЕРВЫЙ СВЕТ" — ПИЛОТНЫЙ ПРОЕКТ
===================================================

ОБЩАЯ ИНФОРМАЦИЯ:
- Название: Мишка и первый свет
- Тип: Пилотный пилот (2 первые сцены)
- Длительность: ~1:30 минуты
- Стиль: Мягкий 2D/3D гибрид cartoon, теплые лесные цвета
- Целевая аудитория: Семейный мультфильм

СОДЕРЖАНИЕ:
- Сцена 1 (0:00–0:45): "Пробуждение леса" — Мишка просыпается после зимней спячки, выходит из берлоги, начинает открывать весну
- Сцена 2 (0:45–1:30): "Первые шаги в светлом лесу" — Мишка идет по лесу, встречает маленького зверька, помогает ему

ПЕРСОНАЖИ:
1. Мишка (главный герой) — молодой добрый медведь, мягкий, выразительный, любит природу
2. Маленький зверёк — лисичка или зайчик, испуганный но благодарный

ЛОКАЦИИ:
- Берлога медведя (зима)
- Лесная тропа (зима → весна переход)
- Ручей (весна)
- Лесная поляна (весна в полном цветении)

ТЕХНИЧЕСКИЕ СПЕЦИФИКАЦИИ:
- Разрешение: 1920x1080
- FPS: 24 fps
- Стиль анимации: Smooth cinematic cartoon
- Длина одного видео-клипа: 3-5 секунд (для оптимальной генерации Runway)
- Всего клипов: 10 видео-секвенций

СЛЕДУЮЩИЙ ШАГ:
1. Запустить скрипт для генерации всех изображений и видео
2. Проверить качество каждого клипа
3. Собрать финальный монтаж с музыкой и звуком
"""

print(GENERATION_SUMMARY)
