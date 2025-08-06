while True:
    starting_budget_input = input("Please enter your starting budget: ")
    try:
        starting_budget = int(starting_budget_input)
        break
    except ValueError:
        print(f"{starting_budget_input} cannot be converted to an integer. Please enter an integer.")


print("Now lets add income and expenses.\nPlease enter 'i' for income, 'e' for expense or 'done' to exit.")

total = starting_budget
counter = 0
while True:
    transaction_amount_input = input("Please enter the amount of the transaction: ")

    if transaction_amount_input == 'done':
        break

    try:
        transaction_amount = int(transaction_amount_input)
    except ValueError:
        print(f"{transaction_amount_input} cannot be converted to an integer. Please enter an integer.")
        continue

    income_or_expense = input("Is this income (i) or expense (e)? ")

    if income_or_expense == 'i':
        total += int(transaction_amount)
        counter += 1
    elif income_or_expense == 'e':
        total -= int(transaction_amount)
        counter += 1
    else:
        print("Invalid entry. Please use 'i' for income, 'e' for expense.")
        continue

print(f"Transactions entered: {counter}\nFinal balance: {total}")
