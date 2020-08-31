class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                right_child = self.right
                right_child.insert(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                left_child = self.left
                left_child.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            if self.left is None:
                return False
            return self.left.contains(target)