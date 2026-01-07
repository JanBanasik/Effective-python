my_tree = (10, (7, None, 9), (13, 11, None))

def contains(tree, value):
    if not isinstance(tree, tuple):
        return tree == value
    
    pivot, left, right = tree

    if value < pivot:
        return contains(left, value)
    elif value > pivot:
        return contains(right, value)
    else:
        return value == pivot
    
print(f"{contains(my_tree, 9)=}")
print(f"{contains(my_tree, 14)=}")

def contains_match(tree, value):
    match tree:
        case pivot, left, _ if value < pivot:
            return contains_match(left, value)
        case pivot, _, right if value > pivot:
            return contains_match(right, value)
        case (pivot, _, _) | pivot:
            return value == pivot
        
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

obj_tree = Node(
    value=10,
    left=Node(value=7, right=9),
    right=Node(value=13, left=11),
)

def contains_class(tree, value):
    if not isinstance(tree, Node):
        return tree == value
    if value < tree.value:
        return contains_class(tree.left, value)
    elif value > tree.value:
        return contains_class(tree.right, value)
    else:
        return value == tree.value
    

def contains_match_class(tree, value):
    match tree:
        case Node(value=pivot, left=left) if value < pivot:
            return contains_match_class(left, value)
        case Node(value=pivot, right=right) if value > pivot:
            return contains_match_class(right, value)
        case Node(value=pivot) | pivot:
            return value == pivot


print(f"JSON RECORDS")
record1 = """{"customer": {"last": "Ross", "first": "Rachel"}}"""
record2 = """{"customer": {"entity": "Steve's Paints"}}"""

from dataclasses import dataclass

@dataclass
class PersonCustomer:
    first_name: str
    last_name: str

@dataclass
class BusinessCustomer:
    company_name: str

import json

def deserialize(data):
    record = json.loads(data)
    match record:
        case {"customer": {"first": first, "last": last}}:
            return PersonCustomer(first_name=first, last_name=last)
        case {"customer": {"entity": company_name}}:
            return BusinessCustomer(company_name=company_name)
        case _:
            raise ValueError("Unknown record type")


print(deserialize(record1))
print(deserialize(record2))
        