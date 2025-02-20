import json
import csv
import os
from models.transaction import Expense

class FileHandler:
    """Handles reading and writing user data."""

    @staticmethod
    def save_user(user):
        # Ensure the data directory exists
        os.makedirs("data", exist_ok=True)
        
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
            writer.writerow(["Category", "Amount"])  # Header row
            for transaction in transaction_list:
                print(f"Saving: Category = {transaction.category}, Amount = {transaction.amount}")  # Debug print
                writer.writerow([transaction.category, transaction.amount])


    @staticmethod
    def load_transactions(filename):
        transactions = []
        file_path = f"data/{filename}"
        
        if not os.path.exists(file_path):  # Handle missing files
            return []

        try:
            with open(file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        amount = float(row["Amount"])  # Attempt to convert amount to float
                        transactions.append(Expense(row["Category"], amount))
                    except ValueError:  # Handle cases where Amount is not a valid float
                        print(f"Skipping invalid row: {row}")
            return transactions
        except Exception as e:
            print(f"Error loading transactions from {filename}: {e}")
            return []
