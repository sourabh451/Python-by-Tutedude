import re

#string="ac"
#string="abc"
string="abbc"
pattern="ab*c" # character before * can be repeated 0 or more time

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')