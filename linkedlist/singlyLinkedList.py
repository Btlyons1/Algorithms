# A simple Python program to introduce a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function adds an item to the head of a Linked List
    # Time complexity is constant time O(1)
    def push(self, new_data):
        # Create the item and assign the data
        new_node = Node(new_data)
        # point to the previous head
        new_node.next = self.head
        # move the head to point to the new node
        self.head = new_node

    # Inserts a new node after the given prev_node
    # Time complexity of insert_after() is O(1) as it does constant amount of work.
    # This function is in LinkedList class. Inserts a
    # new node after the given prev_node. This method is
    # defined inside LinkedList class shown above */
    def insert_after(self, prev_node, new_data):
        print("Previous node is: ", prev_node)
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        #  2. create new node &
        #      Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    # This function inserts a new node anywhere in the linkedlist
    # O(n) time complexity as it needs to traverse through the linked list to find the
    # key of the node
    def insert(self, key, new_data):
        # check if the previous node exists
        if key is None:
            print("The given previous node must inLinkedList.")
            return

        temp = self.head

        while(temp is not None):
            if temp.data == key:
                # create a new node and assign the data
                new_node = Node(new_data)
                # Make next of new Node as next of prev_node
                new_node.next = temp.next
                #  make next of prev_node as new_node
                temp.next = new_node
                break
            prev = temp
            temp = temp.next

    def append(self, new_data):
        # Create the new node
        # Assign new data
        # Next is set as none
        new_node = Node(new_data)

        #If the linked list is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # If not empty, traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # Change the next of last node
        last.next = new_node

    # Given a reference to the head of a list and a key
    # Delete the first occurence of key in linked list
    def delete(self, key):
        # store head node
        temp = self.head

        # if head node itself holds the key to be deleted
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None


    # This function prints contents of linked list
    # starting from head
    def print_list(self):
        temp = self.head
        while (temp):
            print ("Current node is: ", temp.data)
            temp = temp.next
            print("Node.next is: ", temp)


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

    # Start with the empty list
    llist = LinkedList()

    llist.head  = Node(1)
    second = Node(2)
    third  = Node(3)

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as first, 
    second and third 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''

    llist.head.next = second; # Link first node with second

    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    second.next = third; # Link second node with the third node

    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+ 
    '''

    print(llist)
    # Adds a node to the end of the list
    llist.append(5)
    print(llist)

    # Insert a new node at the beginning
    llist.push(15)
    print(llist)

    llist.insert_after(llist.head.next, 4)
    print(llist)

    llist.insert(3, 10)
    print(llist)

    llist.delete(2)

    print(llist)