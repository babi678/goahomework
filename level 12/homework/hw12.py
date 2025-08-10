# დავალება 2
# კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშუნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.
# conditional statement- პირობითი წინადადებები , if/else- განცხადებები გვაქვს if- ფუნქცია თუ არ შესრულდა გამოდის
# გარანტირებული ფუნქცია else

# დავალება 3
# for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.
for i in range(50):
    print("hello world")

# დავალება 4
# while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
i=3
while i<18:
    print(i)
    i=i+1

# დავალება 5
# მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში.
# შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".
user_password=int(input("enter your password:"))
my_password=1234
if user_password==my_password:
    print("Password is correct")
else:print("Password is incorrect")

# დავალება 6
# შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას.
# თუ სახეობა უდრის "ძაღლი" დაბეჟდე "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი"
user_animal=input("enter your favorite animal:")
my_animal="dog"
if user_animal==my_animal:
    print("woaf! woaf!")
else:print("შენ არ გყავს ძაღლი")



