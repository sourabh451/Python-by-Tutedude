'''
class simple:

    def __init__(self):
        self.value_1 = 1
        self.value_2 = 2

    def __A1_(self): #double under score means private
        print("apple")

    def _B2_(self):
        print("ball")

s = simple()
print(s.value_1)
s._simple__A1_()

print(dir(s))
'''

class simple:

    def __init__(self):
        self.__value_1 = 1
        #self._value_1 = 1
        self.value_2 = 2

    def __A1_(self): #double under score means private
        print("apple")

    def _B2_(self):
        print("ball")

s = simple()
#print(s.__value_1)
#print(s._value_1)

print(dir(s))
print(s._simple__value_1)


