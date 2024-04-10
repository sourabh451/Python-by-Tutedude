# CHARACTERS AND CHARACTER SEQUENCES

# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression 0 to 1 times

import re
string = "From bobby.mark@mail.com"
#pattern = "ma*"
#pattern = "ma+"
#pattern = "^F.*?"
#pattern = "^F.*"
#pattern = "^F.+?"
pattern = "^From (\S+@\S+)"
print(re.findall(pattern, string))