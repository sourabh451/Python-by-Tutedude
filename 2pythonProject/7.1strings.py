'''
def add(i,j):
    return i + j
a = add
res = a(1,2)
print(res)
'''

'''
def add(i,j):
    return i + j
def call(i,j):
    return add(i,j)
res = call(1,2)
print(res)
'''

def add(i,j):
    return i + j
def call(i,j):
    return add(i,j)

def pas(i,j,fn):
    return fn(i,j)

res = pas(1,2, call)
print(res)