class BankAccount:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0

    def dictionary(self):
        return {
            "balance": self.balance,
            "accountId": self.account_id
        }
