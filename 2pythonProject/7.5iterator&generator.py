# ITERATOR
'''
list = [1,2,3,4,5]

iteration = iter(list)
print(iteration.__next__())
print(iteration.__next__())
print(next(iteration))
'''


# GENERATOR
'''
def fn():

    yield 1
    yield 2
    yield 3

values = fn()

#print(values.__next__())
#print(values.__next__())
#print(values.__next__())


for i in values:
    print(i)
'''


def squares():

    n = 1
    while n <= 5:
        square = n ** 2
        yield square
        n = n + 1

values = squares()
for i in values:
    print(i)