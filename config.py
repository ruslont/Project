import os

# Asosiy papka
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Fayllar
SUBJECTS_FILE = os.path.join(BASE_DIR, "subjects.txt")
PROXY_FILE = os.path.join(BASE_DIR, "proxy.txt")

# Loglar uchun papka
LOGS_DIR = os.path.join(BASE_DIR, "..", "logs")
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOG_FILE = os.path.join(LOGS_DIR, "cli_send_email.log")

# Email sozlamalar (keyinchalik mijoz POST / SMTP ni tanlaydi)
EMAIL_SETTINGS = {
    "use_smtp": True,  # Agar POST kerak bo‘lsa, False qilinadi
    "smtp_server": "smtp.mail.ru",
    "smtp_port": 587,
    "username": "user@mail.ru",
    "password": "parolni_bu_yerga_yozing"
}

# Test uchun qabul qiluvchi email
TEST_RECEIVER = "receiver@mail.ru"
