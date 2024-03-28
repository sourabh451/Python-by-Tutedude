#1:
file1 = open('5.3my_file.txt','r')
#directory= specify the location
#mode= r,w,a,r+w
file1.close()

#2:
with open('5.3my_file.txt','w') as file1:
    #statements