print('Hello\nWorld')

greeting='Good\nMorning'

print(greeting)
print(len(greeting))

print('This program will print file data')

myfile = open('FirstProgram.py')
for data in myfile:
    print(data)

print('This program will print Total number of Lines in a file ')
fh = open('exception.py', "r")

count = 0
for line in fh:
    count = count + 1
print("Total number of Lines: ",count)

print('This program will print Total number of Lines in a file which starts with-for ')
fh = open('Loop.py', "r")
for line in fh:
    if line.startswith('for'):
        print(line.strip())

print('This program will print Total number of Lines in a file which starts with-while ')
fh = open('Loop.py', "r")
for line in fh:
    line=line.strip()
    if not line.startswith('while'):
        continue
    print(line)

print('This program will prompt for file name and print number of lines which starts with-while ')

user_file=input('Enter file name:')
try:
    fh=open(user_file)
except:
    print('Invalid File', user_file)
    quit()

count = 0
for line in fh:
    if line.startswith('while'):
        count=count+1
print("Total number of while Lines: ", count)


# This program  prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case

filename = input("Enter file name: ")

fh = open(filename)

for line in fh:
    line=line.strip()
    print(line.upper())