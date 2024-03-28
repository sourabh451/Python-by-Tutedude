file1 = open('5.5my_file.txt','w')
writing_file = file1.write('Hello')
print(writing_file)
file1.close()

file1 = open('5.5my_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()