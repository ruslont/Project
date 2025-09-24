import asyncio
from project_parallel import send_email

async def main():
    while True:
        print("\n=== Меню рассылки ===")
        print("1. Отправить тестовое письмо")
        print("2. Выход")
        choice = input("Выберите (1-2): ")

        if choice == "1":
            recipient = input("Введите email получателя: ")
            subject = input("Введите тему письма (Subject): ")
            body = input("Введите текст письма: ")
            await send_email(recipient, subject, body)
            print("✅ Письмо успешно отправлено!")
        elif choice == "2":
            print("Выход из программы...")
            break
        else:
            print("❌ Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    asyncio.run(main())
