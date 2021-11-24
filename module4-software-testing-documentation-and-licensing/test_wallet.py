import pytest
from test.wallet import Wallet

'''Without decorators '''
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(20)
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

'''With decorators'''

@pytest.fixture
def empty_wallet():
    # Returns a wallet instance with a zero balance
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet():
    # Returns a wallet of balance 20
    return Wallet(20)

def test_default_initial_amount_dec(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount_dec(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash_dec(wallet):
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_wallet_spend_cash_dec(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10