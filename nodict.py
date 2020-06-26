#!/usr/bin/env python3


class Node:
    """A class that represents a key/value pair, with a hash"""
    def __init__(self, key, value=None):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


class NoDict:
    def __init__(self, num_buckets=10):
        pass

    def __repr__(self):
        """How this class renders its data when printed"""
        pass

    def add(self, key, value):
        """Inserts a new key-value Node into the NoDict"""
        pass

    def get(self, key):
        """Lookup the value of a key"""
        pass

    def __getitem__(self, key):
        """Implements [] lookup operator"""
        pass

    def __setitem__(self, key, value):
        """Implements [] assignment operator"""
        pass
