#!/usr/bin/env python3

from user import User


class Admin(User):
    """A specific type of user."""
    def __init__(self, first_name, last_name, username, login_attempts=0,
                 privileges=[]):
        super().__init__(first_name, last_name, username, login_attempts)
        self.privileges = Privileges(privileges)


class Privileges:
    """Stores the privileges of users"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
