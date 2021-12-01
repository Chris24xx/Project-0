from data_access_layer.abstract_classes.customers_dao import CustomerDao
from entities.Customers import Customers
from util.connections import connection


class CustomersPostgresDao(CustomerDao):
    def create_customer(self, customer: Customers):
        sql = "insert into Customers values(%s, %s, default) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    def get_customer_info(self, customer_id) -> Customers:
        sql = "select * from Customers where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customers(*customer_record)
        return customer

    def get_all_customers(self) -> list[Customers]:
        sql = "select * from Customers"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customer_list = []
        for customer in customer_records:
            customer_list.append(Customers(*customer))
        return customer_list

    def update_info(self, customer: Customers) -> Customers:
        sql = "update Customers set first_name = %s, last_name = %s where customer_id = %s"
        c = connection.cursor()
        c.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer(self, customer_id) -> bool:
        sql = "delete from Customers where customer_id = %s"
        c = connection.cursor()
        c.execute(sql, [customer_id])
        connection.commit()
        return True
