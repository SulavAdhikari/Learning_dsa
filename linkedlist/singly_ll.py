# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def add_after(self, to_add, after_this):
    current = self.head
    while(current.data != after_this):
      current = current.next
    current.next = Node(data=to_add, next=current.next)

class LLoutput():
  
  def __init__(self, linkedlist):
    self.linkedlist = linkedlist

    # print method for the linked list
  def print_ll(self,):
    current = self.linkedlist.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.add_after(10, 4)
LL_output = LLoutput(LL)

LL_output.print_ll()

