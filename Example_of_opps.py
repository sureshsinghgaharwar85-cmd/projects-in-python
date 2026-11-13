import random

class Details:
    def __init__(self):
        email = input("enter your email: ")
        password = input("enter your password: ")
        username = input("enter your username: ")

class Conformation(Details):
    def OTP_sent(self):
        otp = random.randint(1000,9999)
        print("enter your mobile number the we will sent otp in your mobile number")
        mobile_num = int(input("enter your mobile number: "))
        print(f"{otp}")
        otp_conformation = int(input("enter the OTP: "))
        
        if otp_conformation == otp:
            print("confirmed!")
            print("welcome")
        else:
            print("otp did not matched sorry")

c = Conformation()
c.OTP_sent()
