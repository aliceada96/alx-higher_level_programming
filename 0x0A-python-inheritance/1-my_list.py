#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """Returns elements present in the list"""

    def print_sorted(self):
        """Returns My_list elements in acending order"""
        print(sorted(self))
