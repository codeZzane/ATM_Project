# Automated Teller Machine (ATM) - My FIrst Project
# Author: Adam Daniel P. Azarcon PUP BSCPE
# Date: March 26, 2025


reg_acc = {       # Key:Value
    "01282005":"012805", # CAN:PIN
    "01182006":"011806",
    "08012025":"080125"
}

# Ask for CAN and PIN
card_num = input("Enter your CAN: ")
pass_num = input("Enter your PIN: ")

# Verify if registered
for i in range(2, 0, -1):
    if card_num in reg_acc and reg_acc[card_num] == pass_num:
        print("Welcome!")
        break
    else:
        print(f"Invalid credentials. {i} tries left.")
        card_num = input("Enter your CAN: ")
        pass_num = input("Enter your PIN: ")
else:
    print("Access Denied.")

# if not, try asking again for 3 times
# if yes, display account details
# ask if deposit or withdraw
# if withdraw, ask for amount and check whether amount is <= account balance
# if deposit, ask for amount and add it to the account balance
# display new balance
# ask if new transaction or end