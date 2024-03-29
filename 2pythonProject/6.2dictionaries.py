dictionary = {'a':'apple','b':'ball','c':'cat','d':'dog'}
dictionary['e'] = 'elephant'
print(dictionary)
del(dictionary['c'])
print(dictionary)
print('b' in dictionary)
print('g' in dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.get('g',"'g' not found"))