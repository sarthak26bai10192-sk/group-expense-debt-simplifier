"""
data_storage.py
----------------
Handles saving and loading data to/from a plain text file so
records are not lost when the program closes.

File format used (expense_data.txt):
    MEMBERS
    Alice
    Bob
    EXPENSES
    Alice,300.0,Alice|Bob|Charlie
    Bob,150.0,Alice|Charlie
"""

DATA_FILE = "expense_data.txt"


def load_data():
    """Load members and expenses from the text file.
    If the file doesn't exist yet, return empty starting data."""
    data = {"members": [], "expenses": []}

    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return data

    section = None  # tracks whether we're reading members or expenses

    for line in lines:
        line = line.strip()

        if line == "":
            continue
        elif line == "MEMBERS":
            section = "members"
        elif line == "EXPENSES":
            section = "expenses"
        elif section == "members":
            data["members"].append(line)
        elif section == "expenses":
            parts = line.split(",")
            paid_by = parts[0]
            amount = float(parts[1])
            split_among = parts[2].split("|")
            data["expenses"].append({
                "paid_by": paid_by,
                "amount": amount,
                "split_among": split_among
            })

    return data


def save_data(data):
    """Save the current members and expenses to the text file."""
    with open(DATA_FILE, "w") as file:
        file.write("MEMBERS\n")
        for member in data["members"]:
            file.write(member + "\n")

        file.write("EXPENSES\n")
        for expense in data["expenses"]:
            names = "|".join(expense["split_among"])
            file.write(f"{expense['paid_by']},{expense['amount']},{names}\n")