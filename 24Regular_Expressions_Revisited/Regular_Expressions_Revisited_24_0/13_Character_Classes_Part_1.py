import re

#string="923698875"
#string="1234"
#string="a234"
#pattern=r"\d{5}" # \d means any character in string must be digits and {5} specify it must at least 5 digits

#string="python"
#pattern=r"\D" # \D means any character in string must be any non digits character

#string="python99"
#pattern=r"\w" # \w means it can contain apha numeric character

#string="user75"
string="u5"
pattern=r"\w{4}"

if re.match(pattern,string):
    print('match found')
else:
    print('match not found')