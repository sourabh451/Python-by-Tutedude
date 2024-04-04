#map
#map (function , iterable)

def squares(a):
    return a ** 2

numbers = [1,2,3,4,5]
ans = list(map(squares , numbers))
print(ans)



def squares_1(b):
    return b ** 2

numbers_1 = [1,2,3,4,5]
res = list(filter(squares_1 , numbers_1))
print(res)


def even(a):
    return a%2==0

numbers_2 = [1,2,3,4,5]
res_2 = list(map(even , numbers_2))
print(res_2)


ans_2 = list(map(lambda a : a ** 2, range(11)))
print(ans_2)