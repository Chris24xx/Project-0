class BankAccount:
    def __init__(self, account_id, customer_id, balance=0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.balance = balance

    def make_dictionary(self):
        return {
            "balance": self.balance,
            "accountId": self.account_id,
            "customerId": self.customer_id
        }
