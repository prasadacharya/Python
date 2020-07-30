
#DATA STRUCTURES
#Collection


#Simple List
print([1,10,100])
print([1,10,[100,1000],10000])
print(['Mango','Kiwi','Banana'])
friends = ['Tim','Tom','Jim']
print(friends)
print(friends[1])

# List with for loop

for i in [1,2,3,4,5]:
    print(i)

for friend in friends:
    print('Hello',friend)


#Mutable

friends[2]='Jimmy'
print(friends)

#Length

print(len(friends))

#Range

print(range(len(friends)))

for i in range(len(friends)):
    print('Friend '+str(i)+' is',friends[i])


#Concatinating Strings

numbers = [1,2,3]
fnu=friends+numbers
print(fnu)

#Slicing
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[1:4])
print(numbers[:4])
print(numbers[5:])
print(numbers[:])

#type
print(type(numbers))

#List Methods
x=list()
print(type(x))
print(dir(x))

#append

Shopping_List=list()
Shopping_List.append('Banana')
Shopping_List.append(99)
Shopping_List.append('Milk')
print(Shopping_List)

# in and not in

print(2 in numbers)
print(5 not in numbers)

#sort
friends.sort()
print(friends)

#Built in Functions

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))
print(sum(numbers)/len(numbers))

# Program to accept user input numbers, store it in list, print sum and avg

user_numbers = list()
while True:
    n=input('Enter number; ')
    if (n=='done'): break
    val=int(n)
    user_numbers.append(val)

print(sum(user_numbers))
print(sum(user_numbers)/len(user_numbers))

#strings and list

#split

greeting= "Good Morning Dear"

words = greeting.split()
for word in words:
    print(word)

print(words[2])

fruits='banana;grape;Kiwi'
fruit = fruits.split(';')
print(fruit)

#split and parsing

#fh= open(emails.txt)

#for line in fh:
    #line = line.rstrip()
    #if not line.startswith('From ') : continue
    #words = line.split()
    #print(words[2])

line = 'From abc@xyz.com on Sat 10/10/1010'
words=line.split()
print(words)

#double split
email=words[1]
pieces=email.split('@')
print(pieces)
print(pieces[1])


# Open the file and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

file_name = input("Enter file name: ")
fh = open(file_name)
lst = list()
for line in fh:
    line=line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

#Open the file and read it line by line.
#When you find a line that starts with '#'
#You will parse the line using split() and
#print out the Second word in the line.
#Then print out of comment lines count at the end.


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "File.py"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith('#'): continue
    words = line.split()
    print(words[1])
    count=count+1

print("There were", count, " comment lines in the file ")
