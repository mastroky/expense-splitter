# Expense Splitter

A simple Python tool that calculates the net balance of each person in a group and the minimum number of payments needed to settle shared expenses.

## How it works

1. **`parse_expenses()`**: reads each expense from text.
2. **`compute_balances()`**: calculates how much each person is owed (+) or owes (-).
3. **`minimize_transactions()`**: finds the fewest payments to settle all debts.
4. **`format_report()`**: prints the result in a readable way *(in progress)*.

## Input format

One expense per line:

```
payer;amount;participant1,participant2,...
```

Example: `Alice;30;Alice,Bob,Carol` means Alice paid 30 shared equally by Alice, Bob and Carol.

## Usage

Requires Python 3.9 or later. No external libraries needed.

```bash
python expense_splitter.py
```

## Example

Input:

```
Alice;30;Alice,Bob,Carol
Bob;12;Bob,Carol
```

Balances: Alice +20, Bob -4, Carol -16

Payments: Carol pays Alice 16, Bob pays Alice 4

## Team: Internet Monkeys

| Member | Function |
|---|---|
| Matteo Mastrosanti ([mastroky](https://github.com/mastroky)) | `parse_expenses()` |
| Rubén Cerro Díaz ([rubencerroo](https://github.com/rubencerroo)) | `compute_balances()` |
| Raúl Cortés Caballero ([Nhorac](https://github.com/Nhorac)) | `minimize_transactions()` |
| Álvaro Alemán Cabello | `format_report()` |

## License

This project is licensed under the [MIT License](LICENSE).
