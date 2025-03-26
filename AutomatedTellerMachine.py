# Automated Teller Machine (ATM) - My FIrst Project
# Author: Adam Daniel P. Azarcon PUP BSCPE
# Date: March 26, 2025

# Initialize Accounts
def account_1():
    acc1Balance = 1000.30
    print("Account No.: 01282005")
    print("Name: Adam Daniel Azarcon")
    print(f"Your balance is: {acc1Balance:.2f}")

def account_2():
    acc2Balance = 10500.40
    print("Account No.: 01182006")
    print("Name: Ezra Jan Zuzzane Panado")
    print(f"Your balance is: {acc2Balance:.2f}")

def account_3():
    acc3Balance = 10.00
    print("Account No.: 08012025")
    print("Name: Daniel Rove Azarcon")
    print(f"Your balance is: {acc3Balance:.2f}")

reg_acc = {       # Key:Value
    "01282005":"012805", # CAN:PIN
    "01182006":"011806",
    "08012025":"080125"
}

acc_details = {
    "01282005":account_1,
    "01182006":account_2,
    "08012025":account_3
}

# Ask for CAN and PIN
card_num = "01182006" #input("Enter your CAN: ")
pass_num = "011806" #input("Enter your PIN: ")

# Verify if registered
for i in range(2, 0, -1): # 3 tries only
    if card_num in reg_acc and reg_acc[card_num] == pass_num:
        print("Welcome!")
        acc_details[card_num]() # displaying account details from the provided card_num
        break
    else:
        print(f"Invalid credentials. {i} tries left.")
        card_num = input("Enter your CAN: ")
        pass_num = input("Enter your PIN: ")
else:
    print("Access Denied.")

# ask if deposit or withdraw
print("Press (1) to Withdraw.\nPress (2) to Desposit.\nPress (0) to exit.")
# if withdraw, ask for amount and check whether amount is <= account balance
# if deposit, ask for amount and add it to the account balance
# display new balance
# ask if new transaction or end