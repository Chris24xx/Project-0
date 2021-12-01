from data_access_layer.abstract_classes.Bank_dao import BankDao
from entities.bank_account import BankAccount


class BankPostgresDaoImp(BankDao):
    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    def get_bank_account(self, account_id: int) -> BankAccount:
        pass

    def get_all_bank_accounts(self) -> list[BankAccount]:
        pass

    def update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    def delete_bank_account(self, account_id: int) -> bool:
        pass

    def deposit_into_bank_account(self, account_id: int, amount: int):
        pass

    def withdraw_into_bank_account(self, account_id: int, amount: int):
        pass

    def transfer_into_bank_account(self, account_id: int, account_id2: int, amount):
        pass