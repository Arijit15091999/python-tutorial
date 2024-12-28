from Node import Node

class BinaryTree:
    def __init__(self, arr = None):
        self.root = None
        self.tree = list()
        if(arr != None):
            self.__buildTree(arr)

    def __buildTree(self, arr):
        n = len(arr)
        self.root = Node(val = arr[0])
        self.tree.append(self.root)

        for i in range(1, n):
            node = Node(val = arr[i])
            parentIndex = int((i - 1) / 2)
            parent = self.tree[parentIndex]

            if(i % 2 != 0):
                parent.left = node
            else:
                parent.right = node

            self.tree.append(node)

    def __isLeftChild(self, index):
        return index % 2 != 0

    def addNode(self, val):
        node = Node(val = val)

        if(self.root == None):
            self.root = node
            self.tree.append(node)
            return

        nodeIndex = len(self.tree)
        parentIndex = int((nodeIndex - 1) / 2)
        self.tree.append(node)

        parent = self.tree[parentIndex]

        if(self.__isLeftChild(nodeIndex)):
            parent.left = node
        else:
            parent.right = node

    def display(self):
        for node in self.tree:
            print(node)




