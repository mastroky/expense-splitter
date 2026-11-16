def parse_expenses(lines):
    expenses = []
    for line in lines:
        payer, amount, people = line.split(";")
        participants = [p.strip() for p in people.split(",")]
        expenses.append((payer.strip(), float(amount), participants))
    return expenses

def main():
    lines = ["Alice;30;Alice,Bob,Carol", "Bob;12;Bob,Carol"]
    expenses = parse_expenses(lines)


if __name__ == "__main__":
    main()