from data_access_layer.Implementation_classes.bank_account_dao_postgres_imp import BankPostgresDaoImp
from entities.bank_account import BankAccount

bank_dao = BankPostgresDaoImp()

bank_account = BankAccount(3, 2, 500)
update_account = BankAccount(2, 1, 100)


def test_create_bank_account():
    account = bank_dao.create_bank_account(bank_account)
    assert account.account_id != 0

    # grabs information about the accounts


def test_get_bank_account():
    result = bank_dao.get_bank_account(6)
    assert result.customer_id == 2


# grab all of the accounts information

def test_get_all_bank_accounts():
    result = bank_dao.get_all_bank_accounts()
    assert len(result) >= 3


# update accounts information.

def test_update_bank_account():
    result = bank_dao.update_bank_account(update_account)
    assert result.balance == update_account.balance


# delete accounts

def test_delete_bank_account():
    result = bank_dao.delete_bank_account(3)
    assert result


# function to have multiple sql statements to handle taking and receiving accounts balance information.

def test_transfer():
    result = bank_dao.transfer(100, 6, 5)
    assert result


def test_get_all_customer_accounts():
    result = bank_dao.get_all_accounts_by_customer_id(2)
    assert len(result) >= 2
