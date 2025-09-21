import asyncio
import aiohttp
import tkinter as tk
from tkinter import filedialog, scrolledtext
import os

# Globals
subjects = []
cookies = {"session": "your_cookie_value"}
url = "https://httpbin.org/post"
tasks = []
stop_flag = False

# Async send function
async def send_email(session, subject, log_widget):
    global stop_flag
    if stop_flag:
        return
    data = {
        "to": "test@example.com",
        "subject": subject,
        "body": f"This is email with subject: {subject}"
    }
    try:
        async with session.post(url, cookies=cookies, data=data) as resp:
            text = await resp.text()
            log_widget.insert(tk.END, f"{subject} -> {resp.status}\n")
            log_widget.see(tk.END)
            if not os.path.exists("logs"):
                os.makedirs("logs")
            with open(f"logs/{subject}.log", "w") as log_file:
                log_file.write(text)
    except Exception as e:
        log_widget.insert(tk.END, f"{subject} -> Error: {e}\n")
        log_widget.see(tk.END)

# Start sending
def start_sending(log_widget):
    global tasks, stop_flag
    stop_flag = False
    async def main():
        async with aiohttp.ClientSession() as session:
            task_list = [send_email(session, subj, log_widget) for subj in subjects]
            await asyncio.gather(*task_list)
    tasks = asyncio.run(main())

# Stop sending
def stop_sending():
    global stop_flag
    stop_flag = True

# Import subjects
def import_subjects(log_widget):
    global subjects
    file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            subjects = [line.strip() for line in f if line.strip()]
        log_widget.insert(tk.END, f"Imported {len(subjects)} subjects.\n")
        log_widget.see(tk.END)

# GUI
root = tk.Tk()
root.title("Minimal Email Sender")
root.geometry("500x400")

btn_import = tk.Button(root, text="Import Subjects", command=lambda: import_subjects(log_box))
btn_import.pack(pady=5)

btn_start = tk.Button(root, text="Start Sending", command=lambda: start_sending(log_box))
btn_start.pack(pady=5)

btn_stop = tk.Button(root, text="Stop Sending", command=stop_sending)
btn_stop.pack(pady=5)

log_box = scrolledtext.ScrolledText(root, width=60, height=20)
log_box.pack(pady=10)

root.mainloop()
