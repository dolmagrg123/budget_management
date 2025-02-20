import json
import os

class FileHandler:
    """Handles reading and writing user data."""

    @staticmethod
    def save_user(user):
        """Save user data to JSON file."""
        os.makedirs("data", exist_ok=True)  # Create 'data' directory if not exists

        file_path = "data/user_data.json"

        # Load existing users if the file exists
        users = {}
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                users = json.load(file)

        # Add or update the user data
        users[user.name] = {
            "budget": user.budget.budgets,
            "income": user.income,
            "expense": user.expenses
        }

        # Save the updated list of users to the file
        with open(file_path, "w") as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def load_user():
        """Load user data from JSON file."""
        file_path = "data/user_data.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return json.load(file)
        return {}  # Return an empty dict if no users are found
