#Tuples looks like lists except we use parentheses

fruits= ('Banana','Mango','Kiwi')
print(fruits)
print(fruits[2])
print(len(fruits))

numbers = (1,2,3,4,5)
print(max(numbers))
print(sum(numbers))

#Tuples are Immutable like strings unlike lists
#more efficient then lists

#numbers[3]=6  -->Error
#numbers.sort() --> Error
#numbers.append(5) --> Error
#numbers.reverse() --> Error

# directory output
print(type(numbers))

x=tuple()
print(dir(x))
#count,index

# tuples on left hand side of the assignment
(x,y)=(8,9)
print(y)
(friend,brother,coworker)=('Jim','Tim','Tom')
print(brother)

#(m,n)=7 -->error

# items() methods in dictionaries returns a list of (key,value) tuples

shopping = dict()
shopping['Banana']= 6
shopping['Milk']=1
shopping['Bread']=2

print(shopping)
tuples = shopping.items()
print(tuples)

#Comparison operators

print((2,4,6)>(1,5,7))
print(('Sam','Tom')<('Tim','Jim'))

#Sort by keys

print(sorted(shopping.items()))

#sort by values

shop_rev = list()
for k,v in shopping.items():
    shop_rev.append((v,k))
print(shop_rev)
print(sorted(shop_rev,reverse=True))

# The top 5 most common words in file

count = dict()
user_file = input('Enter a file name: ')

fh=open(user_file)

for line in fh:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1
#print(count)

count_rev = list()
for k,v in count.items():
    count_rev.append((v,k))
#print(count_rev)
#print(sorted(count_rev,reverse=True))

count_top5 = sorted(count_rev,reverse=True)

for v,k in count_top5[:5]:
    print(k,v)

# shorter version -->List comprehension

print(sorted([(v,k) for k,v in shopping.items()]))


#program to read through the emails.txt and figure out the distribution by hour of the day for
#each of the messages. You can pull the hour out from the 'From ' line by finding the time and
#then splitting the string a second time using a colon. From abc@xyz.com Fri Feb  8 10:11:26 2010
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

name = input("Enter file:")
if len(name) < 1: name = "emails.txt"
fhandle = open(name)

counts = dict()

for line in fhandle:
    if not line.startswith('From '): continue
    words = line.split()
    word = words[5]
    time = word.split(':')
    hour = time[0]

    counts[hour] = counts.get(hour, 0) + 1

count = list()
for k, v in counts.items():
    count.append((k, v))
count_sorted = sorted(count)

for k, v in count_sorted:
    print(k, v)
