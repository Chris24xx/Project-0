from abc import abstractmethod, ABC

from entities.bank_account import BankAccount


class BankServiceAb(ABC):

    @abstractmethod
    def service_create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_get_bank_account(self, account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def service_get_all_bank_accounts(self) -> list[BankAccount]:
        pass

    @abstractmethod
    def service_update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_delete_bank_account(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_deposit_into_bank_account(self, account_id: int, amount: int):
        pass

    @abstractmethod
    def service_withdraw_from_bank_account(self, account_id: int, amount: int):
        pass

    @abstractmethod
    def service_transfer_into_bank_account(self, account_id: int, account_id2: int, amount):
        pass