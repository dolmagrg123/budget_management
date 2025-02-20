from models.budget import Budget
from models.transaction import Income, Expense
from utils.file_handler import FileHandler, TransactionHandler

class User:
    """Class to manage user budget information"""

    def __init__(self, name):
        self.name = name
        self.budget = Budget()
        self.income = []
        self.expenses = []

        # Load existing data if available
        data = FileHandler.load_user()

        # Find the user data matching the input name
        user_data = next((user for user in data if user["name"] == self.name), None)
        if user_data:
            self.budget.budgets = user_data["budget"]
            self.income = TransactionHandler.load_transactions("income.csv")
            self.expenses = TransactionHandler.load_transactions("expenses.csv")
        else:
            print(f"User {self.name} does not exist, creating a new profile.")

    def add_income(self, category, amount):
        """Add an income entry."""
        self.income.append(Income(category, amount))
        TransactionHandler.save_transaction("income.csv", self.income)

    def add_expense(self, category, amount):
        """Add an expense entry."""
        if category not in self.budget.budgets:
            print(f"Warning: No budget set for {category}.")
        self.expenses.append(Expense(category, amount))
        TransactionHandler.save_transaction("expenses.csv", self.expenses)

    def save_user_data(self):
        """Save user profile and budget categories."""
        FileHandler.save_user(self)
