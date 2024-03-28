'''
#1:
file1 = open('5.4my_file.txt','r')
#statements()
reading_file = file1.read() #we can give parentheses 5 then Hello will be displayed
print(reading_file)
file1.close()
'''

'''
#1:
file1 = open('5.4my_file.txt','r')
#statements()
reading_file = file1.readline() #will read the first line
print(reading_file)
file1.close()
'''

'''
#1:
file1 = open('5.4my_file.txt','r')
#statements()
reading_file = file1.readlines() #it combines into list
print(reading_file)
file1.close()
'''

#2:
with open('5.4my_file.txt','r') as file1:
    reading_file = file1.read()
    print(reading_file)