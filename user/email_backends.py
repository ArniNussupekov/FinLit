# myproject/email_backends.py
import ssl
from smtplib import SMTP_SSL
from django.core.mail.backends.smtp import EmailBackend


class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            # Создаем объект SMTP_SSL с отключенной проверкой сертификата
            self.connection = SMTP_SSL(self.host, self.port, timeout=self.timeout, context=ssl._create_unverified_context())
            # Устанавливаем логин и пароль
            self.connection.login(self.username, self.password)
        except Exception:
            if not self.fail_silently:
                raise
        return True
