
'''
class const_dest:
    x = 0

    def __init__(self):
        print("Constructed")

    def __del__(self):
        print("Destructed")

cd = const_dest()
'''

# self helps to access atributes and methods

class const_dest:
    x = 0

    def __init__(self,color,type):
        self.color = color
        self.type = type
        print("Constructed")

    def __del__(self):
        print("Destructed")

cd = const_dest("black","SUV")
print(cd.color)
print(cd.type)

cd_1 = const_dest("red","sedan")
print(cd_1.color)
print(cd_1.type)