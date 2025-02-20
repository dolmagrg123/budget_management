from models.user import User

def main():
    user_name = input("Enter your name: ")
    user = User(user_name)


    while True:
        print("\nBudget Management Menu:")
        print("1. Set Budget")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Show Budget")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            category = input("Enter category name: ")
            amount = float(input("Enter budget amount: "))
            user.budget.set_budget(category, amount)       
            print(f"Budget for {category} set to {amount}")  

        elif choice == "2":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            user.add_income(category, amount)
            print(f"Income of {amount} added under {category}")

        elif choice == "3":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            user.add_expense(category, amount)
            print(f"Expense of {amount} added under {category}")

        elif choice == "4":
            print("\nCurrent Budget:")
            for category, amount in user.budget.budgets.items():
                print(f"{category}: ${amount}")

        elif choice == "5":
            print("Exiting Budget Manager")
            break

        else:
            print("Invalid choice. Please select a valid option.")

            
if __name__ == "__main__":
    main()