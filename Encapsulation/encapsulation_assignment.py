
# Python Ver:   3.9
#
# Author:       Melbae Abernathy
#
# Purpose:      Encapsulation Demo. Demonstrating OOP, private attribute and protected attribute,
#               
#
# Tested OS:  This code was written and tested to work with Windows 10.


class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 60
print(obj._protectedVar)

class Protected:
    def __init__(self):
        self._privateVar = 15

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self._privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(25)
obj.getPrivate()
        
