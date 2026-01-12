import pytest
from bank import BankAccount

def test_deposit():
    acc = BankAccount("A1", 1000)
    acc.deposit(500)
    assert acc.balance == 1500

def test_withdraw():
    acc = BankAccount("A1", 1000)
    acc.withdraw(400)
    assert acc.balance == 600

def test_insufficient_balance():
    acc = BankAccount("A1", 300)
    with pytest.raises(ValueError):
        acc.withdraw(500)

def test_mini_statement():
    acc = BankAccount("A1", 1000)
    acc.deposit(200)
    acc.withdraw(100)
    assert len(acc.mini_statement()) == 2
