# Banking Application

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("Deposit amount cannot be negative.")
        return 0

    return amount


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount < 0:
        print("Withdrawal amount cannot be negative.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0

    return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Application")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)  
        elif choice == '2':
            balance += deposit()
            show_balance(balance)  
        elif choice == '3':
            balance -= withdraw(balance) 
            show_balance(balance)         
        elif choice == '4':
            is_running = False
            print("Exiting the application. Goodbye!")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()