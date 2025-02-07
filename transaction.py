from datetime import datetime

class transaction:
    def __init__(self, amount, category, transaction_type, date, notes):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date or datetime.now()
        self.notes = notes

    def __str__(self):
        return f"{self.transaction_type.capitalize()} | {self.category} | ${self.amount:.2f}"
