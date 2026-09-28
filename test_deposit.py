import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(0)

def test_deposit_100(account):
    account.deposit(100)
    assert account.balance == 100

def test_deposit_50(account):
    account.deposit(50)
    assert account.balance == 50
