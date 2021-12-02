from abc import ABC, abstractmethod

from entities.bank_account import BankAccount


class BankDao(ABC):
    # creates accounts
    @abstractmethod
    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    # grabs information about the accounts
    @abstractmethod
    def get_bank_account(self, account_id: int) -> BankAccount:
        pass

    # grab all of the accounts information
    @abstractmethod
    def get_all_bank_accounts(self) -> list[BankAccount]:
        pass

    # update accounts information.
    @abstractmethod
    def update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    # delete accounts
    @abstractmethod
    def delete_bank_account(self, account_id: int) -> bool:
        pass

    # function to have multiple sql statements to handle taking and receiving accounts balance information.
    @abstractmethod
    def transfer(self,  amount, transfer_id, receive_id):
        pass
