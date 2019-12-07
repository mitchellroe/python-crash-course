#!/usr/bin/env python3

current_users = ['medlib_site', 'admin', 'medlib_fpm', 'John', 'phil', 'ben']
current_users = [current_user.lower() for current_user in current_users]
new_users = ['john', 'phil', 'foo', 'bar', 'baz']
new_users = [new_user.lower() for new_user in new_users]
for new_user in new_users:
    if new_user in current_users:
        print('You need to choose a new username.  ' + new_user + ' is already'
              + ' taken.')
    else:
        print('The username you have chosen, ' + new_user + ' is available.')
