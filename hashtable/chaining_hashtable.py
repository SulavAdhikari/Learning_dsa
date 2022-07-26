class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None

class HashMap:
    SIZE = 1000

    def __init__(self):
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]

    def put(self, key, value):
        head = self.hashing[key % self.SIZE]
        current = head.next
        while current:
            if current.key == key: break
            current = current.next
        else:
            current = ListNode(key)
            current.next = head.next
            head.next = current
        current.val = value

    def get(self, key):
        current = self.hashing[key % self.SIZE].next
        while current:
            if current.key == key: 
                break
            current = current.next
        else:
            return None
        return current.val

    def remove(self, key):
        current = self.hashing[key % self.SIZE]
        while current and current.next:
            if current.next.key == key: break
            current = current.next
        else:
            return None
        current.next = current.next.next

hm = HashMap()

hm.put(1, 78)
hm.put(2, 11)
hm.put(3, 30)
hm.put(4, 32)
hm.remove(4)

print(hm.get(3))
