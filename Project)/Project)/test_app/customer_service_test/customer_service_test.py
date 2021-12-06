from custom_exception.custom_exceptions import DuplicateId
from data_access_layer.Implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.Customers import Customers
from service_layer.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDaoImp()
customer_service = CustomerServiceImp(customer_dao)

n_customer = Customers("Christian", "Ayala", 1, 1)


def test_dupe_id():
    try:
        customer_service.service_create_customer(n_customer)
        assert False
    except DuplicateId as e:
        assert str(e) == "account is already in use"
