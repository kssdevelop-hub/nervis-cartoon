"""
Сценарий генерации короткого детского мультфильма из 3 сцен.
Запуск: python generate_story.py
"""
from cartoon_generator import CartoonGenerator


def main():
    generator = CartoonGenerator()

    story = [
        {
            "name": "scene_01_intro",
            "duration": 8,
            "description": "A cheerful little bunny wakes up in a cozy forest clearing, the sun rises, and soft morning light shines on green grass and flowers."
        },
        {
            "name": "scene_02_adventure",
            "duration": 10,
            "description": "The bunny explores the forest, meets a friendly squirrel, and they chase colorful butterflies together through a magical meadow."
        },
        {
            "name": "scene_03_happy_end",
            "duration": 9,
            "description": "The bunny and squirrel sit under a big tree at sunset, smiling and waving at the camera while the sky turns warm orange and pink."
        }
    ]

    print("Начинаем генерацию короткого мультфильма...")
    result = generator.generate_multiple_scenes(story)

    if result:
        print("\nГотово. Сохраненные файлы:")
        for path in result:
            print(f"- {path}")
    else:
        print("\nГенерация не выполнена. Проверьте RUNWAY_API_KEY и доступность Runway API.")


if __name__ == "__main__":
    main()
