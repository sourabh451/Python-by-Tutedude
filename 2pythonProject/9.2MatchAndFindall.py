# match(pattern, string, flags)
'''
import re

pattern = "apple"
if re.match(pattern,"apple"):
    print("True")
else:
    print("False")
'''

# findall (pattern, string, flags)

import re
pattern = "apple"
#string = re.findall("apple",pattern)
#string = re.findall("app",pattern)
string = re.findall("xyz",pattern)
print(string)

