from data_access_layer.Implementation_classes.customers_postgres_dao import CustomersPostgresDao
from entities.Customers import Customers


customer_dao = CustomersPostgresDao()

customer = Customers("test", "test", 0, 2)
updated_cus = Customers("was", "update", 3, 3)


def test_create_customer():
    new_customer: Customers = customer_dao.create_customer(customer)
    assert new_customer.customer_id != 0


def test_get_customer_info():
    cus = customer_dao.get_customer_info(1)
    assert cus.first_name == "get"


def test_delete_customer_info():
    cus_del = customer_dao.delete_customer(2)
    assert cus_del


def test_update():
    update = customer_dao.update_info(updated_cus)
    assert update.first_name == updated_cus.first_name
