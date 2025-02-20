from models.budget import Budget
from utils.file_handler import FileHandler

class User:
    """Class to manage user budget information"""

    def __init__(self, name):
        self.name = name
        self.budget = Budget()
        self.income = {}
        self.expenses = {}

        # Load existing data if available
        data = FileHandler.load_user()

        # Find the user data matching the input name
        user_data = data.get(self.name, None)
        if user_data:
            self.budget.budgets = user_data["budget"]
            self.income = user_data["income"]
            self.expenses = user_data["expense"]
        else:
            print(f"User {self.name} does not exist, creating a new profile.")

    def add_income(self, category, amount):
        """Add an income entry."""
        if category in self.income:
            self.income[category] += amount
        else:
            self.income[category] = amount
        self.save_user_data()

    def add_expense(self, category, amount):
        """Add an expense entry."""
        if category not in self.budget.budgets:
            print(f"Warning: No budget set for {category}.")
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.save_user_data()

    def save_user_data(self):
        """Save user profile and budget categories."""
        FileHandler.save_user(self)
