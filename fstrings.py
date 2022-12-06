# user profile
username = 'example123'
avatar = '''
. .
\_/
'''
post = 'Type anything'
post = input('Enter a post: ')

# create a display by dynamically inserting user data with fstrings
display = f'''
              CONSOLiii
             __________
            |          |
            |          |
            | {avatar} |
            |          |
            ------------
             @{username}
    _____________________________
   |                             |
   |                             |
   |           {post}            |
   |                             |
   |_____________________________|
'''
print(display)
