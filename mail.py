import smtplib
import ssl
from email.message import EmailMessage

def sendMail(name,tomail,body):
    # Define email sender and receiver
    email_sender = 'dummy.python10@gmail.com'
    email_password = 'awjhkdqtopyxqkda'
    email_receiver = tomail

    # Set the subject and body of the email
    subject1 = 'Thanks for Reaching me....'
    body1 = """
        I am chandra kiran.Java and Python developer. 
    Thanks for reaching me.I will contact you shortly…
    """

    subject2 = "Mail from Client "+name
    body2 = "Client Email:"+tomail+"\n" + body
    finalMail(email_sender,email_receiver,subject1,body1,email_password)
    finalMail(email_sender,"jinkachandrakiran2002@gmail.com" , subject2, body2, email_password)
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