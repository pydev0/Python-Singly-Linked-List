# Python Singly Linked List

This repository contains a Python implementation of a singly linked list data structure. The linked list supports various operations, such as inserting, deleting, and retrieving elements. This README provides an overview of the class and its methods.

## Class Definition

### `Node`

Represents a node in the linked list.

**Constructor:**

- `__init__(self, data: any) -> None`: Initializes a node with the given data and sets the next node to `None`.

**Attributes:**

- `data`: The value stored in the node.
- `next`: A reference to the next node in the list.

### `LinkedList`

Represents a singly linked list.

**Constructor:**

- `__init__(self) -> None`: Initializes an empty linked list with the head set to `None`.

**Methods:**

- `print_list(self) -> None`: Prints all elements in the list, separated by arrows (`->`). Ends with a newline.

- `push_back(self, data: any) -> None`: Appends a new node with the given data to the end of the list.

- `push_front(self, data: any) -> None`: Inserts a new node with the given data at the beginning of the list.

- `pop_front(self) -> None`: Removes the node at the beginning of the list. Raises an `IndexError` if the list is empty.

- `pop_back(self) -> None`: Removes the node at the end of the list. Raises an `IndexError` if the list is empty.

- `insert(self, data: any, index: int) -> None`: Inserts a new node with the given data at the specified index. Raises an `IndexError` if the index is negative or out of bounds.

- `erase(self, index: int) -> None`: Removes the node at the specified index. Raises an `IndexError` if the index is negative or out of bounds.

- `get_value(self, index: int) -> any`: Retrieves the value of the node at the specified index. Returns the node's data. Raises an `IndexError` if the index is negative or out of bounds.

- `get_index(self, data: any) -> int`: Finds the index of the first node with the given data. Returns the index. Raises a `ValueError` if the data is not found in the list.

- `length(self) -> int`: Returns the number of nodes in the list.

## Example Usage

Here's an example of how to use the `LinkedList` class:

```python
# Create a new linked list
linked_list = LinkedList()

# Add elements to the end
linked_list.push_back(10)
linked_list.push_back(20)

# Print the list
linked_list.print_list()  # Output: 10 -> 20 -> 30

# Add elements to the beginning
linked_list.push_front('Name')
linked_list.push_front(True)

# Print the list
linked_list.print_list()  # Output: True -> Name -> 10 -> 20 -> 30

# Insert an element at index 1
linked_list.insert(15, 1)
linked_list.print_list()  # Output: True -> Name -> 10 -> 15 -> 20 -> 30

# Remove the element at index 2
linked_list.erase(2)
linked_list.print_list()  # Output: True -> Name -> 15 -> 20 -> 30

# Get the value at index 1
print(linked_list.get_value(1))  # Output: Name

# Get the index of a value
print(linked_list.get_index(30))  # Output: 4

# Get the length of the list
print(linked_list.length())  # Output: 5
