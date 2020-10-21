# This module implements a in order to implement iterative dfs and different uses
# Implementing a stack is a nice way to practice OOP in python
# Programmer : Dor Bitton

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    ## that way we dont see the last arrow.

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def Top(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from empty stack")
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1


if __name__ == "__main__":
    stk = Stack()
    for i in range(1, 11):
        stk.push(i)

    print(stk)
    print(stk.isEmpty())
    stk.pop()
    stk.pop()
    print(stk)
    print(stk.Top())
