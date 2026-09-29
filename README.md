# Group Expense Debt Simplifier

## Overview
When a group of people share expenses — like roommates, a trip, or a hangout —
figuring out who owes whom quickly becomes confusing, especially when different
people pay for different things. This project solves that problem automatically.

Users log every expense (who paid, how much, and who it was split among), and
the program calculates each person's **net balance** and then works out the
**minimum number of payments** needed to settle the entire group — instead of
everyone paying everyone back individually.

## Features
- Add group members
- Log expenses with flexible splitting (split among everyone, or specific people)
- View a full history of all recorded expenses
- View each member's net balance (who owes money, who is owed money)
- Generate an optimized settlement plan using a greedy debt-simplification algorithm
- Input validation (rejects invalid amounts, unknown member names, etc.)
- Data is saved automatically to a plain text file, so nothing is lost between sessions

## Technologies / Tools Used
- Python 3
- Plain text file handling (`open`, `read`, `write`)
- Core Python concepts: functions, dictionaries, lists, loops, conditionals

## Project Structure
```
group-expense-debt-simplifier/
│
├── main.py                  # Entry point - menu-driven interface
├── expense_manager.py       # Add members, log and list expenses
├── balance_calculator.py    # Calculates each member's net balance
├── debt_simplifier.py       # Greedy algorithm to minimize settlement transactions
├── data_storage.py          # Saves/loads data using a plain text file
├── README.md
└── statement.md
```

## How to Install & Run
1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:
   ```
   python main.py
   ```
   (use `python3 main.py` if `python` doesn't work on your system)

## How to Test
1. Run the program using the steps above.
2. From the menu, choose option **1** to add at least 2-3 members (e.g., Alice, Bob, Charlie).
3. Choose option **2** to log a few expenses — try different payers and different
   ways of splitting (e.g., "all" vs. specific names).
4. Choose option **3** to confirm all expenses were recorded correctly.
5. Choose option **4** to view each member's net balance.
6. Choose option **5** to generate the final settlement plan and verify the
   payments shown correctly settle everyone up.
7. Choose option **6** to exit — then re-run the program to confirm your data
   was saved and reloaded correctly from `expense_data.txt`.

## Example
If Alice pays ₹300 split among all 3 members, and Bob pays ₹150 split between
himself, Alice, and Charlie, the settlement plan will show:
```
Charlie pays Alice Rs.125.00
Charlie pays Bob Rs.50.00
```
instead of multiple separate, unsimplified payments.