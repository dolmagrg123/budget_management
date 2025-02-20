import json
import csv
import os

class FileHandler:
    """Handles reading and writing user data."""

    @staticmethod
    def save_user(user):
        """Save user data to a JSON file."""
        data = {
            "name": user.name,
            "budget": user.budget.budgets  # Save budget categories
        }
        with open("data/user_data.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_user():
        """Load user data from JSON file."""
        if os.path.exists("data/user_data.json"):
            with open("data/user_data.json", "r") as file:
                return json.load(file)
        return None  # No user data exists

class TransactionHandler:
    """Handles CSV-based income and expense storage."""

    @staticmethod
    def save_transaction(filename, transaction_list):
        """Save income or expenses to a CSV file."""
        with open(f"data/{filename}", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])  # Header
            for transaction in transaction_list:
                writer.writerow([transaction.category, transaction.amount])

    @staticmethod
    def load_transactions(filename):
        """Load transactions from CSV file."""
        transactions = []
        if os.path.exists(f"data/{filename}"):
            with open(f"data/{filename}", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions.append(Expense(row["Category"], float(row["Amount"])))
        return transactions
