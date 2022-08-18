#! /bin/python3

# Doubly linked list

# Node
#   - Value
#   - Prev
#   - Next


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_new(self, value):
        if not self.head:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            return

        first_node = self.head
        new_node = Node(value)

        self.head = new_node
        new_node.next = first_node
        first_node.prev = new_node

    def add_end(self, value=None):
        if not self.head:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            return

        new_node = Node(value)
        last_node = self.tail
        self.tail = new_node
        last_node.next = new_node
        new_node.prev = last_node

    def print_list(self):
        this_node = self.head

        while this_node:
            if this_node.next:
                print(this_node.value, "->", end="")
            else:
                print(this_node.value, "->", "None")

            this_node = this_node.next

    def print_reverse(self):
        this_node = self.tail

        while this_node:
            if this_node.prev:
                print(this_node.value, "->", end="")
            else:
                print(this_node.value, "->", "None")
            this_node = this_node.prev


def main():
    new_list = DLL()
    new_list.add_new("Four")
    new_list.add_new("Three")
    new_list.add_new("Two")
    new_list.add_new("One")
    new_list.add_end("Five")

    new_list.print_list()
    new_list.print_reverse()

    return


if __name__ == "__main__":
    main()
