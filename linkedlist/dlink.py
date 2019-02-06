'''A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer,
together with next pointer and data which are there in singly linked list.'''

class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # adds to beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)

        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        # 1. check if the given prev_node is NULL
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        #2. allocate node  & 3. put in the data
        new_node = Node(new_data)

        # 4. Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make the next of prev_node as new_node
        prev_node.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_node's next node */
        if new_node.next is not None:
            new_node.next.prev = new_node

    # Adds item to the end
    def append(self, new_data):
        # 1. allocate node 2. put in the data
        new_node = Node(new_data)
        last = self.head

        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        new_node.next = None

        # 4. If the Linked List is empty, then
        #  make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        while (last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node
        # 7. Make last node as previous of new node */
        new_node.prev = last

    # Given the value of an item in the Double linked list, insert a new node before it.
    def insert_before(self, new_data, key):
        # check if the previous node exists
        if key is None:
            print("The given previous node must in Double LinkedList.")
            return

        temp = self.head

        while(temp is not None):
            if temp.data == key:
                if temp == self.head:
                    self.push(new_data)
                    break
                # create a new node and assign the data
                new_node = Node(new_data)
                # Make previous of new Node as previous of prev_node
                new_node.prev = temp.prev
                # new_node.next = temp
                new_node.next = temp
                # assing temp.prev to the new node
                temp.prev = new_node
                # Take the previous node of temp.next and assign it to new node
                new_node.prev.next = new_node
                break
            prev = temp
            temp = temp.next

    # removes the last item in the double linked list
    def pop(self):
        temp = self.head

        if (temp.next == None):
            self.head = temp.next
            temp = None
            return

        while(temp.next is not None):
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    def pop_item(self, key):

        temp = self.head

        if (temp.data == key):
            self.head = temp.next
            temp = None
            return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        # Temp is:  16
        # Temp.prev is:  4
        # next is:  45
        # 4 next points to 45
        # if node is at the end of the list
        if temp.next == None:
            self.pop()
            return
        temp.prev.next = temp.next
        # 45 prev needs to point to 4
        temp.next.prev = temp.prev
        temp = None

    def delete(self, node):
        if self.head is None or node is None:
            return

        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.data
            n = n.next

    def __repr__(self):
        if self.head is None:
            return 'link:[]'
        return 'link:[{0:s}]'.format(','.join(map(str, self)))




# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()
    llist.push(4)
    # print(llist)
    llist.append(45)
    llist.push(32)
    llist.insert_before(16, 45)
    # print(llist)
    llist.insert_before(66, 32)
    # print(llist)ß
    llist.pop_item(16)
    print(llist)
    llist.pop_item(45)
    print(llist)
    llist.pop_item(66)
    print(llist)
    llist.delete(llist.head.next)
    print(llist)
    llist.delete(llist.head)
    print(llist)









