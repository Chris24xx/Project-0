class Customers:
    def __init__(self, first_name: str, last_name: str, customer_id):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id

    def dict(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "customerId": self.customer_id
        }
