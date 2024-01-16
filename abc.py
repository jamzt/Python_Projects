from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your pruchase amount: ",amount)
        #this f passes in an arg, but not what kind data and how
        @abstractmethod 
        def payment(self, amount):
            pass

class DebitCardPayment(car):
#defining how to implement the mayment function from its parent paySlip class
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit'.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")

