course = 'Python course for "beginners"'
print(course)
# write a multiline string
user_data = '''
fname: "Taylor"
lname: "Lautner"
star_sign: "Virgo"
occupation: "Werewolf"
'''
# print the multiline string
print(user_data)
# get the character at a specific index of a string
alphabet = 'a b c d e f g'
i = 8
# print out the letter 'e' from the string
print(f'{alphabet[i]} is at index position {i} of this string')
# get the last two characters of a string
dob = '01/09/97'
print(f"yy: {dob[-2]}{dob[-1]}")
# print out all characters from index 8 until last character
code = '1287390enigma9879213'
print(f'The secret code is: {code[7:13]}')
print(code.count('8'))
# destructure the string "ample" from "example"
word = "example"
print(word[2:])
# print all characters excluding last
print(word[:-1])
# print all characters using index search ([])
print(word[:])
# destructure month from date string
date = '1807/01/22'
print(date[5:7])
# determine age from date
year = int(date[0:4])
month = int(date[5])
day = int(date[-2:-1])
current_year = 2022
current_month = 12
month_length_in_days = 31
how_old = f'''
You are,
{current_year - year} years,
{current_month - month} months & 
{month_length_in_days - day} days old
'''
print(how_old)
