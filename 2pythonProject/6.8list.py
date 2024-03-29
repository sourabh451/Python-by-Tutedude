'''
x = []
for i in range(11):
    z = i ** 2
    x.append(z)
print(x)
'''

# Syntax:
# [expression for item in list]

'''
x = [i ** 2 for i in range(11)]
print(x)
'''

'''
x = []
for i in range(11):
    if i%2 == 0:
        z = i ** 2
        x.append(z)
print(x)
'''

# Syntax:
# [expression for item in list{if (test expression)}]

x = [i ** 2 for i in range(11) if i ** 2 %2 == 0]
print(x)
