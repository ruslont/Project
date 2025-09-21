import requests

def main():
    try:
        response = requests.get("https://httpbin.org/get")
        with open("logs/test_request.log", "w") as log_file:
            log_file.write(response.text)
        print("✅ Test muvaffaqiyatli bajarildi. Natija logs/test_request.log ichida.")
    except Exception as e:
        with open("logs/test_request_error.log", "w") as log_file:
            log_file.write(str(e))
        print("❌ Xatolik yuz berdi. logs/test_request_error.log faylini tekshiring.")

if __name__ == "__main__":
    main()
