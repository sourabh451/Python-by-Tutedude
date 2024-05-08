import re

#string="ac"
string="abc"
pattern="ab+c" # character before + must present once

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')