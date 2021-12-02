from data_access_layer.abstract_classes.Bank_dao import BankDao
from entities.bank_account import BankAccount


class BankDaoImp(BankDao):
    dummy_account = BankAccount(1)
    dummy_2 = BankAccount(2)
    dummy_del = BankAccount(3)
    bank_list = [dummy_account, dummy_2, dummy_del]
    bank_generator_id = 3

    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        bank_account.account_id = BankDaoImp.bank_generator_id
        BankDaoImp.bank_generator_id += 1
        BankDaoImp.bank_list.append(bank_account)
        return bank_account

    def get_bank_account(self, account_id: int) -> BankAccount:
        for bank_account in BankDaoImp.bank_list:
            if bank_account.account_id == account_id:
                return bank_account

    def get_all_bank_accounts(self) -> list[BankAccount]:
        return BankDaoImp.bank_list

    def update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        for bank_account_in_list in BankDaoImp.bank_list:
            if bank_account_in_list.account_id == bank_account.account_id:
                index = BankDaoImp.bank_list.index(bank_account_in_list)
                BankDaoImp.bank_list[index] = bank_account
                return bank_account

    def delete_bank_account(self, account_id: int) -> bool:
        for account_in_list in BankDaoImp.bank_list:
            if account_in_list.account_id == account_id:
                index = BankDaoImp.bank_list.index(account_in_list)
                del BankDaoImp.bank_list[index]
                return True

    def deposit_into_bank_account(self, account_id: int, amount: int):
        for account_in_list in BankDaoImp.bank_list:
            if account_in_list.account_id == account_id:
                info = BankAccount(account_in_list)
                info.balance += amount
                return info.balance

    def withdraw_into_bank_account(self, account_id: int, amount: int):
        for account_in_list in BankDaoImp.bank_list:
            if account_in_list.account_id == account_id:
                info = BankAccount(account_in_list)
                info.balance -= amount
                return info.balance

    def transfer_into_bank_account(self, account_id: int, account_id2: int, amount):
        pass
