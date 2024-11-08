# Lab 1

# f = open("about_me.txt", "a")

# f.write('\n')
# f.write('Perfect night out: dinner somewhere in the Loop, walk through Grant Park')

# f.close()

# f = open("about_me.txt", "r")

# print(f.readlines(25))
# print(f.readlines(25))
# print(f.readlines(25))

# f.close()


# Lab 2

f = open("pi_million_digits.txt", 'r')

# print(f.read(250))

pi_lines = f.readlines()

f.close()

user_birthday = input('Enter your birthday in the format MMDDYY: ')
bday_found = None

for i in pi_lines:
    if user_birthday in i:
        print(f'Your birthday is in the first million digits of pi!')
        bday_found = 1
        break


pi_string = ''

for i in pi_lines:
    pi_string += i.strip()

if bday_found != 1:
    print('Your birthday was not found')
else: 
    birthday_pos = pi_string.index(user_birthday) - 1
    print(f'Your birthday begins at decimal place {birthday_pos}')