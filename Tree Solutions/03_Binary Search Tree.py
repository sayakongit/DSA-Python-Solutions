class BstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, child):
        if self.data == child:
            return

        if child < self.data:
            if self.left:
                self.left.addChild(child)
            else:
                self.left = BstNode(child)
        else:
            if self.right:
                self.right.addChild(child)
            else:
                self.right = BstNode(child)

    def in_order_traversal(self):
        elements = []

        # Left Subtree
        if self.left:
            elements += self.left.in_order_traversal()
        # Root
        elements.append(self.data)
        # Right Subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # Root
        elements = [self.data]
        # Left Subtree
        if self.left:
            elements += self.left.pre_order_traversal()
        # Right Subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # Left Subtree
        if self.left:
            elements += self.left.post_order_traversal()
        # Right Subtree
        if self.right:
            elements += self.right.post_order_traversal()
        # Root
        elements.append(self.data)

        return elements

    def calculateSum(self):
        return sum(self.in_order_traversal())

    def findMin(self):
        elem = self.data
        while self.left:
            elem = self.left.data
            self.left = self.left.left

        return elem

    def findMax(self):
        elem = self.data
        while self.right:
            elem = self.right.data
            self.right = self.right.right

        return elem


def buildTree(arr):
    r = BstNode(arr[0])

    for i in arr[1:]:
        r.addChild(i)

    return r


if __name__ == '__main__':
    nodes = [8, 4, 6, 7, 2, 4, 3, 10]
    root = buildTree(nodes)

    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    print(root.calculateSum())
    print(root.findMin())
    print(root.findMax())
