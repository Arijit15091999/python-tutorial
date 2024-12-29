from NodeClass import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def addFirst(self, val):
        node = Node(val)

        if(self.__size == 0):
            self.root = node
            self.tail = node
            self.__size += 1
            return

        self.__size += 1

        node.next = self.root
        self.root = node

    def addLast(self, val):
        node = Node(val)

        if(self.__size == 0):
            self.root = node
            self.tail = node
            self.__size += 1
            return
        self.tail.next = node
        self.__size += 1
        self.tail = self.tail.next

    def addAtIndex(self, val, index):
        if(index < 0 or index >= self.__size):
            raise IndexError("index out of bounds")

        i = 0
        node = self.root
        while(i < index - 1):
            node = node.next

        node.next = Node(val, node.next)

    def deleteFirstNode(self):
        if(self.__size == 0):
            print("list empty")
            return

        node = self.root

        self.root = self.root.next
        self.__size -= 1

        if(self.__size == 0):
            self.root = None
            self.tail = None

        del node

    def deleteLastNode(self):
        prev = None
        current = self.root

        while(current.next != None):
            prev = current
            current = current.next

        prev.next = None
        self.tail = prev
        self.__size -= 1

        if(self.__size == 0):
            self.root = None
            self.tail = None

        del current

    def deleteNodeAtIndex(self, index):
        if(index < 0 or index >= self.__size):
            raise IndexError("index out of bounds")

        i = 0
        node = self.root
        while(i < index - 1):
            node = node.next

        node.next = node.next.next


    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def printLinkedList(self):
        if self.isEmpty():
            print("empty")
            return

        node = self.head

        while(node != None):
            print(node.val, sep = " -> ")
            node = node.next
        print()


l = LinkedList()

for i in range(10):
    l.addLast(i)

l.printLinkedList()