class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ' if current_node.next else '')
            current_node = current_node.next
        print()

    def push_back(self, data: any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def push_front(self, data: any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop_front(self) -> None:
        if not self.head:
            raise IndexError("Pop from empty list")

        self.head = self.head.next

    def pop_back(self) -> None:
        if not self.head:
            raise IndexError("Pop from empty list")

        if not self.head.next:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def insert(self, data: any, index: int) -> None:
        new_node = Node(data)

        if index < 0:
            raise IndexError('Position must be a  non-negative integer')

        if index == 0:
            self.push_front(data)
            return

        current_node = self.head
        current_index = 0

        while current_node and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        if not current_node:
            raise IndexError('Index out of bounds')

        new_node.next = current_node.next
        current_node.next = new_node

    def erase(self, index: int) -> None:
        if index < 0:
            raise IndexError('Index must be a  non-negative integer')

        if not self.head:
            raise IndexError('Erase from empty list')

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_index = 0

        while current_node and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        if not current_node or not current_node.next:
            raise IndexError('Index out of bounds')

        current_node.next = current_node.next.next

    def get_value(self, index: int) -> any:
        if index < 0:
            raise IndexError('Index must be a  non-negative integer')

        if not self.head:
            raise IndexError('List is empty')

        current_node = self.head
        current_index = 0

        while current_node and current_index < index:
            current_node = current_node.next
            current_index += 1

        if not current_node:
            raise IndexError('Index out of bounds')

        return current_node.data

    def get_index(self, data: any) -> int:
        current_node = self.head
        current_index = 0

        while current_node:
            if current_node.data == data:
                return current_index
            current_node = current_node.next
            current_index += 1

        raise ValueError('Value not found in the list')

    def length(self) -> int:
        total_length = 0

        current_node = self.head
        while current_node:
            current_node = current_node.next
            total_length += 1

        return total_length
