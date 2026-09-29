"""
debt_simplifier.py
--------------------
Takes everyone's net balance and finds the MINIMUM number of
transactions needed to settle the whole group.

This uses a simple greedy algorithm:
Repeatedly match the person who owes the MOST with the person
who is owed the MOST, settle as much as possible between them,
and repeat until everyone's balance is zero.
"""


def simplify_debts(balances):
    """
    balances: dictionary of {name: net_balance}
    Returns a list of settlement instructions like:
    [("Alice", "Bob", 150.0), ...]  meaning Alice pays Bob Rs.150
    """
    # Work on a copy so we don't modify the original balances
    balances = balances.copy()
    transactions = []

    while True:
        # Find the person who owes the most (most negative balance)
        debtor = min(balances, key=balances.get)
        # Find the person who is owed the most (most positive balance)
        creditor = max(balances, key=balances.get)

        # If both are (close to) zero, everyone is settled
        if round(balances[debtor], 2) == 0 and round(balances[creditor], 2) == 0:
            break

        # Settle the smaller of the two amounts between this pair
        amount = min(-balances[debtor], balances[creditor])
        amount = round(amount, 2)

        if amount <= 0:
            break

        transactions.append((debtor, creditor, amount))

        balances[debtor] += amount
        balances[creditor] -= amount

    return transactions


def print_settlement_plan(transactions):
    """Display the final simplified settlement plan."""
    print("\n----- Settlement Plan -----")
    if not transactions:
        print("Everyone is already settled up!")
        return

    for payer, receiver, amount in transactions:
        print(f"{payer} pays {receiver} Rs.{amount:.2f}")