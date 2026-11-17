def parse_expenses(lines):
    expenses = []
    for line in lines:
        payer, amount, people = line.split(";")
        participants = [p.strip() for p in people.split(",")]
        expenses.append((payer.strip(), float(amount), participants))
    return expenses

# An expense: (payer, amount, participants)
Expense = tuple[str, float, list[str]]


# Function to calculate balances
def compute_balances(expenses: list[Expense]) -> dict[str, float]:
    """
    Compute the net balance of each person.

    Args:
        expenses (list[Expense]): (payer, amount, participants) for each expense.

    Returns:
        dict[str, float]: Balance per person (positive = is owed, negative = owes).

    Raises:
        ValueError: If an expense has no participants.
    """
    # Start with an empty balance for the group
    balances: dict[str, float] = {}

    # Go through every expense
    for payer, amount, participants in expenses:
        # Split the amount equally among the participants (an expense needs at least one)
        try:
            share: float = amount / len(participants)
        except ZeroDivisionError:
            raise ValueError(f"Expense paid by {payer} has no participants")

        # The payer gets back the whole amount they paid
        balances[payer] = balances.get(payer, 0.0) + amount

        # Each participant (payer included) owes their share
        for person in participants:
            balances[person] = balances.get(person, 0.0) - share

    # Return the net balance of each person
    return balances


def minimize_transactions(balances: dict[str, float]) -> list[tuple[str, str, float]]:
    """
    Given a dictionary of balances, returns a list of transactions to settle debts.
    """
    debtors = []
    creditors = []
    
    for name, balance in balances.items(): # check if balance is negative or positive and add to debtors or creditors list
        if balance < -0.005:
            debtors.append([name, -balance])
        elif balance > 0.005:
            creditors.append([name, balance])
            
    debtors.sort(key=lambda x: x[1], reverse=True) # sort debtors and creditors by amount owed/owed to
    creditors.sort(key=lambda x: x[1], reverse=True)
    
    transfers = []
    i = 0
    j = 0
    
    while i < len(debtors) and j < len(creditors): # while there are still debtors and creditors to process
        amount = round(min(debtors[i][1], creditors[j][1]), 2) # calculate the amount to transfer
        transfers.append((debtors[i][0], creditors[j][0], amount))
        
        debtors[i][1] -= amount # update the debtor's balance
        creditors[j][1] -= amount # update the creditor's balance
        
        if debtors[i][1] < 0.005: # if the debtor's balance is close to zero, move to the next debtor
            i += 1
        if creditors[j][1] < 0.005: # if the creditor's balance is close to zero, move to the next creditor
            j += 1
            
    return transfers # return the list of transfers


def main():
    lines = ["Alice;30;Alice,Bob,Carol", "Bob;12;Bob,Carol"]
    expenses = parse_expenses(lines)
    balances = compute_balances(expenses)
    transactions = minimize_transactions(balances)
    # TEMPORARY: test prints, remove when format_report() is implemented
    print(balances)
    print(transactions)


if __name__ == "__main__":
    main()