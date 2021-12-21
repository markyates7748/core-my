from importlib.machinery import SourceFileLoader
import requests
import os

# get defined methods
populate_bank = SourceFileLoader('bank_producer' ,'aline_files/aline-bank-microservice-my/python-data-producer/bank_producer.py').load_module()
populate_branch = SourceFileLoader('branch_producer', 'aline_files/aline-bank-microservice-my/python-data-producer/branch_producer.py').load_module()
populate_applicant = SourceFileLoader('applicant_producer', 'aline_files/aline-underwriter-microservice-my/python-data-producer/applicant_producer.py').load_module()
populate_user = SourceFileLoader('user_producer', 'aline_files/aline-user-microservice-my/python-data-producer/user_producer.py').load_module()
populate_transaction = SourceFileLoader('transaction_producer', 'aline_files/aline-transaction-microservice-my/python-data-producer/transaction_producer.py').load_module()

# login to api services to get bearer token
login_info = {
    'username' : 'adminUser',
    'password' : 'Password*8'
}
login_response = requests.post('http://localhost:8070/login', json=login_info)
bearer_token = login_response.headers['Authorization']
auth = {'Authorization' : bearer_token}

# execute methods to populate db
print("Populating banks")
populate_bank.populate_bank(auth)
print("Populating branches")
populate_branch.populate_branch(auth)
print("Populating applications")
app_out = populate_applicant.populate_applicant(auth)
print("Populating users")
populate_user.populate_user(auth, app_out[0])
print("Populating transactions")
populate_transaction.populate_transaction(auth, app_out[1])