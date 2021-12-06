from data_access_layer.Implementation_classes.bank_account_dao_postgres_imp import BankPostgresDaoImp
from entities.bank_account import BankAccount
from service_layer.bank_services.bank_service import BankService
from custom_exception.custom_exceptions import *

bank_dao = BankPostgresDaoImp()

bank_service = BankService(bank_dao)
acc_taken = BankAccount(1, 2, 0)


def test_update_exception_1():
    try:
        bank_service.service_update_bank_account(acc_taken)
        assert False
    except AccountTaken as e:
        assert str(e) == "This Account is not yours"


def test_deposit_exception():
    try:
        bank_service.service_deposit_into_bank_account(1, -200)
        assert False
    except NoNegativeNumbers as e:
        assert str(e) == "no negative deposits"


def test_transfer_exception():
    try:
        bank_service.service_transfer_into_bank_account(1, 2, -100)
        assert False
    except NoNegativeNumbers as e:
        assert str(e) == "No negative funds"


def test_transfer_exception_2():
    try:
        bank_service.service_transfer_into_bank_account(1, 2, 800)
        assert False
    except NotEnoughFunds as e:
        assert str(e) == "Not Enough Funds!"
