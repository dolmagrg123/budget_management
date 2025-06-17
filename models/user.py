import json
from models.budget import Budget
from utils.file_handler import FileHandler
from models.transaction import Income, Expense

class User:
    """Class to manage user budget information"""

    def __init__(self, name):
        self.name = name
        self.budget = Budget()  # Budget instance to store budget details
        self.income = []  # List to store Income objects
        self.expenses = []  # List to store Expense objects

        # Load existing data if available
        data = FileHandler.load_user()

        # Find the user data matching the input name, or create a new profile
        user_data = data.get(self.name, None)
        if user_data:
            self.budget.budgets = user_data.get("budget", {})

            # Load and convert income data
            income_data_loaded = user_data.get("income", {})
            if isinstance(income_data_loaded, dict):
                # Old format (dictionary of aggregated amounts)
                for category, amount in income_data_loaded.items():
                    self.income.append(Income(category, amount))
            elif isinstance(income_data_loaded, list):
                # New format (list of transaction dictionaries)
                for transaction_data in income_data_loaded:
                    if isinstance(transaction_data, dict) and "category" in transaction_data and "amount" in transaction_data:
                        self.income.append(Income(transaction_data["category"], transaction_data["amount"]))

            # Load and convert expense data
            expense_data_loaded = user_data.get("expense", {})
            if isinstance(expense_data_loaded, dict):
                # Old format (dictionary of aggregated amounts)
                for category, amount in expense_data_loaded.items():
                    self.expenses.append(Expense(category, amount))
            elif isinstance(expense_data_loaded, list):
                # New format (list of transaction dictionaries)
                for transaction_data in expense_data_loaded:
                    if isinstance(transaction_data, dict) and "category" in transaction_data and "amount" in transaction_data:
                        self.expenses.append(Expense(transaction_data["category"], transaction_data["amount"]))

        else:
            print(f"User {self.name} does not exist, creating a new profile.")

    def add_income(self, category, amount):
        """Add an income entry."""
        self.income.append(Income(category, amount))

    def add_expense(self, category, amount):
        """Add an expense entry."""
        if category not in self.budget.budgets:
            print(f"Warning: No budget set for {category}.")
        self.expenses.append(Expense(category, amount))

    def save_user_data(self):
        """Save user profile and budget categories."""
        FileHandler.save_user(self)
