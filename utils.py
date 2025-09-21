# utils.py
import os
import datetime
from config import LOGS_DIR

# Log papkasini avtomatik yaratib qo‘yish
os.makedirs(LOGS_DIR, exist_ok=True)

def log_response(subject: str, response_text: str, error: bool = False):
    """
    Javob yoki xatolikni log faylga yozib qo‘yish.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_subject = subject.replace(" ", "_")

    if error:
        filename = f"{safe_subject}_error.log"
    else:
        filename = f"{safe_subject}.log"

    filepath = os.path.join(LOGS_DIR, filename)

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"\n--- {timestamp} ---\n")
        f.write(response_text + "\n")

def read_logs():
    """
    Log papkasidagi barcha fayllarni ko‘rsatish.
    """
    files = os.listdir(LOGS_DIR)
    return files
