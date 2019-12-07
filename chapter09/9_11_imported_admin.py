#!/usr/bin/env python3

from admin import Admin


my_admin = Admin("John", "Wayne", "johnwayne", 0, ["can change acls"])
my_admin.greet_user()
my_admin.describe_user()
