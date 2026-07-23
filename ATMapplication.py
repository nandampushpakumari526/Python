#ATM application 
balance = 5000
pin = 1234
card="c"
insert=input("Insert the card")
if insert==card:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Available Balance:", balance)
            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    balance = balance + amount
                    print("Deposit Successful.")
                    print("New Balance:", balance)
                else:
                    print("Invalid Amount")
            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid Amount")
                elif amount > balance:
                    print("Insufficient Balance")
                else:
                    balance = balance - amount
                    print("Please collect your cash.")
                    print("Remaining Balance:", balance)
            elif choice == 4:
                print("Thank you for using our ATM.")
                break
            else:
                print("Invalid Choice")
    else:
        print("Incorrect PIN")
else:
    print("Invalid inserting card")


