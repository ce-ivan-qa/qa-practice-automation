

#read the file and store all lines in list
#reverse the list
#write the list back to the file
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

a = 1
while a <= 4:
  b = a * 2
  a = a + 2
  print(b)

