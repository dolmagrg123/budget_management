# Budget Management Application

This Budget Management Application allows users to track and manage their budgets, income, and expenses. The application provides a modular approach to personal finance management with data persistence, error handling, and scalability.

## Features

- **Budget Management**: Set and manage budgets for different categories (e.g., Food, Entertainment, etc.).
- **Income and Expense Tracking**: Add income and expense transactions for different categories.
- **Data Persistence**: Saves user data (budgets, transactions) in a JSON file to ensure data is retained across sessions.
- **Error Handling**: Handles invalid inputs and ensures that data integrity is maintained throughout.
- **Modular Architecture**: Designed with modular components for easy expansion and maintenance.
- **Unit Testing**: Includes unit tests to ensure all key features work as expected.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `json` module (part of the Python standard library)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dolmagrg123/budget_management.git
cd budget_management
```

2. No additional dependencies are required since the project uses only Python’s standard library.

## Usage

1. Run the application:

```bash
python main.py
```

2. Features available:
   - **Set Budget**: Set a budget for different categories (e.g., Food, Entertainment, etc.).
   - **Add Income/Expense**: Add income or expense transactions to a particular category.
   - **View Budget**: View your current budget for any category and compare it against income and expenses.

3. **Data Persistence**:
   - User data is saved in `data/user_data.json` and automatically loaded when the application starts. This ensures your information persists even after closing the app.

4. **Error Handling**:
   - If the user provides invalid inputs (such as non-numeric values for amounts), the application will prompt the user to enter valid numbers.
   - If you try to add an expense to a category with no budget set, the system will alert you that no budget has been set for the category.

## File Structure

```
budget_management/
│
├── data/                       
│   └── user_data.json         # Stores user data (budgets, income, and expenses) in JSON format
│
├── models/                    
│   ├── budget.py              # Defines the Budget class to manage budget categories
│   ├── transaction.py         # Defines Transaction class, with Income and Expense classes inheriting from it
│   └── user.py                # Handles user profile and integrates with FileHandler for saving/loading data
│
├── test/                      
│   └── budget_test.py         # Unit tests to verify the functionality of the application
│
├── utils/
│   └── file_handler.py        # Handles file operations (saving/loading user data to/from JSON)
│
├── main.py                    # Root file to run the application and interact with user
├── .gitignore                 # Git ignore file to exclude unnecessary files/folders from version control
└── README.md                  # Project documentation
```

- **`models/`**: Contains the core logic of the application:
  - `budget.py`: Defines the `Budget` class to manage different budget categories.
  - `transaction.py`: Defines the base `Transaction` class and specialized `Income` and `Expense` classes.
  - `user.py`: Manages user profiles, including adding and viewing budgets and transactions.
  
- **`test/`**: Contains unit tests to verify that the application’s components work as expected.
  - `budget_test.py`: Unit test file that ensures the functionality of the Budget Management Application.

- **`utils/`**: Contains utility classes like `file_handler.py` to manage data storage and retrieval.

- **`data/`**: Contains `user_data.json` where all user data (budgets, transactions, etc.) is stored in a JSON format.

- **`main.py`**: The root file that drives the application. It handles user interactions, runs the budget management logic, and displays information to the user.

- **`.gitignore`**: Specifies files and directories to be ignored by Git version control, such as temporary files, compiled files, and other non-essential files.

## Testing

Unit tests are provided to verify the functionality of the core components:

1. **Run Unit Tests**:

```bash
python -m unittest test/budget_test.py
```

The unit tests ensure that the Budget, Transaction, User classes, and FileHandler class behave as expected and handle edge cases such as invalid inputs and missing categories.


## Future Enhancements

- **Database Integration**: As the application grows, we may integrate a relational database like PostgreSQL or MySQL for better scalability and performance.
- **User Authentication**: Implement user authentication to secure sensitive data and ensure that only authorized users can access their personal financial data.
- **Data Encryption**: Add encryption for sensitive user data to ensure that it remains secure even if unauthorized access occurs.
- **Role-based Access**: Introduce roles and permissions to allow for multiple types of users with different levels of access.
