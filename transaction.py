from datetime import datetime

class Transaction:
    def __init__(self, amount, category, date, notes):
        self.amount = amount
        self.category = category
        self.date = date or datetime.now()
        self.notes = notes


class Income(Transaction):
    """Class to handle Income entries"""
    def __init__(self, category, amount, date, notes):
        super().__init__(category, amount, date, notes)

class Expense(Transaction):
    """Class to handle Expense entries"""
    def __init__(self, category, amount, date, notes):
        super().__init__(category, amount, date, notes)
