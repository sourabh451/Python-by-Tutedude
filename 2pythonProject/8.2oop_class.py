# Syntax

# class (name):
#   statements & attributes
#   ...

# class the class
# statements

#1:
'''
class car:
    pass #if you dont want to send any statements & attributes
# then send pass operation it a null operator

car_1 = car()
print(car_1)
'''

#2:
'''
class car:
    color = "black"

car_1 = car()
print(car_1.color)
'''

#3

class car:
    color = "black"
    type = "SUV"

car_1 = car()
print(car_1.color.upper())
print(car_1.color.isalpha())

# . ==> dot notation (it can hold method and attributes)