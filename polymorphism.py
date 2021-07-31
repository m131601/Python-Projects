#Parent Class User

class User:
    name = "Melbae"
    email = "melbaeabernathyliveops@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your name: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

#This is the same method in the parent class "User".
#The difference is that, instead of using entry_password, we using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")


#Child Class Customer
class Customer(User): 
    mailing_address = ' '
    mailing_list = True

#This is the same method in the parent class "User".
#The difference is that, instead of using entry_password, we using entry_address.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_address = input("Enter your address: ")
        if (entry_email == self.email and entry_address == self.address):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The address or email is incorrect")

#The following code invoke the methods inside each class for User, Employee and Customer.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
