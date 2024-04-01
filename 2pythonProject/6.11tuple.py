# tuple
'''
numbers = (1,2,3,4,5)
print(numbers[1])

tup1 = ('Mike',10,2.5)
tup2 = ('pop',1)
print(tup1 + tup2)

tup = (1,'Nick',9.8,'Rio')
print(len(tup))

#lists ----> mutable
numbers = [1,2,3,4,5]
numbers[0] = 0
print(numbers)

#tuple ---> immutable because tuple' object does not support item assignment
numbers = (1,2,3,4,5)
numbers[0] = 0
print(numbers)
'''

tup3 = (2,3,45,21,34,76,789,12,10000)
tup3_sort = sorted(tup3)
print(tup3_sort)
print(tup3.index(789))