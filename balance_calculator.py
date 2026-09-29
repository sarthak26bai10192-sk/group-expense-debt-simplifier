"""
balance_calculator.py
----------------------
Calculates how much each person owes or is owed (net balance).
"""


def calculate_balances(data):
    """
    Returns a dictionary: { member_name: net_balance }
    Positive balance  -> this person should RECEIVE money
    Negative balance  -> this person OWES money
    """
    balances = {member: 0 for member in data["members"]}

    for expense in data["expenses"]:
        paid_by = expense["paid_by"]
        amount = expense["amount"]
        split_among = expense["split_among"]
        share = amount / len(split_among)

        # The payer gets credited the full amount they paid
        balances[paid_by] += amount

        # Everyone sharing the expense gets debited their share
        for person in split_among:
            balances[person] -= share

    return balances


def print_balances(balances):
    """Display each person's balance in a readable way."""
    print("\n----- Net Balances -----")
    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} should RECEIVE Rs.{balance:.2f}")
        elif balance < 0:
            print(f"{person} OWES Rs.{-balance:.2f}")
        else:
            print(f"{person} is settled up.")