from models.budget import Budget
from models.transaction import Income, Expense


class User:
    def __init__(self, name):
        self.name = name
        self.budget = Budget()
        self.income = []
        self.expenses = []

    def add_income(self,category,amount):
        self.income.append(Income(category, amount))

    def add_expense(self, category, amount):
        self.expenses.append(Expense(category, amount))
