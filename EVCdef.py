pin = "8899"
balance = 1000
SalaamBank = 200
pinBank = "9090"
npin = input("Enter PIN: ")


def show_balance(balance):
    print("Your balance is:", balance)


#transfer_evc
def transfer_evc(balance):
    number = input("Enter the number to transfer to: ")
    amount = float(input("Enter the amount to transfer: "))
    if amount <= balance:
        balance -= amount
        print("Successfully transferred $",amount, "to ",number, " Your new balance is $" ,balance)
    else:
        print("ma kugu fillno balance.")
    return balance

#salaam_bank
def salaam_bank(balance, SalaamBank):
    bank_pin = input("Enter Salaam Bank PIN: ")
    if bank_pin == pinBank:
        print("1. Check Salaam Bank Balance")
        print("2. Transfer to Salaam Bank")
        print("3. Transfer from Salaam Bank")
        bank_choice = input("Choose an option: ")

        if bank_choice == "1":
            print("Your Salaam Bank balance is:", SalaamBank)
        elif bank_choice == "2":
            amount = float(input("Enter the amount to transfer to Salaam Bank: "))
            if amount <= balance:
                balance -= amount
                SalaamBank += amount
                print("Successfully transferred $",amount, "balance is ",balance, " Salaam Bank balance is $",SalaamBank)
            else:
                print("ma kugu fillno balance.")
        elif bank_choice == "3":
            amount = float(input("Enter the amount to transfer from Salaam Bank: "))
            if amount <= SalaamBank:
                SalaamBank -= amount
                balance += amount
                print("Successfully transferred $",amount, "from Salaam Bank. balance is ",balance, " Salaam Bank balance is $",SalaamBank)
            else:
                print("ma kugu fillno Salaam Bank balance.")
        else:
            print("Invalid choice.")
    else:
        print("Incorrect Salaam Bank PIN.")
    return balance, SalaamBank

if npin == pin:
    print("1. Itus Haraagaga ")
    print("2. Uwareeji EVC ")
    print("3. Salaam Bank")
    choice = input("Choose an option: ")
if choice == "1":
    show_balance(balance)
elif choice == "2":
     balance = transfer_evc(balance)
elif choice == "3":
     balance, SalaamBank = salaam_bank(balance, SalaamBank)
else:
    print("Invalid choice.")
