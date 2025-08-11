from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import List


class TransactionType(Enum):
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'

# --- data model ---
@dataclass
class Transaction:
    ttype: TransactionType
    amount: float
    ts: datetime
    note: str | None = None

# --- helper: format currency ---
def fmt_money(value: float) -> str:
    return f"${value:,.2f}"

def record_transaction(transactions: List[Transaction],
                       ttype: TransactionType,
                       amount: float,
                       note: str | None = None) -> None:
    """Append a new transaction to the in-memory list."""
    transactions.append(Transaction(ttype=ttype, amount=amount, ts=datetime.now(), note=note))

def summarize(transactions: List[Transaction]) -> dict:
    """Return aggregates you can print (counts and totals by type and net)."""
    summary = {
        "deposits_count": 0,
        "deposits_total": 0.0,
        "withdrawals_count": 0,
        "withdrawals_total": 0.0,
        "net_total": 0.0
    }
    for tx in transactions:
        if tx.ttype == TransactionType.DEPOSIT:
            summary['deposits_count'] += 1
            summary['deposits_total'] += tx.amount
        elif tx.ttype == TransactionType.WITHDRAWAL:
            summary["withdrawals_count"] += 1
            summary["withdrawals_total"] += tx.amount
    summary['net_total'] = summary['deposits_total'] - summary['withdrawals_total']
    return summary

# --- print summary nicely ---
def print_summary(starting_budget: float, ending_total: float, summary: dict) -> None:
    print("\n=== Session Summary ===")
    print(f"Starting Balance: {fmt_money(starting_budget)}")
    print(f"Deposits:   {summary['deposits_count']} (total {fmt_money(summary['deposits_total'])})")
    print(f"Withdrawals:{summary['withdrawals_count']} (total {fmt_money(summary['withdrawals_total'])})")
    print(f"Net Change: {fmt_money(summary['net_total'])}")
    print(f"Final Balance: {fmt_money(ending_total)}")

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

# --- prompt for a note per transaction ---
def maybe_get_note() -> str | None:
    """Ask user for an optional note; empty -> None."""
    note = input("Add a note for this transaction? (optional, press Enter to skip): ").strip()
    return note or None

def process_transaction(total: float, transaction_type: TransactionType, amount: float) -> float:
    
    if transaction_type == TransactionType.DEPOSIT:
        return total + amount
    elif transaction_type == TransactionType.WITHDRAWAL:
        return total - amount

def run_budget_tracker():
    starting_budget = get_starting_budget()
    total = starting_budget
    transactions: List[Transaction] = []

    while True:
        user_input = input("Add a transaction? (Press Enter to continue or 'done' to exit): ")
        if user_input.strip().lower() == 'done':
            break
        
        transaction_amount = get_transaction_amount()
        transaction_type = get_transaction_type()
        note = maybe_get_note()

        # record and apply
        record_transaction(transactions=transactions, ttype=transaction_type, amount=transaction_amount, note=note)
        total = process_transaction(total=total, transaction_type=transaction_type, amount=transaction_amount)

    summary = summarize(transactions=transactions)
    print(f"Transactions Entered: {len(transactions)}")
    print_summary(starting_budget=starting_budget, ending_total=total, summary=summary)

if __name__ == "__main__":
    run_budget_tracker()
