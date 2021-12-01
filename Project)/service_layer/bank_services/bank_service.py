from data_access_layer.Implementation_classes.bank_dao_imp import BankDaoImp
from entities.bank_account import BankAccount
from service_layer.bank_services.bank_service_abstract import BankServiceAb


class BankService(BankServiceAb):
    def __init__(self, bank_dao):
        self.bank_dao: BankDaoImp = bank_dao

    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        return self.bank_dao.create_bank_account(bank_account)

    def get_bank_account(self, account_id: int) -> BankAccount:
        return self.bank_dao.get_bank_account(account_id)

    def get_all_bank_accounts(self) -> list[BankAccount]:
        return self.bank_dao.get_all_bank_accounts()

    def update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    def delete_bank_account(self, account_id: int) -> bool:
        return self.bank_dao.delete_bank_account(account_id)

    def deposit_into_bank_account(self, account_id: int, amount: int):
        pass

    def withdraw_into_bank_account(self, account_id: int, amount: int):
        pass

    def transfer_into_bank_account(self, account_id: int, account_id2: int, amount):
        pass
