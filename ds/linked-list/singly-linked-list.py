#! /bin/python3


# Singly linked list

# Node
#   - Value
#   - Next

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def add_new(self, value=None):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, value=None):
        if not self.head:
            self.head = Node(value)
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        new_node = Node(value)
        last_node.next = new_node

    def add_after(self, after, value):
        if not self.head:
            self.head = Node(value)
            return

        this_node = self.head

        while this_node.value != after:
            this_node = this_node.next

        next_node = this_node.next
        new_node = Node(value)
        this_node.next = new_node
        new_node.next = next_node

    def print_list(self):
        this_node = self.head

        while this_node:
            if this_node.next:
                print(this_node.value, "->", end="")
            else:
                print(this_node.value, "->", "None")
            this_node = this_node.next


def main():
    new_list = SLL()
    new_list.add_new("Two")
    new_list.add_end("One")
    new_list.add_new("Three")
    new_list.add_new("Four")
    new_list.add_new("Six")
    new_list.add_after("Six", "Five")

    new_list.print_list()

    return


if __name__ == "__main__":
    main()
