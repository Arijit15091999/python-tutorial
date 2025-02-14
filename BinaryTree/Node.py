class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


    def __str__(self):
        return f"""
        ({self.val}),
        ---> (left -> {self.left.val if self.left != None else "Null"}) ,
        ---> (right -> {self.right.val if self.right != None else "Null"})
        """