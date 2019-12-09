#!/usr/bin/env python3

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test the Employee class."""

    def setUp(self):
        self.my_employee = Employee('john', 'jingleheimer-schmidt', 50000)

    def test_give_default_raise(self):
        """
        Does giving the default raise increase an employee's salary by 5000?
        """
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 55000)

    def test_give_custom_raise(self):
        """Can we give only a raise of $25?"""
        self.my_employee.give_raise(25)
        self.assertEqual(self.my_employee.salary, 50025)


if __name__ == '__main__':
    unittest.main()
