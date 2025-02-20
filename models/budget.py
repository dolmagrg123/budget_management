class Budget:
    """Class to manage budget categories"""

    def __init__(self):
        self.budgets = {}  # Dictionary to store category-wise budgets

    def set_budget(self, category, amount):
        """Set a budget for a specific category."""
        self.budgets[category] = amount

    def get_budget(self, category):
        """Retrieve the budget for a category."""
        return self.budgets.get(category, 0)  # Returns 0 if category not found
