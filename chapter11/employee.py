#!/usr/bin/env python3


class Employee:
    """A class to model an employee."""

    def __init__(self, first_name, last_name, salary):
        """Create a new employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give an employee a raise."""
        self.salary += amount
