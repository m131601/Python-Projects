


class User:
    #Define the attribute of the class
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

class Employee(User): #child class
    base_pay = 11.00
    department = 'General'

class Customer(User): #child class
    mailing_address = ' '
    mailing_list = True
