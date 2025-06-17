import json
from models.user import User
from utils.file_handler import FileHandler


# We can use a match (which is like case in some other languages) instead of if-elif in Python 3.10 and later.
# The match statement provides a more structured way to handle multiple conditions,
# making the code more readable and potentially faster for larger sets of conditions.

def main():
    """Main function to manage the budget app"""
    user_name = input("Enter your username: ")
    user = User(user_name)

    while True:
        print("""
        Budget Management Menu:
        1. Set Budget (Create New/Update Existing)
        2. Income (Create New/Update Existing)
        3. Expense (Create New/Update Existing)
        4. Show Budget
        5. Exit (Saves all Changes)
        """)

        choice = input("Select an option: ")
        if choice == "1":
            list_existing_categories('budget') # Pass 'budget' to list only budget categories
            set_budget_option(user)

        elif choice == "2":
            add_income_option(user)

        elif choice == "3":
            add_expense_option(user)

        elif choice == "4":
            show_budget_option(user)

        elif choice == "5":
            # Exit the program
            print("Exiting Budget Manager. Data saved successfully.")
            FileHandler.save_user(user)
            break

        else:
            print("Invalid choice. Please select a valid option.")

def get_all_categories(user_data):
    """
    Extracts all unique income and expense categories from the loaded user data.

    Args:
        user_data (dict): The loaded user data from user_data.json.

    Returns:
        tuple: A tuple containing two sets: unique income categories and unique expense categories.
    """
    income_categories = set()
    expense_categories = set()
    for user_info in user_data.values():
        income_data = user_info.get("income", [])
        expense_data = user_info.get("expense", [])

        # Handle both old dictionary format and new list format
        if isinstance(income_data, dict):
            income_categories.update(income_data.keys())
        elif isinstance(income_data, list):
            income_categories.update(t.get("category") for t in income_data if isinstance(t, dict) and "category" in t)

        if isinstance(expense_data, dict):
            expense_categories.update(expense_data.keys())
        elif isinstance(expense_data, list):
            expense_categories.update(t.get("category") for t in expense_data if isinstance(t, dict) and "category" in t)

    return income_categories, expense_categories



def set_budget_option(user):
 # Set a budget category
    category = input("Enter category name for your budget: ")
    try:
        amount = float(input("Enter budget amount: "))
        user.budget.set_budget(category, amount)
        print(f"Budget for {category} set to ${amount}")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def add_income_option(user):
    # Add income entry
    list_existing_categories('income')
    category = input("Enter income category: ")

    # Check if the category already exists in user's income transactions
    category_exists = any(income.category == category for income in user.income)

    proceed_with_add = True # Flag to control whether to add the transaction

    if category_exists:
        print(f"Category '{category}' already exists.")
        while True: # Loop to get valid user choice
            choice = input("Options: 1. Add a new income transaction with this category, 2. Cancel: ")
            if choice == '1':
                break # Exit the loop and proceed with adding
            elif choice == '2':
                proceed_with_add = False # Set flag to False to cancel
                print("Operation cancelled.")
                break # Exit the loop
            else:
                print("Invalid choice. Please enter 1 or 2.")

    if proceed_with_add: # Only proceed if the flag is True
        try:
            amount = float(input("Enter income amount: "))
            user.add_income(category, amount)
            print(f"Income of ${amount} added under {category}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def add_expense_option(user):
    # Add expense entry
    list_existing_categories('expense')
    category = input("Enter expense category: ")

    # Check if the category already exists in user's expense transactions
    category_exists = any(expense.category == category for expense in user.expenses)

    proceed_with_add = True # Flag to control whether to add the transaction

    if category_exists:
        print(f"Category '{category}' already exists.")
        while True: # Loop to get valid user choice
            choice = input("Options: 1. Add a new expense transaction with this category, 2. Cancel: ")
            if choice == '1':
                break # Exit the loop and proceed with adding
            elif choice == '2':
                proceed_with_add = False # Set flag to False to cancel
                print("Operation cancelled.")
                break # Exit the loop
            else:
                print("Invalid choice. Please enter 1 or 2.")

    if proceed_with_add: # Only proceed if the flag is True
        try:
            # Note: The warning for no budget set for the category remains here
            if category not in user.budget.budgets:
                print(f"Warning: No budget set for {category}.")

            amount = float(input("Enter expense amount: "))
            user.add_expense(category, amount)
            print(f"Expense of ${amount} added under {category}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def show_budget_option(user):
    # Show budget, income, and expenses
    print("\nCurrent Budget:")
    if user.budget.budgets:
        for category, amount in user.budget.budgets.items():
            print(f"{category}: ${amount}")
    else:
        print("No budget set.")

    print("\nIncome:")
    if user.income:
        for income in user.income:
            print(f"Category: {income.category}, Amount: ${income.amount}")
    else:
        print("No income entries.")

    print("\nExpenses:")
    if user.expenses:
        for expense in user.expenses:
            print(f"Category: {expense.category}, Amount: ${expense.amount}")
    else:
        print("No expense entries.")

def list_existing_categories(category_type):
    # Load all user data to get categories from other users as well
    user_data = FileHandler.load_user()
    all_income_categories, all_expense_categories = get_all_categories(user_data)
    all_budget_categories = set()
    for user_info in user_data.values():
        if "budget" in user_info:
            all_budget_categories.update(user_info["budget"].keys())

    if category_type == 'budget':
        print("\nExisting Budget Categories:")
        if all_budget_categories:
            print(", ".join(all_budget_categories))
        else:
            print("No existing budget categories.")
    elif category_type == 'income':
        print("\nExisting Income Categories:")
        if all_income_categories:
            print(", ".join(all_income_categories))
        else:
            print("No existing income categories.")
    elif category_type == 'expense':
        print("\nExisting Expense Categories:")
        if all_expense_categories:
            print(", ".join(all_expense_categories))
        else:
            print("No existing expense categories.")


if __name__ == "__main__":
    main()
