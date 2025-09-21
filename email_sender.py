import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SETTINGS, TEST_RECEIVER


def send_email(subject: str, body: str, receiver: str = TEST_RECEIVER):
    """
    SMTP orqali email yuborish funksiyasi
    """
    try:
        # Yuboruvchi va qabul qiluvchilar
        sender = EMAIL_SETTINGS["username"]

        # Xabarni tayyorlash
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        # SMTP serverga ulanish
        with smtplib.SMTP(EMAIL_SETTINGS["smtp_server"], EMAIL_SETTINGS["smtp_port"]) as server:
            server.starttls()
            server.login(sender, EMAIL_SETTINGS["password"])
            server.sendmail(sender, receiver, msg.as_string())

        print(f"✅ Email yuborildi: {subject}")
        return True

    except Exception as e:
        print(f"❌ Yuborishda xatolik: {e}")
        return False
