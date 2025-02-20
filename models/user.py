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
        if data:
            self.name = data["name"]
            self.budget.budgets = data["budget"]
            self.income = TransactionHandler.load_transactions("income.csv")
            self.expenses = TransactionHandler.load_transactions("expenses.csv")

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
