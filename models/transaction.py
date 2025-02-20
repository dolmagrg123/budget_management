class Transaction:
    """Base class for a transaction"""

    def __init__(self, category, amount):
        self.category = category  # Category of the transaction (income or expense)
        self.amount = amount      # Amount involved in the transaction

class Income(Transaction):
    """Class to handle Income entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)

class Expense(Transaction):
    """Class to handle Expense entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)

    def __repr__(self):
        """Custom representation for Expense object"""
        return f"Expense(Category: {self.category}, Amount: {self.amount})"
