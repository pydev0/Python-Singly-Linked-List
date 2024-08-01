from node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node == None:
            self.head = new_node
            return

        while current_node.get_next() != None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def show(self):
        current_node = self.head
        output = ''

        while current_node != None:
            output += str(current_node.get_data()) + '->'
            current_node = current_node.get_next()
        print(output)

    def length(self):
        current_node = self.head
        counter = 0

        while current_node != None:
            counter += 1
            current_node = current_node.get_next()
        print(counter)

    def push_front(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.set_next(current_node)
        self.head = new_node

    def remove_back(self):
        current_node = self.head

        while current_node.get_next().get_next() != None:
            current_node = current_node.get_next()
        current_node.set_next(None)

    def remove_front(self): self.head = self.head.get_next()

    def value_at(self, index):
        counter = 0
        current_node = self.head

        while current_node != None:
            if counter == index:
                return print(current_node.get_data())
            counter += 1
            current_node = current_node.get_next()
        print('Index is out of range')

    def insert(self, data, index):
        new_node = Node(data)
        current_node = self.head
        counter = 0

        while current_node.get_next() != None:
            if index == 0:
                return self.push_front(data)
            elif index == counter + 1:
                next_current_node = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(next_current_node)
                return
            counter += 1
            current_node = current_node.get_next()
        print('Index is out of range')

    def remove(self, index):
        current_node = self.head
        counter = 0

        while current_node.get_next() != None:
            if index == 0:
                return self.remove_front()
            elif index == counter + 1:
                return current_node.set_next(current_node.get_next().get_next())
            counter += 1
            current_node = current_node.get_next()
        print('Index is out of range')

    def reverse(self):
        previous_node = None
        current_node = self.head
        next_node = None

        while current_node != None:
            next_node = current_node.get_next()
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
