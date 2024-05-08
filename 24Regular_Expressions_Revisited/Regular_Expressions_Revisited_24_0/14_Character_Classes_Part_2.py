import re
# Python python
#string="Python"
#string="python"
#pattern=r"^[Pp]ython"

#string="python"
#string="Python"
#pattern=r"^[a-z]"

string="Python"
pattern=r"^[a-zA-Z]"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')