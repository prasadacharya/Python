
print('***While Loop 1***')
n=7
while(n>0):
    print(n)
    n=n-1
print('after loop 1 ')
print('n=', n)

print('***While Loop 2***')
while True:
    user_input = input('Enter your input: ')
    if(user_input[0]=='#'):
        continue
    if(user_input=='done'):
        break
    print(user_input)
print('end of loop 2')

print('***For loop 1***')
for i in [1,2,3,4,5,6]:
    print(i)

print('***For loop 2***')
friends = ['harry potter', 'batman', 'joker']
for friend in friends:
    print('Happy birthday', friend)

print('***For loop 3***')
large = -1
items = [23,67,25,88,45]

for i in items:
    if i>large:
        large=i

print('largest number: ', large)

print('***For loop 4***')
count = 0

for item in [10, 20, 30, 40, 50, 60, 70, 80]:
    count = count + 1
print('Number of items in array:', count)


print('***For loop 5***')
sum = 0

for item in [10, 20, 30, 40, 50, 60, 70, 80]:
    sum = sum + item
print('Sum of all items in array:', sum)

print('***For loop 6***')
count = 0
sum = 0
avg = 0

for item in [10, 20, 30, 40, 50, 60, 70, 80]:
    count = count + 1
    sum = sum + item

avg = sum/count
print('avg of all items in array:', avg)


print('***For loop 7***')

arr = [10, 20, 30, 40, 50, 60, 70, 80]

for item in arr:
   if item>50:
       print('Large number',item)

print('***For loop 7***')

arr = [10, 20, 30, 40, 50, 60, 70, 80]
found=False
for item in arr:
   if item==50:
       found = True
       break

print ('Found', found)

print('***For loop 8***')

arr = [100, 10, 20, 30, 40, 10, 5, 50, 60, 70, 80]
small= arr[0]


for item in arr:
   if item < small:
       small = item


print ('smallest', small)