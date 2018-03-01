import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

print 'sending email'
server.login("gayatri.rasberrypi@gmail.com","rasberrypi#08")
mymsg = 'Message from gayatri'
server.sendmail("gayatri.rasberrypi@gmail.com","Rpi.tests.readings@gmail.com",mymsg)
server.quit()
print ' sent !!!'
