```markdown
# Budget Management App

This is a simple command-line budget management application built with Python. It allows users to set budgets for different categories, track income and expenses, and view their overall budget status.

## Features

*   **Set Budget:** Define budget limits for various categories (e.g., food, rent, entertainment).
*   **Add Income:** Record income entries with category and amount.
*   **Add Expense:** Record expense entries with category and amount.
*   **Show Budget:** Display the current budget status, including budget limits, income, expenses, and remaining balance for each category.
*   **Data Persistence (Suggested):** *(Not yet implemented)* In future versions, the application will save budget data to a file (e.g., CSV, JSON) so that it persists between sessions.

## Getting Started

1.  **Prerequisites:** Python 3.x

2.  **Installation:**

    ```bash
    # No installation steps needed as it's a simple script
    # But you can create a virtual environment (recommended):
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Running the App:**

    ```bash
    python main.py
    ```

## Usage

1.  Run the application using the command above.
2.  Follow the on-screen menu to interact with the budget manager.
3.  Enter your name when prompted to begin.
4.  Use the numbered options to navigate through the menu and manage your budget.



## Code Examples

*   **Setting a budget:**

    ```python
    user.budget.set_budget("Food", 300)
    ```

*   **Adding income:**

    ```python
    user.add_income("Salary", 2000)
    ```

*   **Adding an expense:**

    ```python
    user.add_expense("Food", 50)
    ```


