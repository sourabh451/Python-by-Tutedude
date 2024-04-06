# Regular Expression
# regex
# strings
# import re
# validate the input

#1: match()
import re

pattern = "apple"

#if re.match(pattern,"apple"):
#if re.match(pattern,"appleapple"): # true because it take 1st five words
if re.match(pattern,"appappleball"): # false because it take 1st five words
    print("True")
else:
    print("False")