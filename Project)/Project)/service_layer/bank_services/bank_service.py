from data_access_layer.Implementation_classes.bank_account_dao_postgres_imp import BankPostgresDaoImp
from entities.bank_account import BankAccount
from service_layer.bank_services.bank_service_abstract import BankServiceAb
from custom_exception.custom_exceptions import *


class BankService(BankServiceAb):
    def __init__(self, bank_dao):
        self.bank_dao: BankPostgresDaoImp = bank_dao

    def service_create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        return self.bank_dao.create_bank_account(bank_account)

    def service_get_bank_account(self, account_id: int) -> BankAccount:
        return self.bank_dao.get_bank_account(account_id)

    def service_get_all_bank_accounts(self) -> list[BankAccount]:
        return self.bank_dao.get_all_bank_accounts()

    def service_update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        accounts = self.bank_dao.get_all_bank_accounts()
        for existing_account in accounts:
            # if existing_account.account_id in accounts:
            if existing_account.account_id == bank_account.account_id:
                if existing_account.customer_id != bank_account.customer_id:
                    raise AccountTaken("This Account is not yours")
        # else:
        #     raise AccountDoesNotExist("This account does not exist")
        return self.bank_dao.update_bank_account(bank_account)

    def service_delete_bank_account(self, account_id: int) -> bool:
        return self.bank_dao.delete_bank_account(account_id)

    def service_deposit_into_bank_account(self, account_id: int, amount: int):
        account = self.service_get_bank_account(account_id)
        if amount <= -1:
            raise NoNegativeNumbers("no negative deposits")
        account.balance += amount
        updated_account = self.service_update_bank_account(account)
        return updated_account

    def service_withdraw_from_bank_account(self, account_id: int, amount: int):
        account = self.bank_dao.get_bank_account(account_id)
        if amount < -1:
            raise NoNegativeNumbers("can't withdraw negative amounts")
        account.balance += amount
        updated_account = self.service_update_bank_account(account)
        return updated_account

    def service_transfer_into_bank_account(self, transfer_id: int, receive_id: int, amount):
        account = self.bank_dao.get_bank_account(transfer_id)
        if amount < -1:
            raise NoNegativeNumbers("No negative funds")
        if account.balance < amount:
            raise NotEnoughFunds("Not Enough Funds!")
        return self.bank_dao.transfer(amount, transfer_id, receive_id)

    def get_all_accounts_by_customer_id(self, customer_id):
        return self.bank_dao.get_all_accounts_by_customer_id(customer_id)
