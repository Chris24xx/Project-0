from custom_exception.custom_exceptions import DuplicateId
from data_access_layer.Implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.Customers import Customers
from service_layer.customer_service_abstract import CustomerServiceAb


class CustomerServiceImp(CustomerServiceAb):
    def __init__(self, customer_dao):
        # are using injection dependency code.
        self.customer_dao: CustomerDaoImp = customer_dao

    def service_create_customer(self, customer: Customers):
        for customer_new in self.customer_dao.customer_list:
            if customer_new.account_id == customer.account_id:
                raise DuplicateId("account is already in use")
            else:
                return self.customer_dao.create_customer(customer)

    def service_get_customer_info(self, customer_id) -> Customers:
        return self.customer_dao.get_customer_info(customer_id)

    def service_update_info(self, customer: Customers) -> Customers:
        return self.customer_dao.update_info(customer)

    def service_delete_customer(self, customer_id) -> bool:
        return self.customer_dao.delete_customer(customer_id)
