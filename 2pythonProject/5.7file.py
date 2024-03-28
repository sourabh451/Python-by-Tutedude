# r+ ---> write and read

file = open('5.7my_file.txt','r+')
writing_file = file.write('Welcome')
print(writing_file)
file.close()

file = open('5.7my_file.txt','r+')
reading_file = file.read()
print(reading_file)
file.close()
