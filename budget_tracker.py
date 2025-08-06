starting_budget = int(input("Please enter your starting budget: "))
print("Now lets add income and expenses.\nPlease enter 'i' for income, 'e' for expense or 'done' to exit.")

total = starting_budget
counter = 0
while True:
    transaction_amount = input("Please enter the amount of the transaction: ")

    if transaction_amount == 'done':
        break

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
