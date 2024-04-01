#LAMBDA
'''
def add(a):
    return a + 1
res = add(1)
print(res)
'''

# In Lambda arrgument and expression are in single line
#Syntax
# lambda arrgument:expression
fun = lambda a : a + 1
res = fun(2)
print(res)


fun1 = lambda a,b : a + b
res1 = fun1(2,3)
print(res1)