
#Collection
#Key value pair
#A "bag" of values, each with its own label(key)

shopping = dict()

shopping['Milk'] = 2
shopping['Fruits'] = 5
shopping['Pizza'] = 1

print(shopping)
print(shopping['Pizza'])

shopping['Pizza'] = shopping['Pizza']+2
print(shopping)

shopping['Fruits'] = 10
print(shopping)

print('Banana' in shopping)

# Read friend name and add it in Dictionary with count

friends= dict()
while True:
    friend=input('Enter friend name: ')
    if friend == 'Done': break
    if friend in friends:
        friends[friend] = friends[friend]+1
    else:
        friends[friend] = 1
print(friends)

# Read friends list  and count

friends = dict()
lst = ['John', 'Jim', 'Tom', 'Tim', 'Jim', 'John', 'Henry']

for friend in lst:
    if friend not in friends:
        friends[friend]=1
    else:
        friends[friend]=friends[friend]+1
print(friends)

#using get()

friends= dict()
lst = ['John', 'Jim', 'Tom', 'Tim', 'Jim', 'John', 'Henry']

for friend in lst:
    friends[friend]=friends.get(friend,0)+1
print(friends)

# dictionary to get word count in line

count = dict()
user_line = input('Enter a line: ')

words = user_line.split()
print(words)

for word in words:
    count[word] = count.get(word,0)+1
print('Counts:',count)

# dictionary to get word count in file

count = dict()
user_file = input('Enter a file name: ')

fh=open(user_file)

for line in fh:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count)

# Retrieving lists of keys and values

Shopping = {'Banana':6,'Bread':2,'Milk':1}

for k in Shopping:
    print(k,Shopping[k])

print(list(shopping))

print(shopping.keys())

print(shopping.values())

print(shopping.items())

#Two iteration variables

for k,v in Shopping.items():
    print(k,v)

# shopping item with max value
maxkey = None
maxvalue = None
for k,v in shopping.items():
    if maxvalue is None or v>maxvalue:
        maxkey = k
        maxvalue = v

print(k,v)

# output : Error
stuff = dict()
print(stuff['candy'])

# output : -1
stuff = dict()
print(stuff.get('candy',-1))

#program to read through the emails.txt and
#figure out who has sent the greatest number of mail messages.
#The program looks for 'Mail:' lines and
#takes the third word of those lines as the person who sent the mail.
#The program creates a dictionary that maps the sender's mail address
#to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a loop to find the maximum one.
#Mail: from abc@xyz.com Fri Feb  8 10:11:26 2010
name = input("Enter file:")
if len(name) < 1: name = "emails.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('Mail:'): continue
    words = line.split()
    word = words[2]
    counts[word] = counts.get(word, 0) + 1

print(counts)

maxmail = None
maxnumber = None
for k, v in counts.items():
    if v > maxnumber or maxnumber is None:
        maxmail = k
        maxnumber = v
print(maxmail, maxnumber)
