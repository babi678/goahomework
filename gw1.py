#ბანკის დასაწყისი
print("Welcome to GOA Bank!")
print("enter your pin code: (if you dont have it yet create one. press enter to create your pin code)")
input("")
Pin = int(input("Create your pin code: "))
print("Your pin code has been created successfully.")

tries = 3
while tries > 0:
    Pin1= int(input("Enter your PIN: "))
    if Pin1 == Pin:
        break
    else:
        tries = tries - 1
        print("Pin code incorrect. "+ str(tries) + " " + "tries left.")
    if tries == 0:
        print( "Access denied. Please try again later.")
input("")
#ბანკში შესვლა
print("choose")
print("1- login")
print("2- registration")
choice_1=int(input("Choose:"))
default_password="GOA"
if choice_1==1:

    user_name_1=input("Enter your username: ")
    while True:
        default_password="GOA"
        default_password_1=input("Enter your password:")
        if default_password_1==default_password:
            print("Welcome!")
            break
        else:
            print("password is incorrect")
if choice_1==2:
    input("Press Enter to start registration:")
    print("Registration Form:")

#მომხმარებლის მონაცემების შეყვანა
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user_id = input("Enter your ID: ")
    user_name=input("enter your username: ")
    #პაროლის შემოწმება while ციკლით
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Repeat password: ")

    #თუ პაროლები ემთხვევა ციკლი შეწყდება
        if password == confirm_password:
            print("Password saved successfully!")
            break  # ციკლის შეწყვეტა
        else:
            # თუ პაროლები არ ემთხვევა მომხმარებელს დაეცემა შეტყობინება
            print("Passwords do not match, try again.")

    print("login")
    while True:
        user_name_2=input("enter your username: ")
        password_2=input("enter your password: ")

        if user_name_2=="" or password_2=="":
            print("input fields should not be empty")
        elif user_name_2!=user_name or password_2!=password:
            print("try again")
            break
        else:
            #სტატუსის არჩევა
            print("Choose your status:")
            print("1 - Pupil")
            print("2 - Student")
            choice = int(input("Enter number: "))

            #სტატუსის შენახვა
            if choice == 1:
                status = "Pupil"
            else:
                status = "Student"

            #რეგისტრაციის შედეგების ჩვენება
            print(" Registration completed!")
            print("")
            print("First Name:", first_name)
            print("Last Name:", last_name)
            print("ID:", user_id)
            print("Status:", status)

            #პროგრამის დასასრული
            print("")
            print(first_name ,"Thank you for using GOA Bank!")
            print("")
print("would you like to fill your balance?")
print("choose:")
print("yes")
print("no")
choice_6=input("enter your answer:")
if choice_6=="yes":
    balance = int(input("enter your balance: " ))
    print("you have succesfully updated your balance")
if choice_6=="no":
    print("your balance has not been updated.")
print("would you like to fill your AURA_balance?")
print("choose:")
print("yes")
print("no")
print("")
choice_7=input("enter your answer:")
if choice_7=="yes":
    A_balance=int(input("enter your AURA_balance:"))
    print("your AURA_balance has not been updated.")
if choice_7=="no":
    print("your AURA_balance has not been updated.")
print("")
print("0. view information")
print("1. pay the tuition fee")
print("2. send money to another student")
print("3. switch currency")
print("4. view balance")
print("5. Transaction history")
print("6. Offers")
print("7. card")
print("8. settings")
print("9. exit")
choice = int(input("choose an action (0-9): "))

#გადასახადის გადახდა
if choice == 0:
    print("  ---------💚GoaCash💚--------")
    print("🏦GoaCash is the mobile app designed to put the power of banking at your fingertips." \
    "🤑Our app provides a secure and straightforward way to manage your cash and AURAS in one place.")
    print("")
    print("---What are auras?---")
    print("Aura is a special GoaCash currency, which allows you to pay GOA Academy's tuition fee.💵")
    print("")
    print(" ---Why choose GoaCash?---")
    print("✅Instant account access: quick registration,check your balance and view transactions anywhere anytime!")
    print("")
    print("💵Quick transactions : easily convert ₾ to AURA😎")
    print("")
    print("💚Fast and easy transfers: Send money or AURAS to your fellow GOA academy friends, pupils and students!")
    print("")
    print("💰Get discounts and daily notifications about your finances!")
    print("")
    print("👾seamlessly and easily view your transaction history")
    print("---Why are GoaCash verification cards compulsory?---")
    print("At hackathons, participants are required to carry a special verification card that serves as proof of registration and eligibility to enter the event.💻👩‍💻")
    print("These cards are typically issued after the participant has successfully checked in with their registration details🪪🫆.")
    print("")
    print("--------💚💚💚--------")
    print("")
    print("🗿Never forget! You are a GIGA CHAD, so use GoaCash to simplify your financial life and take control of your money and AURAS like never before🧠")
    answer = input("Would you like to return to the menu?: ")
elif choice == 1:
    fee = float(input("enter the amount: "))
    if fee <= balance:
        print("payment succesfull.")
        print("Enter to view transaction history")
        input("")
        print("You have paid tution fee of"+fee+"and right now your balance is"+balance)
        print("")
    else:print("payment unseccesfull.")
elif choice == 2: # ფულის გაგზავნა სხვა სტუდენტისთვის
    sending = float(input("enter the amount: "))
    if sending <= balance:
        NAME=input("enter the user: ")
        print("succesful.  ")
        print("Enter to view transaction history")
        input("")
        print("You have sent money to"+NAME)
    else:print("unseccesfull.  ")
elif choice == 3: #ვალუტის შეცვლა
    print("change the currency")
    print("")
    Auras=int(input("Enter how many Auras you want to exchange in GEL:")) 
    if balance >= Auras:
        if Auras >= 1000:
            exchanged = Auras * 10 + 200
        elif Auras >= 500:
            exchanged = Auras * 10 + 100
        elif Auras >= 200:
            exchanged = Auras * 10 + 50
        else:
            exchanged = Auras * 10

        A_balance -= Auras
        print("Balance after transaction: " + str(A_balance)+"Auras")
        print("You received:" + str(exchanged)+"GEL")
        print("")
        print("The transaction is completed ")
        print("Enter to view transaction history")
        input("")
        print("You succesfully exchanged"+Auras+"into"+exchanged+"GEL")
    else:
        print("The transaction could not be completed ")
    print("")
#ბალანსის ნახვა
elif choice == 4:
    print("your balance is" + str(balance)+"GEL")
    print("your AURA_balance" + str(A_balance)+"Auras")
# სეთინგები
elif choice==8:
    print("choose")
    print("a. terms and conditions.")
    print("b. privacy")

    sub_choice_1=input("enter your choice: ")
    if sub_choice_1=="a":
        print("---------📜Terms & Conditions📜----------")
        print("1)By creating an account and using this application, you agree to comply with these Terms and Conditions. The app is intended solely for personal banking, payments, and related services.")

        print("2)You are responsible for keeping your login credentials and PIN secure. The bank is not liable for losses arising from unauthorized access due to negligence in safeguarding your account.")

        print("3)All payments and transfers made through the app are processed according to current banking policies. Once confirmed, transactions cannot be reversed")

        print("4)service charges, discounts, or reward programs (including AURAS and cashback) may be subject to change.")

        print("5)Your personal data will be collected and processed in accordance with the official Privacy Policy to ensure the security and efficiency of banking services.")
        print("-----------------------------")
        print("Please review our Terms and Conditions before continuing.")
        print("By selecting “I agree”, you confirm that you have read, understood, and accepted the Terms and Conditions.")
        print("If you select “i disagree”, you will not be able to proceed with the use of this application.")
        choice2 = int(input("Please choose (1-2): "))
        print("1. i agree.")
        print("2. i disagree.")
        if choice2== 1:
            print("Thank you for accepting the Terms and Conditions. You may now proceed to use GoaCash.")
        else:
            print("Access to GoaCash will be restricted until you agree to the terms.")
    elif sub_choice_1=="b":
        while True:
            password_11=input("enter your password to acces: ")
            if password_11==password_2:
                print("access granted!")
                input("")
                print("--------------------------")
                print("P. change my password")
                print("C. change the card passcode")
                print("B. change the bank passcode")
                choice_0=input("what would you like to do?: ")
                if choice_0=="P":
                    cur_password=input("enter your current password: ")
                    while True:
                        if cur_password!=password_2:
                            print("access denied.try again.") 
                            break
                        else:
                            new_password=input("enter your new password: ")
                            input("")
                            print("you have succesfuly changed your password.")
                elif choice_0=="C":
                    cur_passcode_card=input("enter your current passcode: ")
                    while True:
                        default_passcode=1234
                        if cur_passcode_card!=default_passcode:
                            print("access denied.try again.") 
                            break
                        else:
                            new_passcode_card=input("enter your new passcode: ")
                            input("")
                            print("you have succesfuly changed your passcode.")
                elif choice_0=="B":
                    cur_passcode_bank=input("enter your current passcode: ")
                    while True:
                        if cur_passcode_bank!=Pin:
                            print("access denied.try again.") 
                            break
                        else:
                            new_passcode_bank=input("enter your new passcode: ")
                            input("")
                            print("you have succesfuly changed your passcode.")
            break
    else:
        print("try again")

#გამოსვლა
elif choice == 9:
    print("BYE BYE! 📌 ")
running = False



