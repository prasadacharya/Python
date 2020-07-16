#To print nth letter of string
sport = 'Tennis'
letter = sport[4]
print(letter)

n=5
print(sport[n-1])

#To print length of the string
print(len(sport))

#To print index and letters of string
user_input= input('Enter a string: ')
input_length=len(user_input)
i=0
for letter in user_input:
  print(letter,i)
  i=i+1

#To print number of specific letter in string

user_input= input('Enter a string: ')
user_letter= input('Enter a letter: ')
count = 0
for letter in user_input:
    if(letter==user_letter):
        count=count+1

print('Number of user_letter in user_input: ', count)

#String slicing

s=input('Enter a string: ')

print(s[0:4])
print(s[5:15])
print(s[6:7])
print(s[5:])
print(s[:8])
print(s[:])

#string concatenation

user_input1= input('Enter a string1: ')
user_input2= input('Enter a string2: ')

print(user_input1+' '+user_input2)

if 'd' in user_input1:
    print('Found it!')
else:
    print('Not Found it!')

#String Comparison
user_input1= input('Enter a string1: ')
user_input2= input('Enter a string2: ')

if user_input1 > user_input2:
    print('Greater!')
elif user_input1 < user_input2:
    print('Smaller!')
else:
    print('Same!')

#String Library(built in functions)

greeting=" Good Morning "

print(type(greeting))
print(dir(greeting))

print(greeting.lower())
print("Dear".upper())
print(greeting.find('od'))
print(greeting.find('h'))
print(greeting.replace('Morning','Evening'))
print(greeting.replace('o','0'))
print(greeting.strip())
print(greeting.lstrip())
print(greeting.rstrip())
print(greeting.startswith(' Good'))
print(greeting.startswith(' g'))

#String Parsing and Extracting

data = 'received from firstname_lastname@xyz.com on 05/09/2010'

at_position=data.find('@')
print(at_position)

space_position=data.find(' ',at_position)
print(space_position)

host=data[at_position+1:space_position]
print(host)

#String Parsing and Extracting
text = "Total value is:    0.8475";

colpos = text.find(':')
num=text[colpos+1:]
print(float(num.lstrip()))

#strings and character sets
#unicode

x='hello'
y=u'hello'
print(type(x),type(y))