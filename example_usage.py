"""
Примеры использования генератора мультфильмов
"""
from cartoon_generator import CartoonGenerator
import logging

# Настройка логирования для вывода информации
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def example_1_single_scene():
    """Пример 1: Генерация одной простой сцены"""
    print("\n" + "="*60)
    print("ПРИМЕР 1: Одна простая сцена")
    print("="*60)
    
    generator = CartoonGenerator()
    
    video = generator.generate_cartoon_scene(
        scene_description="A cute baby elephant learning to walk in the savanna",
        duration=10,
        scene_name="baby_elephant"
    )
    
    if video:
        print(f"\n✅ Успешно! Видео сохранено: {video}")
    else:
        print("\n❌ Ошибка при генерации видео")


def example_2_story_scenes():
    """Пример 2: Генерация сцен для мультфильма - историй про животных"""
    print("\n" + "="*60)
    print("ПРИМЕР 2: История про маленькую лису (5 сцен)")
    print("="*60)
    
    generator = CartoonGenerator()
    
    story_scenes = [
        {
            "description": "A small orange fox cub playing in the forest with autumn leaves falling",
            "duration": 8,
            "name": "fox_01_morning"
        },
        {
            "description": "The fox cub discovers a beautiful butterfly and tries to catch it",
            "duration": 6,
            "name": "fox_02_butterfly"
        },
        {
            "description": "The fox cub makes friends with a friendly rabbit in the meadow",
            "duration": 8,
            "name": "fox_03_friendship"
        },
        {
            "description": "They play together running through the sunny field",
            "duration": 7,
            "name": "fox_04_playing"
        },
        {
            "description": "As the sun sets, the fox cub and rabbit say goodbye at the tree",
            "duration": 6,
            "name": "fox_05_sunset"
        }
    ]
    
    videos = generator.generate_multiple_scenes(story_scenes)
    
    print(f"\n✅ История создана!")
    print(f"Всего сцен: {len(videos)}")
    for i, video in enumerate(videos, 1):
        print(f"  {i}. {video}")


def example_3_adventure_story():
    """Пример 3: Приключение маленького путешественника"""
    print("\n" + "="*60)
    print("ПРИМЕР 3: Приключение маленького путешественника (3 сцены)")
    print("="*60)
    
    generator = CartoonGenerator()
    
    adventure_scenes = [
        {
            "description": "A curious little boy starting his adventure, leaving his house with a backpack",
            "duration": 5,
            "name": "adventure_01_start"
        },
        {
            "description": "The boy discovers a mysterious path leading into a magical forest with glowing trees",
            "duration": 8,
            "name": "adventure_02_forest"
        },
        {
            "description": "The boy meets friendly magical creatures and they dance together",
            "duration": 7,
            "name": "adventure_03_friends"
        }
    ]
    
    videos = generator.generate_multiple_scenes(adventure_scenes)
    
    print(f"\n✅ Приключение готово!")
    print(f"Всего видео: {len(videos)}")


def example_4_character_showcase():
    """Пример 4: Демонстрация персонажей"""
    print("\n" + "="*60)
    print("ПРИМЕР 4: Демонстрация персонажей (каждый отдельно)")
    print("="*60)
    
    generator = CartoonGenerator()
    
    characters = [
        {
            "description": "A happy yellow duck swimming in a blue pond with water lilies",
            "duration": 5,
            "name": "character_duck"
        },
        {
            "description": "A sleepy brown bear waking up in a cozy cave",
            "duration": 5,
            "name": "character_bear"
        },
        {
            "description": "A jumping red squirrel collecting acorns in the autumn forest",
            "duration": 5,
            "name": "character_squirrel"
        },
        {
            "description": "A colorful peacock spreading its beautiful feathers",
            "duration": 5,
            "name": "character_peacock"
        }
    ]
    
    videos = generator.generate_multiple_scenes(characters)
    
    print(f"\n✅ Персонажи созданы!")
    print(f"Всего персонажей: {len(videos)}")


def example_5_educational_content():
    """Пример 5: Образовательный контент - что-то новое"""
    print("\n" + "="*60)
    print("ПРИМЕР 5: Образовательный контент - изучение цветов")
    print("="*60)
    
    generator = CartoonGenerator()
    
    educational_scenes = [
        {
            "description": "A cheerful red apple on a white background, rotating slowly",
            "duration": 4,
            "name": "color_red_apple"
        },
        {
            "description": "A bright orange pumpkin with a smile face on a field",
            "duration": 4,
            "name": "color_orange_pumpkin"
        },
        {
            "description": "A yellow sun shining brightly in the blue sky",
            "duration": 4,
            "name": "color_yellow_sun"
        },
        {
            "description": "Green leaves and grass swaying in the wind",
            "duration": 4,
            "name": "color_green_nature"
        },
        {
            "description": "A big blue whale swimming in the ocean",
            "duration": 4,
            "name": "color_blue_whale"
        }
    ]
    
    videos = generator.generate_multiple_scenes(educational_scenes)
    
    print(f"\n✅ Образовательный контент готов!")
    print(f"Всего видео: {len(videos)}")


def example_6_quick_test():
    """Пример 6: Быстрый тест (очень короткое видео)"""
    print("\n" + "="*60)
    print("ПРИМЕР 6: Быстрый тест (короткое видео - 3 сек)")
    print("="*60)
    
    generator = CartoonGenerator()
    
    # Очень короткое видео для быстрого тестирования
    video = generator.generate_cartoon_scene(
        scene_description="A smiling cartoon sun",
        duration=3,
        scene_name="test_sun"
    )
    
    if video:
        print(f"\n✅ Тест пройден! Видео: {video}")
    else:
        print("\n❌ Тест не пройден")


# Главное меню
if __name__ == "__main__":
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ГЕНЕРАТОРА МУЛЬТФИЛЬМОВ".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    print("\nВыберите пример:")
    print("1 - Одна простая сцена")
    print("2 - История про маленькую лису (5 сцен)")
    print("3 - Приключение путешественника (3 сцены)")
    print("4 - Демонстрация персонажей (4 персонажа)")
    print("5 - Образовательный контент (5 цветов)")
    print("6 - Быстрый тест (3 секунды)")
    print("0 - Выход")
    
    choice = input("\nВведите номер (0-6): ").strip()
    
    examples = {
        "1": example_1_single_scene,
        "2": example_2_story_scenes,
        "3": example_3_adventure_story,
        "4": example_4_character_showcase,
        "5": example_5_educational_content,
        "6": example_6_quick_test,
    }
    
    if choice in examples:
        try:
            examples[choice]()
        except KeyboardInterrupt:
            print("\n\n⚠️  Отменено пользователем")
        except Exception as e:
            print(f"\n\n❌ Ошибка: {e}")
    elif choice != "0":
        print("❌ Неверный выбор")
    
    print("\n")
