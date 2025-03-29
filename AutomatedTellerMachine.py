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

# Transactions
def withdraw():
    while True:
        amount = float(input("Enter your withdrawal amount: "))
        if amount <= acc_bal[card_num]:
            acc_bal[card_num] -= amount
            print(f"Your new balance is: {acc_bal[card_num]:.2f}")
            break
        else:
            print("Invalid amount. Try again.")
            

def deposit():
    amount = float(input("Enter your deposit amount: "))
    acc_bal[card_num] += amount
    print(f"Your new balance is: {acc_bal[card_num]:.2f}")

acc_bal = {
    "01282005":1000.30,
    "01182006":10500.40,
    "08012025":10.00
}

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
while True:
    print("\nPress (1) to Withdraw.\nPress (2) to Desposit.")
    choice = int(input("Choose an option: "))
    if choice == 1:
        withdraw()
    elif choice == 2:
        deposit()
    else:
        print("Invalid option.")
        choice = input("Choose an option: ")

    while True: # asking if want another transaction

        another_transaction = input("Would you like to make another transaction? Y/N: ").lower().strip()

        if another_transaction == "y":
            break # breaking the inner while loop to go back to the main while loop
        elif another_transaction == "n":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input! Please enter 'Y' or 'N'.")
#####