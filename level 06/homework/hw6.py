# დავალება 1
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
print(num_1>num_2)
print(num_1<num_2)
print(num_1==num_2)

# დავალება 2
num1="12"
num2="30"
num3="48"
num4=50
num5=40
print(int(num1)*int(num2)*int(num3)*num4*num5)
print((int(num1)*int(num2)*int(num3)*num4*num5)/5)

# დავალება 3
name_1=input("enter your name:")
name_2=input("enter your surname:")
name_3=input("enter your fav animal:")
number_1=int(input("enter random number:"))
print(name_1+name_2+name_3)
NAME=name_1+name_2+name_3
print(NAME*number_1)

# დავალება 4
# ჩვენ ვისწავლეთ ორი ლოგიკური ოპერატორი or , and 
# and-ის დროს უპირატესობა ენიჭება false-ს , or-ის დროს უპირატესობა ენიჭება true-ს

# დავალება 5
                        
True and True --  True   |   True or True -- True          
True and False -- False    |   True or False -- True
False and True -- False  |   False or True -- True
False and False -- False|   False or False -- False

# დავალება 6
print(True and False)
print(True or True)

# დავალება 7
animal="dog"
number=40
height=1.80
honesty=True
print(type(animal))
print(type (number))
print(type(height))
print(type(honesty))

# დავალება 8
Name_1=input("enter your fav fruit:")
Num_1=int(input("enter number:"))
Num_2=float(input("enter your height:"))
x=input("enter float:")
print(bool(x))