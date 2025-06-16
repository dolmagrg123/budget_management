from models.budget import Budget
from utils.file_handler import FileHandler
from models.transaction import Income, Expense # Import Income and Expense classes

class User:
    """Class to manage user budget information"""

    def __init__(self, name):
        self.name = name
        self.budget = Budget()  # Budget instance to store budget details
        self.income = [] #changing income into list
        self.expenses = []  # List to store expense categories and amounts

        # Load existing data if available
        data = FileHandler.load_user()

        # Find the user data matching the input name, or create a new profile
        user_data = data.get(self.name, None)
        if user_data:
            self.budget.budgets = user_data["budget"]
            # Load and convert aggregated income data to list of Income objects
            if "income" in user_data:
                for category, amount in user_data["income"].items():
                    self.income.append(Income(category, amount))
            if "expense" in user_data:
                for category, amount in user_data["expense"].items():
                    self.expenses.append(Expense(category, amount))
        else:
            print(f"User {self.name} does not exist, creating a new profile.")

    def add_income(self, category, amount):
        """Add an income entry."""
        self.income.append(Income(category, amount))


    def add_expense(self, category, amount):
        """Add an expense entry."""
        if category not in self.budget.budgets:
            print(f"Warning: No budget set for {category}.")  # Warn if budget not set for category        #add an expense if category exists:
        self.expenses.append(Expense(category, amount))

    def save_user_data(self):
        """Save user profile and budget categories."""
        FileHandler.save_user(self)
