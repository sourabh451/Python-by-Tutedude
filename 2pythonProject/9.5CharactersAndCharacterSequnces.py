# Characters and character sequnces

# ^ - Matches the beginning of a line
# $ - Matches the end of a line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non- digit
# \s - Matches whitespace
# \S - Matches non- whitespace

import re
string = "It is a dog 56"
#pattern = "^I"
#pattern = "g$"
#pattern = "."
#pattern = "^I."
#pattern = "^I..."
#pattern = "\d"
#pattern = "\D"
#pattern = "\s"
pattern = "\S"
print(re.findall(pattern,string,flags=0))