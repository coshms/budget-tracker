import builtins
from datetime import datetime
import pytest

import budget_tracker as bt


def test_process_transaction_deposit():
    out = bt.process_transaction(100.0, bt.TransactionType.DEPOSIT, 25.5)
    assert out == 125.5


def test_process_transaction_withdrawal():
    out = bt.process_transaction(100.0, bt.TransactionType.WITHDRAWAL, 40.25)
    assert out == pytest.approx(59.75)


@pytest.mark.xfail(reason="Would be nicer to raise on unknown type; current code returns None")
def test_process_transaction_unknown_type_raises():
    class FakeType:  # not in the Enum
        pass
    # EXPECTED (future): raise ValueError
    with pytest.raises(ValueError):
        bt.process_transaction(100.0, FakeType(), 10.0)


def test_record_transaction_appends_and_sets_timestamp():
    txs = []
    bt.record_transaction(txs, bt.TransactionType.DEPOSIT, 10.0, note="first")
    assert len(txs) == 1
    tx = txs[0]
    assert tx.ttype is bt.TransactionType.DEPOSIT
    assert tx.amount == 10.0
    assert isinstance(tx.ts, datetime)
    assert tx.note == "first"


def test_summarize_counts_and_totals():
    txs = []
    bt.record_transaction(txs, bt.TransactionType.DEPOSIT, 100.0)
    bt.record_transaction(txs, bt.TransactionType.WITHDRAWAL, 30.0)
    bt.record_transaction(txs, bt.TransactionType.DEPOSIT, 20.0)
    s = bt.summarize(txs)
    assert s["deposits_count"] == 2
    assert s["withdrawals_count"] == 1
    assert s["deposits_total"] == pytest.approx(120.0)
    assert s["withdrawals_total"] == pytest.approx(30.0)
    assert s["net_total"] == pytest.approx(90.0)


def test_fmt_money_formats_two_decimals():
    assert bt.fmt_money(1234.5) == "$1,234.50"
    assert bt.fmt_money(0) == "$0.00"
