#!/usr/bin/env python3


class User:
    """Users of a system."""
    def __init__(self, first_name, last_name, username, login_attempts=0):
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
