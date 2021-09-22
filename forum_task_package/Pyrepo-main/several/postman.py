import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = ""  # from
mypass = ""  # insertpas
toaddr = ""  # where

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"

body = "Это пробный текст сообщения"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.post service', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
