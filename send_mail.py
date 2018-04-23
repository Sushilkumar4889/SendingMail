import smtplib, time
server = smtplib.SMTP('smtp.gmail.com',587)
print("Opening Gmail")
time.sleep(1)
server.starttls()
print('Security Initiazed...')
time.sleep(1)
server.login("sushil.kumar4889@gmail.com","type your password here")
abc="Logging in"
print("Logging in")
for i in range(0,8):
    print(".",end=(''))
    time.sleep(0.5)
time.sleep(2)
msg = "Hi, This is my first python program"
server.sendmail('sushil.kumar4889@gmail.com','theashwanisingla@gmail.com',msg)
print("Sending Mail...")
time.sleep(2)
print('Mail sent successfully')
server.quit()
print("Auto Logged Out")
