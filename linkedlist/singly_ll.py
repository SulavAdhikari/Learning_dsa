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
      
  def display(self,):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

  def return_str(self,):
    return_str = ""
    current = self.head
    while(current):
      return_str += str(current.data)
      current = current.next
    return return_str




