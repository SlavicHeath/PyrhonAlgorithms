########################################################
########################################################
#
# Name: Slavic Heath
#
# Create a DoublyLinked List from Linked list
# Implement operations is_empty, add_to_head, pop_head, add_to_tail, pop_tail, etc.
#
########################################################
########################################################

class DLL:
    # Initalize DLL Doubly Linked List
    def __init__(self):
        '''
        Initialise Head of list tail of list and size of the list
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        '''
        Check If the list is empty True if empty else false
        :return: Boolean of weather list is empty or not
        '''
        if self.size == 0:
            return True
        else:
            return False

    def __str__(self):
        '''
        Print a string representaion of each node created in a given format [1; 2; 3;]
        :return: String representation of Linked List
        '''
        result = "["
        n = self.head
        # Loop through all nodes adding string representation
        while n is not None:
            result = result + str(n.data) + "; "
            n = n.next
        # Ignore space and all string for formating
        result = result[:-2] + "]"

        return result

    def add_to_head(self, item):
        '''
        Add to the head of the list
        :param item: Item to be added
        :return: None
        '''
        # Node to be added
        newNode = Node(item)

        # point the new node to the head
        newNode.next = self.head
        self.head = newNode

        # Check if there are no nodes and point new node to head and tail
        if self.size == 0:
            self.tail = newNode
            self.head = newNode
        # Increase list size
        self.size += 1

    def pop_head(self):
        '''
        Remove from the head of the list
        :return: Node to be removed
        '''
        # If list is empty return
        if self.is_empty():
            print("List is empty!")
            return
        # Point the next node to head
        next_node = self.head.next
        # Check if there is next node and point previous to
        if next_node != None:
            next_node.previous = None
        # point node to head return item that was popped
        item = self.head.data
        self.head = next_node
        return item

    def add_to_tail(self, item):
        '''
        Add to the tail side of the list
        :param item: item to be added
        :return: None
        '''
        # Create new node to be added
        newNode = Node(item)
        # Check if size is empty and point tail and head to new node
        if self.is_empty() is True:
            self.tail = newNode
            self.head = newNode
        else:
            # Point tail to new node and previous to previous node increase size
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.size += 1

    def pop_tail(self):
        '''
        Remove from tail side
        :return: poped item
        '''
        # Check if list is empty
        if self.is_empty():
            print('List is empty')
            return
        # Point prev value to tail previous
        item = self.tail.data
        prev = self.tail.previous

        # Check if previous is None and point to next and previous to the previous item
        if prev != None:
            prev.next = None

        self.tail.prev = None
        self.tail = prev
        # return item
        return item

    def contains(self, item):
        '''
        Check if an item is inside of a list
        :param item: Item to be found
        :return: Boolean if item is found
        '''
        # Initialise boolean to not found
        Found = False

        self.current = self.head
        # iterare through nodes
        while self.current.data != item and self.current.next is not None:
            self.current = self.current.next
        # Check if item is found and change boolean to true else return False
        if self.current.data == item:
            Found = True
        return Found

    def insert(self, index, item):
        '''
        Insert item at an index in a List
        :param index: Place item to be placed
        :param item: item to be placed
        :return: None
        '''
        # Initialize new node
        newNode = Node(item)
        # if value is the first value point new value to head and prev of prev value to new Node
        if index == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        else:
            # Using temporary node iterate through list until node is found at index
            node = self.head
            for i in range(1, index):
                if node is not None:
                    node = node.next
            # Change found node with point to next node and previous node
            if node is not None:
                newNode.next = node.next
                newNode.previous = node
                node.next = newNode
                if newNode.next is not None:
                    newNode.next.previous = newNode

    def remove(self, index):
        '''
        Remove node at a given index
        :param index: at which point to remove item
        :return: item removed
        '''

        node = self.head
        # iterate through nodes till node is found decreasing index
        while index > 1:
            node = node.next
            index -= 1
        # With found node Reccord node wit item and point next node to te next and previous node to next
        prev = node
        item = node.next
        node.next = node.next.next
        node.previous = prev
        return item.data

    def length(self):
        '''
        Give a value of the length of the list
        :return length of the List
        '''
        #initialize counter = result
        result = 0
        temp = self.head
        #Iterate through list increasing counter
        while temp is not None:
            result += 1
            temp = temp.next
        # return length
        return result

    def last_index(self, item):
        '''
        Traverse through a list and give the last index item is in
        :param item: item ot be searched
        :return: index of the item
        '''
        # Check if list is empty
        if self.head is not None:
            # Initalize to transverse through list
            last = self.tail
            index = 0
            while last is not None:
                index += 1
                if last.data == item:
                    break
                else:
                    last = last.previous
            return self.length() - index


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)
