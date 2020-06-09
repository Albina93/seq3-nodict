# seq3-nodict
For this assignment, you will be using Python classes to create a new object that behaves like a dictionary in python, but you are not allowed to use a built-in dictionary in your implementation.


This assignment focuses on creating a data structure that can be used in other programs, rather than a real-world concrete appliction.  You will create a single class named `NoDict` that performs functions of a dictionary:
- association of key/value pairs
- Ability to insert new key/value entry or update existing entry
- Ensure that all keys are unique (handles duplicates)
- Look up a value when given a key
- Delete a key/value entry

# Objectives
- Understand how dictionaries work under the hood
- Learn what `hashing` is and how to apply it
- Apply principles of [Object Composition](https://realpython.com/inheritance-composition-python/) to a solution

# Instructions
We will use the principle of _Object Composition_ to create the `NoDict` class.  This means that the primary `NoDict` class will be composed of a collection of smaller class objects called `Nodes`.  Each Node object represents a single key/value pair.  The keys and values of a dictionary should be kept together, otherwise the benefit of _associative mapping_ that dictionaries provide becomes lost.  The job of the `NoDict` class is to manage the `Nodes` and provide interface methods that can be easily used by a programmer.  The `Node` class itself is not used directly by a programmer, but it is a private working part of the `NoDict` class.

## Part A

- Define a class named `Node` that can be initialized with a key (mandatory) and a value (optional)
- The key and the value should be stored as instance variables within `Node`.
- Within the Node class, define and implement python "dunder" methods for `__init__`,  `__repr__`, and `__eq__`
- The Node class should print a human-readable representation of it's key/value contents when asked. For example, this is not very readable
```python
>>> print(Node("Kevin", 21))
<__main__.Node object at 0x7f4b24f33580>
```
This is more readable, and shows the contents of the Node:
```python
>>> print(Node("Kevin", 21))
Node(k="Kevin" v=21)
```
- The Node class should hash it's own key, and keep that hash value as an instance variable.  This hash value will be used by the NoDict class.
- The Node class object should be able to compare itself to other Node objects using the Python built-in `==` operator.  For example
```python
n1 = Node('Mike', 21)
n2 = Node('Mike', 34)
n3 = Node('Nick', 56)
print(f'n1 == n2 ? {n1 == n2}')
print(f'n2 == n3 ? {n2 == n3}')
```
This should output
```
n1 == n2 ? True
n2 == n3 ? False
```
- Each method defined in the Node class should have a docstring.

# Part B


# References
