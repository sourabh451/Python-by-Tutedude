import re

#string="9123698875"
#string="23698875"
#string="923698875"
#pattern=r"^91" # character after ^ must match the pattern

string="923698875"
pattern=r"^9"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')