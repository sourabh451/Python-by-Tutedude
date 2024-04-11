# Characters and character sequences

# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character
# [a-z 0-9] - Set of characters can include a range
# {}

'''
import re
string = "Python 3.0"
#pattern = "[^xyz]"
#pattern = "[a-z 0-9]"
pattern = "[A-Z]"
print(re.findall(pattern,string,flags=0))
'''

'''
import re
string = "pythonnn"
#pattern = "python{2}"
#pattern = "python{1}"
#pattern = "python{0}"
#pattern = "python{3}"
pattern = "python{4}"
print(re.findall(pattern,string,flags=0))
'''

import re
string = "From bobby.mark@mail.com"
pattern = "@([^ ]*)"
print(re.findall(pattern,string,flags = 0))