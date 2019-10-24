#!/usr/bin/python3

class Node():
    def __init__(self, data=None):
        self.data = data 
        self.next = None 

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

if __name__=='__main__':
    data = ['h','w','a','r','b','c']
    ll = LinkedList()
    for d in data:
        ll.insert_node(d)

    ll.print_list()
