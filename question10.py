def question10():
    balence = 1000

    while True:
        print("\n=== ATM MACHINE ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Choose an option (1-4): "))

        if choice == 4:
            print("Exiting program...")
            break

        elif choice == 1:
            print(f"Your current balance is: ${balence:.2f}")

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balence += amount
                print(f"Deposited ${amount:.2f}. New balance: ${balence:.2f}")
            else:
                print("Invalid amount. Please enter a positive number.")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount > balence:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                balence -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${balence:.2f}")

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

question10()
