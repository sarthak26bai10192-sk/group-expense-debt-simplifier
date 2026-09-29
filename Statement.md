# Problem Statement

## Problem Statement
When a group of people share expenses over time — such as roommates splitting
rent and groceries, or friends splitting costs during a trip — it becomes
increasingly difficult to track who paid for what and who ultimately owes whom.
Simply listing every individual transaction leads to a confusing web of debts,
often requiring far more payments than necessary to settle the group.

This project addresses that problem by allowing users to log group expenses
and automatically calculating a simplified settlement plan that clears every
debt using the minimum possible number of transactions.

## Scope of the Project
- Track multiple group members and the expenses they log
- Support flexible expense splitting (equally among everyone, or among
  selected members only)
- Calculate each member's net balance across all recorded expenses
- Simplify group debts into the minimum number of payments using a greedy
  algorithm
- Persist data between sessions using local text file storage
- Provide a simple, menu-driven command-line interface

This project does not include real payment processing, multi-currency
support, or a graphical/web interface — it is a command-line tool intended
to demonstrate core programming concepts through a practical, real-world
problem.

## Target Users
- Roommates sharing recurring household expenses
- Groups of friends splitting costs during trips, outings, or events
- Any small group that shares expenses and wants a fair, simplified way to
  settle up

## High-Level Features
- Add and manage group members
- Log expenses with details on who paid and how the cost is split
- View a complete history of all recorded expenses
- View each member's current balance (amount owed or to be received)
- Generate an optimized settlement plan requiring the fewest possible
  transactions
- Automatic data persistence so information is not lost between runs