class ProtectedVar:
    def __init__ (self):
        self.protectedVar = "This is the first protected function."
#using protected method to create obect
object = ProtectedVar()
object.protectedVar = "This is a new function."
print(object.protectedVar)


class Protected:
    def __init__ (self):
        self.__privateVar = "Testing private function.This will be replaced."

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
#using private method to create obect and give it a new value
object = Protected()
object.getPrivate()
object.setPrivate("New replaced private function.")
object.getPrivate()

 