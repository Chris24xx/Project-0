from flask import Flask, request, jsonify

from custom_exception.custom_exceptions import DuplicateId
from data_access_layer.Implementation_classes.customers_postgres_dao import CustomersPostgresDao
from entities.Customers import Customers
from service_layer.postgres_imp.postgres_service_imp import PostgresServiceImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG,format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
customer_dao = CustomersPostgresDao()
customer_service = PostgresServiceImp(customer_dao)


# create customer
@app.post("/create")
def api_create_customer():
    try:
        customer_data = request.get_json()
        new_customer = Customers(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["customerId"]
        )
        customer_returned = customer_service.service_create_customer(new_customer)
        cust_dict = customer_returned.dict()
        cust_json = jsonify(cust_dict)
        return cust_json
    except DuplicateId as e:
        dict_message = {"message": str(e)}
        exception_json = jsonify(dict_message)
        return exception_json

    # get customer info


@app.get("/customer/<customer_id>")
def api_get_customer_info(customer_id):
    customer_information = customer_service.service_get_customer_info(int(customer_id))
    cust_dict = customer_information.dict()
    cust_json = jsonify(cust_dict)
    return cust_json


# get all customers
@app.get("/customer")
def api_get_all_customers():
    customers_as_customer = customer_service.service_get_all_customers()
    customers_as_dictionary = []
    for customers in customers_as_customer:
        customer_dict = customers.dict()
        customers_as_dictionary.append(customer_dict)
    return jsonify(customers_as_dictionary)


# update information
@app.patch("/customer/<customer_id>")
def api_update_info(customer_id: str):
    customer_data = request.get_json()
    new_customer = Customers(
        customer_data["firstName"],
        customer_data["lastName"],
        int(customer_id)
    )
    updated_cust = customer_service.service_update_info(new_customer)
    cust_dict = updated_cust.dict()
    cust_as_json = jsonify(cust_dict)
    return cust_as_json


# delete information by id
@app.delete("/customer/<customer_id>")
def service_delete_customer(customer_id):
    result = customer_service.service_delete_customer(int(customer_id))
    if result:
        return " you have deleted {} based off of ID all info has been deleted".format(customer_id)
    else:
        return "nope not working"


app.run()
