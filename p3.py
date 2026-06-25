""""
password =input("enter the rigt password : ")

if len(password) <8 :
    print("pass is too short")

else:
    print("password is accepted")
"""
###########################################################

password = input("Enter Password: ")

if len(password) < 8:
    print("Password too short")

elif not any(char.isdigit() for char in password):
    print("Password must contain a number")

elif not any(char.isupper() for char in password):
    print("Password must contain a capital letter")

else:
    print("Strong Password")

####################################
"""
email = input("Email: ")
password = input("Password: ")

if "@" not in email or "." not in email:
    print("Invalid Email")

elif len(password) < 8:
    print("Password too short")

elif not any(char.isdigit() for char in password):
    print("Password must contain a number")

elif not any(char.isupper() for char in password):
    print("Password must contain a capital letter")

else:
    print("Registration Successful")
"""