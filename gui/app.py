import tkinter as tk
from tkinter import messagebox
import requests

def test_request():
    url = "https://httpbin.org/get"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            messagebox.showinfo("Natija", "✅ So‘rov muvaffaqiyatli bajarildi")
        else:
            messagebox.showwarning("Natija", f"⚠️ Xatolik kodi: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Xatolik", str(e))

# Tkinter oynasi
root = tk.Tk()
root.title("Project Send - Test GUI")
root.geometry("300x150")

btn = tk.Button(root, text="Test Request", command=test_request, bg="lightblue")
btn.pack(pady=40)

root.mainloop()
