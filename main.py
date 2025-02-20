from models.user import User

def main():
    user_name = input("Enter your name: ")
    user = User(user_name)


    while True:
        print("\nBudget Management Menu:")
        print("1. Set Budget")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Show Budget")
        print("5. Exit")

        choice = input("Select an option: ")

if __name__ == "__main__":
    main()