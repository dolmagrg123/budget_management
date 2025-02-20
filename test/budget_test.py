import unittest
from models.transaction import Income, Expense

class TestTransaction(unittest.TestCase):
    def test_income_initialization(self):
        """Test initializing an income transaction"""
        income = Income(1000, "Salary")
        self.assertEqual(income.amount, 1000)
        self.assertEqual(income.category, "Salary")

    def test_expense_initialization(self):
        """Test initializing an expense transaction"""
        expense = Expense(200, "Food")
        self.assertEqual(expense.amount, 200)
        self.assertEqual(expense.category, "Food")

    def test_expense_repr(self):
        """Test the string representation of an expense"""
        expense = Expense(200, "Food")
        self.assertEqual(repr(expense), "Expense(Category: Food, Amount: 200)")

if __name__ == '__main__':
    unittest.main()
