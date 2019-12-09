#!/usr/bin/env python3

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'James Tiberius Kirk' work?"""
        formatted_name = get_formatted_name('james', 'kirk', 'tiberius')
        self.assertEqual(formatted_name, 'James Tiberius Kirk')


unittest.main()
