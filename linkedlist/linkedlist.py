


class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail


class LinkedList:
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Add value to front of the list (1)"""
        self.head = LinkedNode(value, self.head)


    def remove(self, value):
        # traverse pointer one at a time
        # Keep track of first and last element
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            last = n
            n = n.next

        return False



    def pop(self):
        """remove first value from list"""
        if self.head is None:
            raise Exception("Empty List")
        val = self.head.value
        self.head = self.head.next
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head is None:
            return 'link:[]'
        return 'link:[{0:s}]'.format(','.join(map(str, self)))


a = LinkedList()
a.prepend(1)
a.prepend(2)
a.prepend(3)

# Each new value becomes the head
# will print 3, 2, 1
for _ in a:
    print(_)

print ("Pop value from LinkedList", a.pop())

a.prepend(3)

print("LinkedList is: ", a)


## Turns operations into constant time

class QueueLinkedList:
    def __init__(self, *start):
        """Demo queue using linked list"""
        self.head = None
        self.tail = None
        for _ in start:
            self.add(_)

    def append(self, value):
        """Add value to end of queue"""
        newNode = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def isEmpty(self):
        """determine if queue is empty """
        return self.head == None

    def pop(self):
        """Remove first value from a queue"""
        if self.head is None:
            raise Exception("Queue is empty")
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head is None:
            return 'link:[]'
        return 'Queue:[{0:s}]'.format(','.join(map(str, self)))


q = QueueLinkedList()

q.append(1)
q.append(2)
q.append(3)

print(q)


