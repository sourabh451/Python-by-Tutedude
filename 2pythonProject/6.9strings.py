'''
a = 'krishantH'
print(a.capitalize()) # capitalize will capitalize first letter and other upper letter to lower
print(a.upper())
'''

'''
a = '7'
print(a.isnumeric())
print(a.isalpha())
'''

'''
a = 'Mike is a good boy'
print(a.startswith('Mike'))
print(a.startswith('Nick'))
print(a.endswith('boy'))
'''

'''
a = 'Mike is a good boy'
#    012345678
print(a.replace('Mike','Nick'))
print(a.find('a'))
'''

'''
a = '   Mike is a good boy'
print(a)
print(a.lstrip())  # and rstrip will remove space at end of line
print(a.split())  # convert into list
print(a.splitlines())  # whole line convert into list
'''

a = 'Mike','Nick'
print(a) # print in tuple
b =','
print(b.join(a))