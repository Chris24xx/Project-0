from data_access_layer.abstract_classes.Bank_dao import BankDao
from entities.bank_account import BankAccount

from util.connections import connection


class BankPostgresDaoImp(BankDao):

    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:
        sql = "insert into bankaccounts values (default, %s, %s) returning account_id"
        c = connection.cursor()
        c.execute(sql, (bank_account.customer_id, bank_account.balance))
        connection.commit()
        account_id = c.fetchone()[0]
        bank_account.account_id = account_id
        return bank_account

    def get_bank_account(self, account_id: int) -> BankAccount:
        sql = "select * from bankaccounts where account_id = %s"
        c = connection.cursor()
        c.execute(sql, [account_id])
        bank_record = c.fetchone()
        bank_account = BankAccount(*bank_record)
        return bank_account

    def get_all_bank_accounts(self) -> list[BankAccount]:
        sql = "select * from bankaccounts"
        c = connection.cursor()
        c.execute(sql)
        bank_records = c.fetchall()
        bank_list = []
        for bank_account in bank_records:
            bank_list.append(BankAccount(*bank_account))
        return bank_list

    def update_bank_account(self, bank_account: BankAccount) -> BankAccount:
        sql = "update bankaccounts set  customer_id = %s, balance = %s where account_id = %s"
        c = connection.cursor()
        c.execute(sql, (bank_account.customer_id, bank_account.balance, bank_account.account_id))
        connection.commit()
        return bank_account

    def delete_bank_account(self, account_id: int) -> bool:
        sql = "delete from bankaccounts where account_id = %s"
        c = connection.cursor()
        c.execute(sql, [account_id])
        connection.commit()
        return True

    def transfer(self, amount: int, transfer_id, receive_id):
        sql = "update bankaccounts set balance = balance - %s where account_id = %s"
        sql2 = "update bankaccounts set balance = balance + %s where account_id = %s"
        c = connection.cursor()
        c.execute(sql, (amount, transfer_id))
        c.execute(sql2, (amount, receive_id))
        connection.commit()
        return True

    def get_all_accounts_by_customer_id(self, customer_id):
        sql = "select * from bankaccounts where customer_id = %s"
        c = connection.cursor()
        c.execute(sql, [customer_id])
        bank_records = c.fetchall()
        bank_list = []
        for bank_account in bank_records:
            bank_list.append(BankAccount(*bank_account))
        return bank_list
