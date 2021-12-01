from custom_exception.custom_exceptions import DuplicateId
from data_access_layer.Implementation_classes.customers_postgres_dao import CustomersPostgresDao
from entities.Customers import Customers
from service_layer.postgres_ab.postgres_customer_ab import PostgresAB


class PostgresServiceImp(PostgresAB):
    def __init__(self, customer_dao):
        self.customer_dao: CustomersPostgresDao = customer_dao

    def service_create_customer(self, customer: Customers):
        customers = self.customer_dao.get_all_customers()
        for customer_in_list in customers:
            if customer_in_list.account_id == customer.account_id:
                raise DuplicateId("account is already in use")
        created_customer = self.customer_dao.create_customer(customer)
        return created_customer

    def service_get_customer_info(self, customer_id) -> Customers:
        return self.customer_dao.get_customer_info(customer_id)

    def service_update_info(self, customer: Customers) -> Customers:
        customers = self.customer_dao.get_all_customers()
        for cus_in_list in customers:
            if cus_in_list.customer_id != customer.customer_id:
                if cus_in_list.account_id == customer.account_id:
                    raise DuplicateId("account is already in use")
        updated_cus = self.customer_dao.update_info(customer)
        return updated_cus

    def service_delete_customer(self, customer_id) -> bool:
        return self.customer_dao.delete_customer(customer_id)
