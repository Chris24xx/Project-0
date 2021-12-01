from data_access_layer.Implementation_classes.customer_dao_imp import CustomerDaoImp
from entities.Customers import Customers

customer_dao_imp = CustomerDaoImp()
customer = Customers("Chris", "Ayala", 1, 4)


def test_create_customer():
    new_customer: Customers = customer_dao_imp.create_customer(customer)
    assert new_customer.customer_id != 0


def test_get_customer_info():
    got_customer: Customers = customer_dao_imp.get_customer_info(1)
    assert got_customer.customer_id == 1


def test_delete_customer_info():
    deleted_customer = customer_dao_imp.delete_customer(3)
    assert deleted_customer


def test_update():
    update_info = Customers("updated", "to", 2, 2)
    update_cus: Customers = customer_dao_imp.update_info(update_info)
    assert update_cus.last_name == update_info.last_name
