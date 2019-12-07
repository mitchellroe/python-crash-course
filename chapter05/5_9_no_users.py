#!/usr/bin/env python3

# usernames = ['medlib_site', 'admin', 'medlib_fpm']
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello, ' + username + ', would you like to see a status'
                  + ' report?')
        else:
            print('Hello, ' + username + ', thank you for logging in today.')
else:
    print('We need to find some users!')
