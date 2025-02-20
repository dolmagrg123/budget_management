

class Transaction:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

class Income(Transaction):
    """Class to handle Income entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)

class Expense(Transaction):
    """Class to handle Expense entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)
