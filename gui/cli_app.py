import os
import subprocess

LOGS_DIR = "../logs"

def list_logs():
    logs = [f for f in os.listdir(LOGS_DIR) if f.endswith(".log")]
    for idx, log in enumerate(logs, start=1):
        print(f"{idx}. {log}")
    return logs

def view_log():
    logs = list_logs()
    choice = input("Qaysi logni ko‘rmoqchisiz (raqam bilan): ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(logs):
            log_path = os.path.join(LOGS_DIR, logs[idx])
            with open(log_path, "r") as f:
                print(f.read())
        else:
            print("Noto‘g‘ri raqam.")
    except Exception as e:
        print(f"Xatolik: {e}")

def send_test_email():
    # Parallel scriptni chaqiramiz
    subprocess.run(["python3", "../project_parallel.py"])

def main():
    while True:
        print("\n=== Project CLI Menu ===")
        print("1. Test email yuborish")
        print("2. Loglarni ko‘rish")
        print("3. Chiqish")
        choice = input("Tanlang (1-3): ")

        if choice == "1":
            send_test_email()
            print("✅ Test email yuborildi. Natija ../logs/cli_send_email.log faylida.")
        elif choice == "2":
            view_log()
        elif choice == "3":
            break
        else:
            print("Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

if __name__ == "__main__":
    main()
