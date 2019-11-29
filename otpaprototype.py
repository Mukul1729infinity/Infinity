
import smtplib 
import math, random
otp=""

n=input('enter your mobile number')
email=input("enter email")
if len(n)==10:
    string="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lent=len(string)
    opt= "your 6 charter otpa for Mkl university is" + "  " + " don't share your otpa " + " for mobile number is " +  n
    for i in range(6):
        opt+=string[math.floor(random.random()*lent)]
print("your 6 digit opt is ",opt,"donot share this with anyone")

def mobile():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("user mail", "password") 
    s.sendmail("user", reciver email, opt) 
    s.quit() 
mobile()    
    
 
