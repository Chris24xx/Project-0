from data_access_layer.abstract_classes.customers_dao import CustomerDao
from entities.Customers import Customers


class CustomerDaoImp(CustomerDao):
    new_customer = Customers("test", "test", 1 , 1)
    new_customer_two = Customers("get", "all test", 2 , 2)
    delete_cus = Customers("to", "be deleted", 3, 3)
    customer_list = [new_customer, new_customer_two,delete_cus]
    customer_id = 3

    def create_customer(self, customer: Customers) -> Customers:
        customer.customer_id = CustomerDaoImp.customer_id
        CustomerDaoImp.customer_id += 1
        CustomerDaoImp.customer_list.append(customer)
        return customer

    def get_customer_info(self, customer_id: int) -> Customers:
        for customer in CustomerDaoImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def update_info(self, customer: Customers) -> Customers:
        for customer_in_list in CustomerDaoImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerDaoImp.customer_list.index(customer_in_list)
                CustomerDaoImp.customer_list[index] = customer
                return customer

    def delete_customer(self, customer_id: int) -> bool:
        for customer_in_list in CustomerDaoImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerDaoImp.customer_list.index(customer_in_list)
                del CustomerDaoImp.customer_list[index]
                return True
