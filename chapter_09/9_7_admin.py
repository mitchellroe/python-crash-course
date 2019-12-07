#!/usr/bin/env python3


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


class Admin(User):
    """A specific type of user.
    """
    def __init__(self, first_name, last_name, username, login_attempts=0,
                 privileges=[]):
        """This is a function that initializes some stuff.
        """
        super().__init__(first_name, last_name, username, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin = Admin("John", "Wayne", "johnwayne", 0,
              ['can change passwords', 'can delete posts', 'can ban user'])

admin.show_privileges()
