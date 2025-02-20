from models.budget import Budget
from models.transaction import Income, Expense


class User:
    def __init__(self, name):
        self.name = name
        self.budget = Budget()
        self.income = Income
        self.expenses = Expense
