###  Date: 24th April 2021
###
###  Developer: Ifeanyi Udochu
###
###  Title:  Zuri Bank App
###

import random
bankDB = []

### Generate Account Number function
def getAccountNumber():
    number = random.randrange(1111111111, 9999999999)
    return number


def displayWelcomeMessage(acctnum, name):
    print(f"Hello {name},")
    print(f"Welcome to Zuri Bank.")
    print(f"Your account number is {acctnum}")




### Register User function
def OpenNewAccount():
    print("open new account")
    account_number = getAccountNumber()

    name = input("Enter Full Name: ")
    email = input("Enter email address : ")
    initial_balance = float("input(Enter initial deposit amount: ")
    password = input("enter you password (8 character or more) ")
    displayWelcomeMessage(account_number,name)
    ## bankDB.append([account_number, name, email, initial_balance])




### Login function
def Login():
    print("Enter your account credentils")
    acct = input("Enter your account number: ")
    password = input("Enter your password: ")

    ### Loop to verify credentials



### Withdraw function
def Withdraw():
    out_amount = float(input("Enter the amount you wish to withdraw: ") 
    ### if account balance > out_amount:
    ### withdrawal passes
    ### withdaw fail with messgae (insuficient balance)
    ### update bankDB


### Deposit function
def Deposit():
    in_amount = float(input("Enter the amount your wish to deposit: "))
    ## account balance += in_amount
    ##update back db


### Display Account Balance function
def DisplayAccountBalance():
    ## print(f"Your present balance is {accountBalance}")




### Welcome Message function
def Display_Onboard():

    isdisplay = True

    while isdisplay == True:
        print("WELCOME TO ZURI BANK")
        ### Display Onboard Menu function
        print("Zuri Bank ATM")
        print("=============")
        print("1. Login to your account: ")
        print()
        print("2. Open New Account")
        print()
        onboard_choice = int(input ("Enter 1 or 2 to select menu option: "))
        #print(onboard_choice)
        if (onboard_choice == 1):
            isdisplay = False
            Login() 
        elif (onboard_choice == 2):
            isdisplay = False
            OpenNewAccount()
        else: 
            print("Invalid Menu Option Selected!")
            
### Display Operations Menu function
def displayOperationsMenu:
    isDisplay = True
    while isDisplay == True:
        print("What do you wan to do?")
        print("1. Check Account Balance")
        print("2. Make Deposit")
        print("3. Withdrawal")

        choice = int(input("select an option: "))
        if (choice == 1):
            isdisplay = False
            DisplayAccountBalance() 
        elif (onboard_choice == 2):
            isdisplay = False
            Deposit()
        elif (onboard_choice == ):
            isdisplay = False
            Withdraw()
        else: 
            print("Invalid Menu Option Selected!")











def init():
    ##### start menu 
    Display_Onboard()



init()
