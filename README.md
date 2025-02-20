# budget_management

Here’s a more concise version of the documentation in **README** format:

---

# Transaction Class Documentation

## Overview
The `Transaction` class represents a financial transaction (either income or expense) and includes details like the amount, category, type, and date. It also provides a method to display a formatted string of the transaction.

---

## Methods

### `__init__(self, amount, category, date=None)`
Initializes a transaction with the following attributes:
- **`amount`**: The monetary value of the transaction (float or int).
- **`category`**: The category or label for the transaction (e.g., "Salary", "Food").
- **`date`** (optional): The date of the transaction. Defaults to the current date if not provided.


## Example

```python
from transaction import Transaction

# Create a transaction
transaction = Transaction(1000, "Salary", "income")

# Print the transaction
print(str(transaction))  # Output: 2025-02-06 12:34:56 | Income | Salary | $1000.00
```

---

This is a quick overview of the `Transaction` class and how to use it in the budget tracker project.