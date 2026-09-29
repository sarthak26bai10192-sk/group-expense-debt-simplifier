"""
expense_manager.py
-------------------
Handles adding group members and logging expenses.
"""


def add_member(data, name):
    """Add a new member to the group if not already added."""
    name = name.strip().title()
    if name in data["members"]:
        print(f"{name} is already a member.")
    else:
        data["members"].append(name)
        print(f"{name} added to the group.")


def add_expense(data, paid_by, amount, split_among):
    """
    Record a new expense.
    paid_by       -> name of the person who paid
    amount        -> total amount paid
    split_among   -> list of names who share this expense
    """
    expense = {
        "paid_by": paid_by,
        "amount": amount,
        "split_among": split_among
    }
    data["expenses"].append(expense)
    print(f"Expense of Rs.{amount} by {paid_by} recorded, split among {len(split_among)} people.")


def list_expenses(data):
    """Print all recorded expenses so far."""
    if not data["expenses"]:
        print("No expenses recorded yet.")
        return

    print("\n----- All Expenses -----")
    for index, expense in enumerate(data["expenses"], start=1):
        names = ", ".join(expense["split_among"])
        print(f"{index}. {expense['paid_by']} paid Rs.{expense['amount']} (split among: {names})")