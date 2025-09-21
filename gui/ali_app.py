import os

LOG_DIR = "../logs"

def show_menu():
    print("\n=== Project CLI Menu ===")
    print("1. Test email yuborish")
    print("2. Loglarni ko‘rish")
    print("3. Chiqish")

def send_test_email():
    log_file = os.path.join(LOG_DIR, "cli_send_email.log")
    with open(log_file, "w") as f:
        f.write("✅ Test email muvaffaqiyatli yuborildi!\n")
    print(f"✅ Test email yuborildi. Natija {log_file} faylida.")

def view_logs():
    if not os.path.exists(LOG_DIR):
        print("❌ Log katalogi topilmadi.")
        return

    files = os.listdir(LOG_DIR)
    if not files:
        print("❌ Hozircha log fayllar mavjud emas.")
        return

    print("\n=== Log fayllar ===")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")

    try:
        choice = int(input("\nLog faylini tanlang (raqam): "))
        if 1 <= choice <= len(files):
            file_path = os.path.join(LOG_DIR, files[choice - 1])
            print(f"\n📄 {files[choice - 1]} ichidagi ma’lumot:\n")
            with open(file_path, "r") as f:
                print(f.read())
        else:
            print("❌ Noto‘g‘ri tanlov.")
    except ValueError:
        print("❌ Raqam kiriting.")

def main():
    while True:
        show_menu()
        choice = input("Tanlang (1-3): ")
        if choice == "1":
            send_test_email()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    main()
