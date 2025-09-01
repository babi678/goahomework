num_1=float(input("enter first number:"))
num_2=float(input("enter second number:"))
num_3=float(input("enter third number:"))

if num_1==num_2==num_3:
    print("they are the same")
elif num_1==num_2:
    print("it's same")
elif num_1==num_3:
    print("it's same")
elif num_3==num_2:
    print("it's same")
elif num_1!=num_2!=num_3:
    print("they are not the same")

num1=int(input("enter random number (0-12):"))
if num1==12 or num1==1 or num1==2:
    print("ზამთარი")
elif num1==3 or num1==4 or num1==5:
    print("გაზაფხული")
elif num1==6 or num1==7 or num1==8:
    print("ზაფხული")
elif num1==9 or num1==10 or num1==11:
    print("შემოდგომა")
else:print("wrong number")

name=input("enter your name:")
if name=="admin":
    password=input("enter your password:")
    if password=="adminpassword123":
        print("hello admin")
    else:print("u have no connect")
else:print("hello user")