class vegetables:

    def __init__(self,carrot,beans):
        self.carrot = carrot
        self.beans = beans

    def __add__(self, other):
        carrot = self.carrot + other.carrot
        beans = self.beans + other.beans
        return vegetables(carrot,beans)

v1 = vegetables(5,3)
v2 = vegetables(7,8)
v3 = v1 + v2
print(v3.carrot)
print(v3.beans)
