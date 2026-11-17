def parse_expenses(lines):
    expenses = []
    for line in lines:
        payer, amount, people = line.split(";")
        participants = [p.strip() for p in people.split(",")]
        expenses.append((payer.strip(), float(amount), participants))
    return expenses

#add another function to calculate balances here


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
    balances = calculate_balances(expenses) #to be implemented
    transactions = minimize_transactions(balances)


if __name__ == "__main__":
    main()