expense_data = {}

# View all expenses
def view_expenses(expense_data):
    if not expense_data:
        print("No expenses to display.\n")
        return

    try:
        for category, expenses in expense_data.items():
            print(f"Category: {category}")
            for description, amount in expenses:
                print(f"    - {description}: ${float(amount):.2f}")
        print()
    except Exception as e:
        print(f"An error occurred while displaying expenses: {e}")

# View summary of expenses per category
def view_summary(expense_data):
    if not expense_data:
        print("No expenses to summarize.\n")
        return

    try:
        print("Summary:")
        total = 0
        for category, expenses in expense_data.items():
            category_total = sum(float(amount) for _, amount in expenses)
            print(f"{category}: ${category_total:.2f}")
            total += category_total
        print(f"Total spent: ${total:.2f}\n")
    except Exception as e:
        print(f"An error occurred while summarizing expenses: {e}")

# Main loop
while True:
    print("Welcome to the Personal Finance Tracker!")
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

    try:
        option = int(input("Choose an option (1-4): "))
    except ValueError:
        print("Please enter a number from 1 to 4.\n")
        continue

    if option == 1:
        try:
            description = input("Enter expense description: ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
            continue

        expense = (description, amount)
        if category in expense_data:
            expense_data[category].append(expense)
        else:
            expense_data[category] = [expense]
        print("Expense added successfully.\n")

    elif option == 2:
        view_expenses(expense_data)

    elif option == 3:
        view_summary(expense_data)

    elif option == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose from 1 to 4.\n")
