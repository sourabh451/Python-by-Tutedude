import re

'''
string="ababc"
pattern="a"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')
'''

string="babc"
pattern="a"

if re.search(pattern,string):
    print('match found')
else:
    print('match not found')