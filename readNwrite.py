file = open('test.txt')
#read all contents of file
#print(file.read())
#read N number of characters passing paramter
#print(file.read(17))
#reads a single line at a time
#print(file.readline())



#print line by using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

#values = [apple, bee, cat, dog, etc.]
for line in file.readlines():
    print(line)

file.close()