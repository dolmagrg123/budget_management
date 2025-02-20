

class Transaction:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount  

class Income(Transaction):
    """Class to handle Income entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)

class Expense(Transaction):
    """Class to handle Expense entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)
    def __repr__(self):
        return f"Expense(Category: {self.category}, Amount: {self.amount})"