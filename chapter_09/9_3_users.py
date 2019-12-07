#!/usr/bin/env python3


class User:
    """Users of a system.
    """
    def __init__(self, first_name, last_name, username):
        """Creates users of a system.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Username: " + self.username)

    def greet_user(self):
        print("Welcome, " + self.first_name + " " + self.last_name + "!")


my_user1 = User("John",  "Wayne", "westernbadass")
my_user2 = User("Julia", "Child", "culinarybadass")
my_user3 = User("Muhatma", "Ghandi", "peacefulbadass")

my_users = [my_user1, my_user2, my_user3]

for my_user in my_users:
    my_user.describe_user()
