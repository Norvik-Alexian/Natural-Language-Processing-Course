myfile = open('files/text.txt', 'r')

print(myfile.read())

myfile.seek(0)

print('\n', myfile.read(), '\n')

myfile.seek(0)
content = myfile.readlines()

for line in content:
    print(line.split()[0])

myfile.close()

with open('files/text.txt', 'w+') as file:
    file.write('This is a new text')
    file.read()

with open('files/text_2.txt', 'a+') as file:
    file.write('My first line in this file')