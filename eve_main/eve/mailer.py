import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(to, message, subject="'SOS ALERT - EVE'"):
    
    mail_content = message
    
    sender_address = 'progsdproject@gmail.com'
    sender_pass = 'nnuricwsrdrtoeuv'
    
    receiver_address = to
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    
    session.login(sender_address, sender_pass)
    text = message.as_string()
    
    session.sendmail(sender_address, receiver_address, text)
    
    session.quit()

    return 1