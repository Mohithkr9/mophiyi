# atmpin =1234
# balance = 1000
# atm_pin=input("Enter your ATM PIN: ")
# if atm_pin == str(atmpin):
#     amount = float(input("Enter the amount to withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print("Withdrawal successful. ")
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Insufficient funds.")
# else:
#     print("Incorrect PIN. Access denied.")   
# 
# 
# --------------------------------------------------------------------------------------------------------------------- 
# color = input("Enter your favorite color: ").lower()

# match color:
#     case "red":
#         print("Stop")
#     case "green":
#         print("Go")
#     case "yellow":
#         print("Slow down")
#     case _:
#         print("Invalid color")
# ----------------------------------------------------------------------------------------------------------------
print("----- MENU -----")
print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Juice")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You selected Pizza.")
    case 2:
        print("You selected Burger.")
    case 3:
        print("You selected Sandwich.")
    case 4:
        print("You selected Juice.")
    case _:
        print("Invalid choice.")