import eveservices as es
import loginFunctions as ls
import bankservices as bs

print("welcome!!")
lr = int(input("do you want to 1. login or 2. register or 3. bank?"))
if(lr==1):
    userName = input("enter your username: ")
    password = input("enter your password: ")
    userDetails = ls.login(userName,password)
    if(userDetails):
        es.eveServices(userDetails)
elif(lr==2):
    firstName = input("enter your first name: ")
    lastName = input("enter your last name: ")
    userName = input("enter your username: ")
    password = input("enter your password: ")
    email = input("enter your email id: ")
    age = input("enter your age: ")
    phone = input("enter your phone: ")
    address = input("enter your address: ")
    pincode = input("enter your pincode: ")
    drivingLicense = input("enter your driving license: ")
    sos = input("enter a sos contact: ")
    uType = input("enter 1. normal, 2. student. : ")
    userDetails = ls.register(firstName,lastName,userName,password,email,age,phone,address,pincode,drivingLicense,sos,uType)
    if(userDetails):
        es.eveServices(userDetails)
elif(lr==3):
    bs.checkPending()
else:
    print("wrong option bye!!")
print("bye!!")
ls.cursor.close()
