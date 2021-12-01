from abc import ABC, abstractmethod

from entities.Customers import Customers


class CustomerDao(ABC):
    # create customer method
    @abstractmethod
    def create_customer(self, customer: Customers):
        pass

    # get customer info
    @abstractmethod
    def get_customer_info(self, customer_id) -> Customers:
        pass

    # get all customer info
    def get_all_customers(self) -> list[Customers]:
        pass

    # update information
    @abstractmethod
    def update_info(self, customer: Customers) -> Customers :
        pass

    # delete information by id
    @abstractmethod
    def delete_customer(self, customer_id)-> bool:
        pass
