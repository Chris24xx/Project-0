from flask import Flask, request, jsonify
from entities.bank_account import BankAccount
from service_layer.bank_services.bank_service import BankService
from custom_exception.custom_exceptions import *
from data_access_layer.Implementation_classes.customers_postgres_dao import CustomersPostgresDao
from data_access_layer.Implementation_classes.bank_account_dao_postgres_imp import BankPostgresDaoImp
from entities.Customers import Customers
from service_layer.postgres_imp.postgres_service_imp import PostgresServiceImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
customer_dao = CustomersPostgresDao()
customer_service = PostgresServiceImp(customer_dao)
bank_dao = BankPostgresDaoImp()
bank_service = BankService(bank_dao)


# create customer
@app.post("/create")
def api_create_customer():
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
def api_delete_customer(customer_id):
    result = customer_service.service_delete_customer(int(customer_id))
    if result:
        return " you have deleted {} based off of ID all info has been deleted".format(customer_id)
    else:
        return "nope not working"


@app.post("/create_account")
def api_create_bank_account():
    bank_data = request.get_json()
    new_bank = BankAccount(
        bank_data["accountId"],
        bank_data["customerId"],
        bank_data["balance"]
    )
    bank_returned = bank_service.service_create_bank_account(new_bank)
    bank_dict = bank_returned.make_dictionary()
    bank_dict_as_json = jsonify(bank_dict)
    return bank_dict_as_json


@app.get("/account/<account_id>")
def api_get_bank_account(account_id: int):
    bank_information = bank_service.service_get_bank_account(int(account_id))
    bank_dict = bank_information.make_dictionary()
    get_json = jsonify(bank_dict)
    return get_json


@app.get("/accounts")
def api_get_all_bank_accounts():
    accounts_as_accounts = bank_service.service_get_all_bank_accounts()
    accounts_as_dict = []
    for accounts in accounts_as_accounts:
        account_dict = accounts.make_dictionary()
        accounts_as_dict.append(account_dict)
    return jsonify(accounts_as_dict)


@app.patch("/account/<account_id>")
def api_update_bank_account(account_id: str):
    bank_data = request.get_json()
    new_info = BankAccount(
        int(account_id),
        bank_data["customerId"],
        bank_data["balance"]
    )
    returned_info = bank_service.service_update_bank_account(new_info)
    info_as_dictionary = returned_info.make_dictionary()
    dictionary_as_json = jsonify(info_as_dictionary)
    return dictionary_as_json


@app.delete("/account/<account_id>")
def api_delete_bank_account(account_id):
    result = bank_service.service_delete_bank_account(account_id)
    if result:
        return " you have deleted {} based off of ID all info has been deleted".format(account_id)
    else:
        return "nope not working"


@app.patch("/account/deposit/<account_id>")
def api_deposit_into_bank_account(account_id: str):
    try:
        bank_data = request.get_json()
        amount = bank_data["amount"]
        int(account_id)
        bank_service.service_deposit_into_bank_account(int(account_id), int(amount))
        return "success you have added {} to your account".format(amount)
    except NoNegativeNumbers as e:
        error_message = {"error": str(e)}
        return jsonify(error_message)


@app.patch("/account/withdraw/<account_id>")
def api_withdraw_from_bank_account(account_id: int):
    try:
        bank_data = request.get_json()
        amount = bank_data["amount"]
        int(account_id)
        bank_service.service_withdraw_from_bank_account(account_id, int(amount))
        return "success you have taken {} from your account".format(amount)
    except NoNegativeNumbers as e:
        error_message = {"error": str(e)}
        return jsonify(error_message)


@app.patch("/account/transfer/<transfer_id>/<receive_id>")
def api_transfer_into_bank_account(transfer_id: str, receive_id: str):
    try:
        data = request.get_json()
        amount = data["amount"]
        bank_service.service_transfer_into_bank_account(int(transfer_id), int(receive_id), int(amount))
        return "success ${} amount was transferred.".format(amount)
    except NoNegativeNumbers as e:
        error = {"error": str(e)}
        return error
    except NotEnoughFunds as e:
        error2 = {"error": str(e)}
        return error2


@app.get("/accounts/customers")
def api_get_all_accounts_by_customer_id(customer_id):
    accounts_as_accounts = bank_service.get_all_accounts_by_customer_id(int(customer_id))
    accounts_as_dict = []
    for accounts in accounts_as_accounts:
        account_dict = accounts.make_dictionary()
        accounts_as_dict.append(account_dict)
    return jsonify(accounts_as_dict)


app.run()
