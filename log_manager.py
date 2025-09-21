import os
from datetime import datetime

# Loglar saqlanadigan papka
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "send_email.log")


def write_log(message: str):
    """
    Log faylga yozish
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def read_log():
    """
    Log fayldan oxirgi yozuvlarni o‘qish
    """
    if not os.path.exists(LOG_FILE):
        return "Log fayli topilmadi."

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()
