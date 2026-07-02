atmpin =1234
balance = 1000
atm_pin=input("Enter your ATM PIN: ")
if atm_pin == str(atmpin):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. ")
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient funds.")
else:
    print("Incorrect PIN. Access denied.")    