import smtplib
import ssl
from email.message import EmailMessage

def sendMail(tomail):
    # Define email sender and receiver
    email_sender = 'dummy.python10@gmail.com'
    email_password = 'awjhkdqtopyxqkda'
    email_receiver = tomail

    # Set the subject and body of the email
    subject = 'thanks'
    body = """
    Thanks for contacting me..... 
    I will 
    """
    finalMail(email_sender,email_receiver,subject,body,email_password)
def finalMail(email_sender,email_receiver,subject,body,email_password):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())