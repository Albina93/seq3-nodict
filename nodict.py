#!/usr/bin/env python3


class Node:
    """A class that represents a key/value pair, with a hash"""
    def __init__(self, key, value=None):
        self.hash = None
        self.key = None
        self.value = None
        # Your code here
        return

    def __repr__(self):
        # Your code here
        return

    def __eq__(self, other):
        # Your code here
        return


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = None
        # Your code here

    def __repr__(self):
        """How this class renders its data when printed"""
        # Your code here
        return

    def add(self, key, value):
        """Inserts a new key-value Node into the NoDict"""
        # Your code here
        return

    def get(self, key):
        """Lookup the value of a key"""
        # Your code here
        return

    def __getitem__(self, key):
        """Implements [] lookup operator"""
        # Your code here
        return

    def __setitem__(self, key, value):
        """Implements [] assignment operator"""
        # Your code here
        return
