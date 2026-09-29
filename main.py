"""
main.py
--------
Group Expense Debt Simplifier
------------------------------
Entry point of the program. Shows a menu-driven interface that
ties together all the modules:
    - expense_manager     (add members, log expenses)
    - balance_calculator  (calculate who owes/is owed what)
    - debt_simplifier     (minimize the number of payments needed)
    - data_storage        (save/load data using a plain text file)
"""

from data_storage import load_data, save_data
from expense_manager import add_member, add_expense, list_expenses
from balance_calculator import calculate_balances, print_balances
from debt_simplifier import simplify_debts, print_settlement_plan


def show_menu():
    print("\n===== Group Expense Debt Simplifier =====")
    print("1. Add a member")
    print("2. Add an expense")
    print("3. View all expenses")
    print("4. View balances")
    print("5. Generate settlement plan")
    print("6. Exit")


def get_valid_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input("Enter amount paid: Rs."))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_valid_split(data):
    """Keep asking until every name entered is an actual member."""
    while True:
        split_input = input("Split among (comma-separated names, or 'all'): ").strip()

        if split_input.lower() == "all":
            return data["members"]

        split_among = [name.strip().title() for name in split_input.split(",")]

        # Check that every name entered is a real member
        unknown = [name for name in split_among if name not in data["members"]]
        if unknown:
            print(f"These names are not members yet: {', '.join(unknown)}")
            print(f"Current members are: {', '.join(data['members'])}")
            continue

        return split_among


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter member name: ")
            add_member(data, name)
            save_data(data)

        elif choice == "2":
            if len(data["members"]) < 2:
                print("Add at least 2 members before recording an expense.")
                continue

            print(f"Members: {', '.join(data['members'])}")
            paid_by = input("Who paid? ").strip().title()

            if paid_by not in data["members"]:
                print("That person is not a member yet.")
                continue

            amount = get_valid_amount()
            split_among = get_valid_split(data)

            add_expense(data, paid_by, amount, split_among)
            save_data(data)

        elif choice == "3":
            list_expenses(data)

        elif choice == "4":
            balances = calculate_balances(data)
            print_balances(balances)

        elif choice == "5":
            balances = calculate_balances(data)
            transactions = simplify_debts(balances)
            print_settlement_plan(transactions)

        elif choice == "6":
            print("Goodbye! Your data has been saved.")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()