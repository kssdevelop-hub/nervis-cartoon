# Настройка генерации мультфильмов с Runway AI

## 📋 Шаги установки

### 1. Получение API ключа ✅ (вы это уже сделали)

API ключ получен с https://dev.runway.com/organization/56c9c1b3-1640-45bc-8004-291c3674b51f/api-keys

### 2. Добавление API ключа в .env файл

Откройте файл `.env` в корне проекта и замените:

```dotenv
RUNWAY_API_KEY=your_api_key_here
```

На:

```dotenv
RUNWAY_API_KEY=ваш_реальный_api_ключ
```

⚠️ **Важно**: Не делитесь этим ключом! Добавьте `.env` в `.gitignore`

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

Это установит:
- `requests` - для HTTP запросов к Runway API
- `python-dotenv` - для загрузки переменных из .env
- `Pillow` - для обработки изображений
- `moviepy` - для работы с видео

### 4. Структура проекта

```
nervis-cartoon/
├── .env                      # ваш API ключ (НИКОМУ НЕ ПОКАЗЫВАТЬ!)
├── .env.example             # пример переменных (можно в репо)
├── config.py                # конфигурация приложения
├── runway_client.py         # клиент для работы с API
├── cartoon_generator.py     # основной генератор
├── requirements.txt         # зависимости
├── output_videos/           # сгенерированные видео (создается автоматически)
├── temp/                    # временные файлы (создается автоматически)
└── input_images/            # исходные изображения (создается автоматически)
```

## 🚀 Использование

### Быстрый старт - простая генерация

```python
from cartoon_generator import CartoonGenerator

# Инициализируем генератор
generator = CartoonGenerator()

# Генерируем одну сцену
video_path = generator.generate_cartoon_scene(
    scene_description="A cute puppy playing with a ball in the park",
    duration=10,
    scene_name="puppy_play"
)

print(f"Видео сохранено: {video_path}")
```

### Генерация нескольких сцен

```python
from cartoon_generator import CartoonGenerator

generator = CartoonGenerator()

scenes = [
    {
        "description": "Котенок просыпается в уютной комнате",
        "duration": 5,
        "name": "kitten_wake_up"
    },
    {
        "description": "Котенок пьет молоко из блюдца",
        "duration": 5,
        "name": "kitten_milk"
    },
    {
        "description": "Котенок играет с клубком ниток",
        "duration": 8,
        "name": "kitten_play"
    }
]

videos = generator.generate_multiple_scenes(scenes)
print(f"Создано видео: {len(videos)}")
```

## ⚙️ Параметры конфигурации

В файле `config.py` можно настроить:

```python
GENERATION_MODEL = "gen3"           # Модель генерации
GENERATION_RESOLUTION = "1920x1080" # Разрешение видео
GENERATION_DURATION = 10            # Длительность по умолчанию (сек)
GENERATION_FPS = 24                 # Кадров в секунду
MAX_VIDEO_DURATION = 30             # Максимальная длительность
```

## 📊 Статусы генерации

При генерации видео возможны следующие статусы:

- **QUEUED** - задача в очереди
- **RUNNING** - идет генерация
- **SUCCEEDED** - генерация завершена успешно ✅
- **FAILED** - ошибка при генерации ❌

Клиент автоматически проверяет статус каждые 10 секунд.

## 🛠️ Методы API клиента

### `RunwayClient`

```python
# Генерация видео
generate_video(prompt, duration, resolution, model)
↓
# Получение статуса
get_task_status(task_id)
↓
# Ожидание завершения
wait_for_completion(task_id, max_wait_time, check_interval)
↓
# Скачивание видео
download_video(output_url, save_path)
```

## 🐛 Решение проблем

### Ошибка: "RUNWAY_API_KEY не установлен"

**Решение**: Проверьте что файл `.env` создан в корне проекта и содержит правильный API ключ

### Ошибка: "401 Unauthorized"

**Решение**: API ключ неверный или истек. Получите новый ключ с https://dev.runway.com/

### Генерация долго ждет

**Решение**: Это нормально! Генерация видео может занять несколько минут. Клиент будет ждать.

### Видео не скачивается

**Решение**: Проверьте что:
- Папка `output_videos/` существует
- У вас достаточно места на диске
- Интернет соединение стабильно

## 📝 Примеры описаний сцен

Для лучших результатов используйте детальные описания:

```python
# ✅ Хорошо
"A happy little bunny with long ears hopping through a sunny meadow full of colorful flowers"

# ❌ Плохо
"Rabbit"
```

На английском языке результаты обычно лучше, но можно писать и на русском.

## 📚 Документация Runway API

https://docs.runwayml.com/

## 🔐 Безопасность

- **Никогда** не коммитьте файл `.env` в репозиторий
- Используйте `.env.example` как шаблон для других разработчиков
- Регулярно обновляйте API ключ в консоли Runway

## ✅ Проверка работы

Запустите этот тест:

```python
from config import config
from runway_client import RunwayClient

# Проверка конфигурации
try:
    config.validate()
    print("✅ Конфигурация OK")
except Exception as e:
    print(f"❌ Ошибка конфигурации: {e}")

# Проверка подключения к API
try:
    client = RunwayClient()
    tasks = client.list_tasks(limit=1)
    print("✅ API подключение OK")
except Exception as e:
    print(f"❌ Ошибка API: {e}")
```

## 🎬 Следующие шаги

1. Добавьте API ключ в `.env`
2. Запустите `pip install -r requirements.txt`
3. Протестируйте генерацию одной сцены
4. Создавайте мультфильмы! 🎨
