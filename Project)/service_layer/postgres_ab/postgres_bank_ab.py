from abc import ABC, abstractmethod

from entities.bank_account import BankAccount


class BankPostgresAb(ABC):
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
    def deposit_into_account(self, account_id, amount):
        pass

    def withdraw_from_account(self, account_id, amount):
        pass

    def transfer_to_account(self, transfer_id, receive_id, amount: int):
        pass