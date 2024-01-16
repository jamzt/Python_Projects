#Parent class User
class User:
    name = "xyz"
    email = "xyz@gmail.com"
    password = "123abc"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input ("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#child class employee
class Employee(User):
    base_pay = 11.00  
    department = "General"
    pin_number = "3980"

#this is the same method in the parent class "User"
#the difference is that instead of using entry_password, we're using entry_pin
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

#the following coder invokes the method inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

 