from random import randint
from typing import Optional


class Node:
    def __init__(self, n: int):
        self.value = n
        self.next = None

class List:
    def __init__(self):
        self.root: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add(self, n: int):
        node = Node(n)
        if self.root:
            self.tail.next = node
            self.tail = node
        else:
            self.root = node
            self.tail = node

    def traverse(self):
        if self.root:
            current_node = self.root
            while current_node:
                print(current_node.value, end='')
                if current_node.next:
                    current_node = current_node.next
                    print(" -> ", end='')
                else:
                    current_node = None
            print('')
        else:
            print("Empty list")


def main():
    linked_list = List()
    for i in range(15):
        linked_list.add(randint(1, 300))

    linked_list.traverse()

    prev = None
    next = None
    current = linked_list.root
    while current:
        next = current.next
        if current != linked_list.root:
            current.next = None
            linked_list.tail = current
        else:
            current.next = prev
        prev = current
        current = next



    linked_list.traverse()


if __name__ == "__main__":
    main()
