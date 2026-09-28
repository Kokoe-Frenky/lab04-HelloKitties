def test_withdraw_100(funded_account):
    funded_account.withdraw(100)
    assert funded_account.balance == 900


def test_withdraw_500(funded_account):
    funded_account.withdraw(500)
    assert funded_account.balance == 500