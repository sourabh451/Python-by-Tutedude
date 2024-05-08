import re

#string="abb"
#string="ab"
#pattern="ab{2}" # character before {} must present as specified in brace or more time

#string="abb"
string="abbb"
pattern=r"ab{3}"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')