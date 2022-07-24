# A single node og a double linked list
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# A linkedlist 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_after(self, add_after, value):
        current = self.head
        while current.data != add_after:
            current=current.next
        newnode = Node(prev=current, data=value, next=current.next)
        current.next = newnode
        newnode.next.prev = newnode

    def insert(self, data):
        if self.head:
            prev=self.head
            current = self.head
            while current.next:
                prev = current
                current = current.next
            current.next = Node(prev=prev, data=data)
        else:
            self.head = Node(data)
            self.tail = self.head

    def print_forward(self,):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
         
        new_node = Node(data)

        # if list is empty
        if self.head is None:
            self.head = new_node
         
        #if node data is smallest
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node
        else:
            current = self.head

            # find new node's destiny
            while ((current.next is not None) and
                   (current.next.data < new_node.data)):
                current = current.next
     
            # connections 
            new_node.next = current.next

            # if new node is not inserted at the end
            if current.next is not None:
                new_node.next.prev = new_node
 
            current.next = new_node
            new_node.prev = current
    
    def printList(self):
 
        node = self.head
        while node:
            print(node.data)
            node = node.next


LL1 = LinkedList()

LL1.insert(1)
LL1.insert(3)
LL1.insert(2)
LL1.add_after(3, 10)

LL2 = SortedLinkedList()
LL2.insert(4)
LL2.insert(1)
LL2.insert(0)
LL2.insert(9)

LL2.printList()
# LL1.print_forward()


