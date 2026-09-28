def test_shared_fixture(funded_account):
    funded_account.withdraw(200)
    assert funded_account.balance == 800