from abc import ABC, abstractmethod

from entities.bank_account import BankAccount


class BankDao(ABC):

    @abstractmethod
    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def get_bank_account(self, account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def get_all_bank_accounts(self) -> list[BankAccount]:
        pass

    @abstractmethod
    def update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def delete_bank_account(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def deposit_into_bank_account(self, account_id: int, amount:int):
        pass

    @abstractmethod
    def withdraw_into_bank_account(self, account_id:int, amount:int):
        pass

    @abstractmethod
    def transfer_into_bank_account(self, account_id: int, account_id2:int, amount):
        pass
