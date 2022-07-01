#username input

name = input("Please type your name ")
if len(name) < 3:
    print('That name is not long enough')
elif len(name) > 50:
    print('That name is too long')
else: 
    print('That\'s a cool name')