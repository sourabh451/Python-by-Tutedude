import re

#string="python-file"
string="pythonfile"
pattern=r"python-?file" # character before ? can be optional

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')