from enum import Enum



class TransactionType(Enum):
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'

def get_starting_budget() -> float:
    while True:
        user_input = input("Please enter your starting budget: ")
        try:
            return float(user_input)
        except ValueError:
            print(f"{user_input} cannot be converted to a float. Please enter a float.")

def get_transaction_amount() -> float:
    while True:
        user_input = input("Please enter the amount of the transaction: ")

        try:
            return float(user_input)
        except ValueError:
            print(f"{user_input} cannot be converted to a float. Please enter a float.")
            continue


def get_transaction_type() -> TransactionType:
    while True:
        user_input = input("Enter transaction type (deposit (d) or withdrawal (w)): ")
        aliases = {
            "d": TransactionType.DEPOSIT,
            "deposit": TransactionType.DEPOSIT,
            "w": TransactionType.WITHDRAWAL,
            "withdrawal": TransactionType.WITHDRAWAL
        }
        key = user_input.strip().lower()
        try:
            return aliases[key]
        except KeyError:
            print(f"{user_input} is not a valid input. Please enter a valid transaction type.")
            continue

def process_transaction(total: float, transaction_type: TransactionType, amount: float) -> float:
    
    if transaction_type == TransactionType.DEPOSIT:
        return total + amount
    elif transaction_type == TransactionType.WITHDRAWAL:
        return total - amount

def run_budget_tracker():
    starting_budget = get_starting_budget()
    total = starting_budget
    counter = 0

    while True:
        user_input = input("Enter any value to continue or 'done' to exit: ")
        if user_input.strip().lower() == 'done':
            break
        
        transaction_amount = get_transaction_amount()
        transaction_type = get_transaction_type()
        total = process_transaction(total=total, transaction_type=transaction_type, amount=transaction_amount)
        counter += 1

    print(f"Transactions Entered: {counter}\nFinal Balance: ${total:,.2f}")

if __name__ == "__main__":
    run_budget_tracker()
