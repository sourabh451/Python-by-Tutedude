# search (pattern, string, flags)

import re
pattern = "apple"
if re.search(pattern,"ballapple",flags = 0):
    print("True")
else:
    print("False")


# match
'''
import re
pattern = "apple"
if re.match(pattern,"ballapple",flags = 0):
    print("True")
else:
    print("False")
'''