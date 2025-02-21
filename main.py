from models.user import User

def main():
    """Main function to manage the budget app"""
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
# We can use a match (which is like case in some other languages) instead of if-elif in Python 3.10 and later.
# The match statement provides a more structured way to handle multiple conditions, 
# making the code more readable and potentially faster for larger sets of conditions.
        if choice == "1":
            set_budget(user)

        elif choice == "2":
            add_income(user)

        elif choice == "3":
            add_expense(user)

        elif choice == "4":
            show_budget(user)

        elif choice == "5":
            # Exit the program
            print("Exiting Budget Manager. Data saved successfully.")
            user.save_user_data()
            break
             
        else:
            print("Invalid choice. Please select a valid option.")


def set_budget(user):
        # Set a budget category
        category = input("Enter category name: ")
        try:
            amount = float(input("Enter budget amount: "))
            user.budget.set_budget(category, amount)
            user.save_user_data()
            print(f"Budget for {category} set to ${amount}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")    


def add_income(user):
        # Add income entry
        category = input("Enter income category: ")
        try:
            amount = float(input("Enter income amount: "))
            user.add_income(category, amount)
            print(f"Income of ${amount} added under {category}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def add_expense(user):
        # Add expense entry
        category = input("Enter expense category: ")
        try:
            amount = float(input("Enter expense amount: "))
            user.add_expense(category, amount)
            print(f"Expense of ${amount} added under {category}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def show_budget(user):
        # Show budget, income, and expenses
        print("\nCurrent Budget:")
        if user.budget.budgets:
            for category, amount in user.budget.budgets.items():
                print(f"{category}: ${amount}")
        else:
            print("No budget set.")

        print("\nIncome:")
        if user.income:
            for category, amount in user.income.items():
                print(f"{category}: ${amount}")
        else:
            print("No income entries.")

        print("\nExpenses:")
        if user.expenses:
            for category, amount in user.expenses.items():
                print(f"{category}: ${amount}")
        else:
            print("No expense entries.")
        



if __name__ == "__main__":
    main()
