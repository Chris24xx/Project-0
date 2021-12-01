from abc import ABC, abstractmethod

from data_access_layer.Implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.Customers import Customers


class CustomerServiceAb(ABC):
    customer_DAO_imp = CustomerDaoImp

    @abstractmethod
    def service_create_customer(self, customer: Customers):
        pass

    # get customer info
    @abstractmethod
    def service_get_customer_info(self, customer_id) -> Customers:
        pass

    # update information
    @abstractmethod
    def service_update_info(self, customer: Customers) -> Customers:
        pass

    # delete information by id
    @abstractmethod
    def service_delete_customer(self, customer_id) -> bool:
        pass