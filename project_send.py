import asyncio
import aiohttp
import os

COOKIE = "sessionid=your-session-id"
URL = "https://httpbin.org/post"

async def send_email(session, subject, body="This is a test email"):
    data = {"subject": subject, "body": body}
    
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    log_path = f"logs/{subject.replace(' ', '_')}.log"
    
    try:
        async with session.post(URL, data=data, headers={"Cookie": COOKIE}, timeout=10) as resp:
            text = await resp.text()
            with open(log_path, "w") as f:
                f.write(text)
            print(f"{subject} {resp.status}")
    except Exception as e:
        error_path = f"logs/{subject.replace(' ', '_')}_error.log"
        with open(error_path, "w") as f:
            f.write(str(e))
        print(f"{subject} Error")

async def main():
    subjects = [line.strip() for line in open("subjects.txt", encoding="utf-8") if line.strip()]
    async with aiohttp.ClientSession() as session:
        tasks = [send_email(session, subject) for subject in subjects]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
