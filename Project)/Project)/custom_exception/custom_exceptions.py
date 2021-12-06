class AccountTaken(Exception):
    def __init__(self, message: str):
        self.message = message


class NotEnoughFunds(Exception):
    def __init__(self, message: str):
        self.message = message


class NoNegativeNumbers(Exception):
    def __init__(self, message: str):
        self.message = message


class AccountDoesNotExist(Exception):
    def __init__(self, message: str):
        self.message = message
