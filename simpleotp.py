#email automation
#otp generation
import random
import math
import smtplib#simple mail transfer protocol library
digit="0123456789"
OTP=""
for i in range(6):
    OTP+=digit[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("nandampushpakumari526@gmail.com","vqzk vjcg tjoj kyrh")
user="nandampushpakumari526@gmail.com"
email=input("enter the mail which you want to send the otp:")
s.sendmail(user,email,msg)
while True:
    a=input("enter  the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("wrong otp")
