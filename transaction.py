from datetime import datetime

class Transaction:
    def __init__(self, amount, category, transaction_type, date, notes):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date or datetime.now()
        self.notes = notes

    def __str__(self):
        return f"{self.transaction_type.capitalize()} | {self.category} | ${self.amount:.2f}"

class Income(Transaction):
    """Class to handle Income entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)

class Expense(Transaction):
    """Class to handle Expense entries"""
    def __init__(self, category, amount):
        super().__init__(category, amount)
