import stdiomask
# STRING METHODS

#METHOD: len()
# user info
username = '@johnDThePogue199x'
# check the length of the username to see if it exceeds max-length
if (len(username) > 20):
    print('Username is too long!')
else:
    print('Saved new username!')
    print(f'Username Length: {len(username)}')

# METHOD: .find()
key = "sierra97hopscotch12alpha234*@nile#liy8762dns"

# find the username (begins with an @ ends at #)
username = key[key.find('@'): key.find('#')]
print(f'Username: {username}')

# METHOD: .replace()

# ask the user to enter a new username
new_username_raw = input('Enter a new username: ')
if (new_username_raw):
    # replace the old username with the new user name
    new_username = username.replace('nile', new_username_raw)
    print(new_username)

# IN OPERATOR

# ask the user to set a password
password = input('Enter a password: ')
confirm_password = input('Confirm Password: ')
if (confirm_password in password):
    print('Success!')
else:
    print('Incorrect Password!')
