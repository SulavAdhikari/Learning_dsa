class Queue:
    def __init__(self):
        self.queue = []

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        if len(self.queue) <= 0:
            return True
        else:
            return False

    def push(self, val):
        self.queue.append(val)
    
    def remove(self):
        return self.queue.pop(0)

    def get_queues(self):
        return self.queue