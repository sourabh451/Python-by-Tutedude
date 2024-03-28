'''
#1: Syntax error
a=2
if a<1:
    print('hello')
else  # colon is missing
    print('welcome')
'''

'''
#2: indentation error
a=2
if a<1:
    print('hello')
else:
print('welcome')  # indentation missing
'''

'''
#3: zero division error
print(8/0)
'''

'''
#4: module error
import mathematics
print(mathematics.pi)
'''

'''
#5: type error
a=2
b='5'
print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#6: Logic error
a=2
b=2
print(a * b) #If we want to add but * sign multipy


