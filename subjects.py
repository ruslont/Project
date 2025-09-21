# subjects.py

def load_subjects(filename="subjects.txt"):
    """
    subjects.txt faylidan mavzularni o‘qib olish.
    Har bir qatorda bitta subject bo‘ladi.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            subjects = [line.strip() for line in f if line.strip()]
        return subjects
    except FileNotFoundError:
        # Agar subjects.txt mavjud bo‘lmasa, default subject qaytaradi
        return ["Default Subject"]

def save_subjects(subjects, filename="subjects.txt"):
    """
    Yangi mavzularni subjects.txt fayliga yozish.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for subject in subjects:
            f.write(subject + "\n")
