
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

print('For loop 1')
for i in [1,2,3,4,5,6]:
    print(i)

print('For loop 2')
friends = ['harry potter', 'batman', 'joker']

for friend in friends:
    print('Happy birthday', friend)




