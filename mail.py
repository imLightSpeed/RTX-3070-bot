import smtplib
import os
from email.message import EmailMessage
class mail:
    def send_mail(self,store, card):
        self.store = store
        self.card = card
        EMAIL_USER = os.environ.get('EMAIL_USER')
        EMAIL_PASS = os.environ.get('EMAIL_PASS')
        msg = EmailMessage()
        msg['Subject'] = 'RTX 3070 IN STOCK'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_USER
        msg.set_content(f'GET OVER TO {self.store}, {self.card} IS IN STOCK NOW')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)


