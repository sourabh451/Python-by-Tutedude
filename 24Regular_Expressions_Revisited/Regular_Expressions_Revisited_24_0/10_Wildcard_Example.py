import re

#string="acb"
#string="achb"
#string="acbb"
#string="abbh"
string="abh"
pattern=r"a.b" # character between . can be any character or any number of character

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')