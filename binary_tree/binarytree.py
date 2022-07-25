class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # uses recursive function
    def insert(self, data):
        if self.data:
            # if data is smaller than parent then puts in left
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # if data is larger than parent then puts in right
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # uses recursive function to find 
    def exists(self, to_search):
        if to_search < self.data:
            if self.left is None:
                return False
            return self.left.exists(to_search)
        elif to_search > self.data:
            if self.right is None:
                return False
            return self.right.exists(to_search)
        else:
            return True

  

