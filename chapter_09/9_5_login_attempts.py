#!/usr/bin/env python3

"""
**9-5: Login Attempts:** Add an attribute called `login_attempts` to your
`User` class from Exercise 9-3 (page 166).  Write a method called
`increment_login_attempts()` that increments the value of `login_attempts` by
1.  Write another method called `reset_login_attempts() that resets the value
of `login_attempts` to 0.

Make an instance of the `User` class and call `increment_login_attempts()`
several times.  Print the value of `login_attempts` to make sure it was
incremented properly, and then call `reset_login_attempts()`.  Print
`login_attempts` again to make sure it was reset to 0.
"""


class User:
    """Users of a system.
    """
    def __init__(self, first_name, last_name, username, login_attempts=0):
        """Creates users of a system.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.login_attempts = login_attempts

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Username: " + self.username)

    def greet_user(self):
        print("Welcome, " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


my_user1 = User("John",  "Wayne", "westernbadass")
my_user1.increment_login_attempts()
print(str(my_user1.login_attempts))
my_user1.increment_login_attempts()
print(str(my_user1.login_attempts))

my_user1.reset_login_attempts()
print(str(my_user1.login_attempts))
