import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = 'gayatri.rasberrypi@gmail.com'
toaddr = 'gayatri.rasberrypi@gmail.com'
msg = MIMEMultipart()
msg['gayatri.rasberrypi@gmail.com'] = fromaddr
msg['gayatri.rasberrypi@gmail.com'] = toaddr
msg['Subject'] = "This is a trial mail"
body = 'Message from gayatri'
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

print 'sending email'
server.login(fromaddr,"rasberrypi#08")

text = msg.as_string()

server.sendmail(fromaddr,toaddr,text)
server.quit()
print ' sent !!!'
