
from data_access_layer.Implementation_classes.customers_postgres_dao import CustomersPostgresDao
from entities.Customers import Customers
from service_layer.postgres_ab.postgres_customer_ab import PostgresAB


class PostgresServiceImp(PostgresAB):
    def __init__(self, customer_dao):
        self.customer_dao: CustomersPostgresDao = customer_dao

    def service_create_customer(self, customer: Customers):
        return self.customer_dao.create_customer(customer)

    def service_get_customer_info(self, customer_id) -> Customers:
        return self.customer_dao.get_customer_info(customer_id)

    def service_get_all_customers(self):
        return self.customer_dao.get_all_customers()

    def service_update_info(self, customer: Customers) -> Customers:
        return self.customer_dao.update_info(customer)

    def service_delete_customer(self, customer_id) -> bool:
        return self.customer_dao.delete_customer(customer_id)
