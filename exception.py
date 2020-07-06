user_input = input('Enter a positive number: ')

try:
    ival_input = int(user_input)
except:
    ival_input = -1

if(ival_input>0):
    print('Valid number', ival_input )
else:
    print('Invalid number')
