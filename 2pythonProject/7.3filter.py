#FILTER
#filter (function, itarable)

def even(a):
    return a%2==0

numbers = [1,2,3,4,5,6,7]

#ans = list(filter(even, numbers))
ans = set(filter(even, numbers))
print(ans)

# in lambda
#ans2 = set(filter(lambda b : b%2==0, numbers))
ans2 = set(filter(lambda b : b%2==0, range(11)))
print(ans2)