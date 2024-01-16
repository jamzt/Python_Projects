from abc import ABC, abstractmethod
class electronics(ABC):
    def Device(self, size):
        print("The size of this device is ",size)

        #this f passes in an arg, but not what kind data and how
        @abstractmethod 
        def screen(self, size):
            pass

class Monitor(electronics):
#defining how to implement the payment function from its parent Device class
    def screen(self, size):
        print('The size of this device is {} and doesn\'t meet your requirement'.format(size))

obj = Monitor()
obj.Device("75inch")
obj.screen("34inch")
