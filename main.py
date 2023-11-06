from email.message import EmailMessage
from credentials import sender, password, reciever
import ssl
import smtplib
# set up 2fa and generate app password
# specify all the things you need for the email, sender, password, receiver and subject
email_sender = sender
email_password = password

email_reciever = reciever

subject = "Don't forget to subscribe"
body = """
When you watch LegendintheGaming streams, don't foprget to follow and subscribe
"""
# use the EmailMessage library to construct the email
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
