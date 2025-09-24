# gui/gui_app.py
import tkinter as tk
from tkinter import messagebox
import asyncio
from project_parallel import send_email

def send_mail_gui():
    recipient = entry_to.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)

    if not recipient or not subject or not body.strip():
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return

    asyncio.run(send_email(recipient, subject, body))
    messagebox.showinfo("Успех", "Письмо успешно отправлено!")

root = tk.Tk()
root.title("Email Рассылка")

tk.Label(root, text="Получатель (To):").pack()
entry_to = tk.Entry(root, width=40)
entry_to.pack()

tk.Label(root, text="Тема письма (Subject):").pack()
entry_subject = tk.Entry(root, width=40)
entry_subject.pack()

tk.Label(root, text="Текст письма:").pack()
text_body = tk.Text(root, width=50, height=10)
text_body.pack()

tk.Button(root, text="Отправить", command=send_mail_gui).pack(pady=10)

root.mainloop()
