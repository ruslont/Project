import requests
import json
import os

def main():
    os.makedirs("logs", exist_ok=True)  # logs papkasi borligini tekshiradi
    url = "https://httpbin.org/post"
    data = {"name": "Suhrob", "project": "Test POST request"}

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()

        with open("logs/test_post_request.log", "w") as log_file:
            log_file.write(json.dumps(response.json(), indent=2, ensure_ascii=False))

        print("✅ POST so‘rov muvaffaqiyatli yuborildi. Natija logs/test_post_request.log ichida.")

    except Exception as e:
        with open("logs/test_post_request_error.log", "w") as log_file:
            log_file.write(str(e))
        print("❌ Xatolik yuz berdi. Tafsilotlar logs/test_post_request_error.log ichida.")

if __name__ == "__main__":
    main()
