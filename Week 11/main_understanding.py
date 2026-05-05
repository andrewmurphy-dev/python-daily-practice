






def main():
    expenses = load_expenses()

    if expenses is None:
        return

    name = input("Expense name: ").strip()
    amount_text = input("Amount: ").strip()

    if not name:
        print("Error: expense name cannot be empty.")
        return

    try:
        amount = int(amount_text)
    except ValueError:
        print("Error: amount must be a number.")
        return

    if amount <= 0:
        print("Error: amount must be greater than 0.")
        return

    add_expense(expenses, name, amount)
    save_expenses(expenses)                             #here we call save expenses

    print("Expense saved.")
    print(expenses)