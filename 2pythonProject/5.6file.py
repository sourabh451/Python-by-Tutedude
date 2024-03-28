file1 = open('5.6my_file.txt','w')
writing_file = file1.write('Hello ')
file1.close()

file1 = open('5.6my_file.txt','a')
appending_file = file1.write('Welcome to this lecture.')
file1.close()

file1 = open('5.6my_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()