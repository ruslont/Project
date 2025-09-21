# gui/gui_app.py
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import subprocess
import os

# Loyihaning asosiy papkasi
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_DIR = os.path.join(BASE_DIR, "logs")
PROJECT_PARALLEL = os.path.join(BASE_DIR, "project_parallel.py")

class EmailGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Project Email GUI")
        self.master.geometry("700x500")
        self.master.resizable(False, False)

        # Menu
        menu = tk.Menu(master)
        master.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_command(label="Exit", command=master.quit)

        # Label
        self.label = tk.Label(master, text="Project Email Automation", font=("Arial", 16))
        self.label.pack(pady=10)

        # Buttons
        self.test_email_btn = tk.Button(master, text="Test Email Yuborish", width=25, command=self.test_email)
        self.test_email_btn.pack(pady=10)

        self.show_logs_btn = tk.Button(master, text="Loglarni Ko‘rish", width=25, command=self.show_logs)
        self.show_logs_btn.pack(pady=10)

        self.log_display = scrolledtext.ScrolledText(master, width=80, height=20)
        self.log_display.pack(pady=10)

    def test_email(self):
        """Test email yuborish funksiyasi"""
        try:
            result = subprocess.run(
                ["python3", PROJECT_PARALLEL],
                capture_output=True,
                text=True,
                cwd=BASE_DIR
            )
            messagebox.showinfo("✅ Test Email", "Test email yuborildi. Natija logs/ papkada.")
            self.log_display.delete(1.0, tk.END)
            self.log_display.insert(tk.END, result.stdout)
        except Exception as e:
            messagebox.showerror("❌ Xatolik", str(e))

    def show_logs(self):
        """Log fayllarini tanlab ko‘rsatish"""
        try:
            log_files = [f for f in os.listdir(LOG_DIR) if os.path.isfile(os.path.join(LOG_DIR, f))]
            log_files.sort()
            selected_log = filedialog.askopenfilename(initialdir=LOG_DIR, title="Logni tanlang", filetypes=[("Log Files", "*.log")])
            if selected_log:
                with open(selected_log, "r", encoding="utf-8") as f:
                    content = f.read()
                self.log_display.delete(1.0, tk.END)
                self.log_display.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("❌ Xatolik", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailGUI(root)
    root.mainloop()
