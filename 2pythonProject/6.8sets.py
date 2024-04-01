# type of collection
# unordered
# unique elements
# {}

'''
set1 = {1,2,3,4,5,1}
print(set1) # output {1, 2, 3, 4, 5} only unique elements
set1.add(6)
print(set1)
set1.remove(1)
print(set1)
print(2 in set1)
print(6 in set1)
print(1 in set1)
'''

'''
set1 = {1,2,3,4,5}
set2 = {2,3,5,7}
print(set1 & set2) # intersection of two sets
print(set1.union(set2))
'''

set1 = {1,2,3,4,5}
set2 = {1,2,3}
print(set2.issubset(set1))