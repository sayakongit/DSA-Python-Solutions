class TreeNode:
    def __init__(self, name):
        self.data = name
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self, level):
        if self.getLevel() <= level:
            spaces = self.getLevel() * "  " * 2
            prefix = spaces + "|--" if self.parent else ""
            print(prefix, end="")
            print(self.data)
            if self.children:
                for i in self.children:
                    i.printTree(level)

    def getLevel(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent

        return level


if __name__ == '__main__':
    root = TreeNode("Global")
    a1 = TreeNode("India")
    a2 = TreeNode("USA")
    b1 = TreeNode("Gujarat")
    b2 = TreeNode("Karnataka")
    b3 = TreeNode("New Jersey")
    b4 = TreeNode("California")
    c1 = TreeNode("Ahmedabad")
    c2 = TreeNode("Baroda")
    c3 = TreeNode("Bangalore")
    c4 = TreeNode("Mysore")
    c5 = TreeNode("Princeton")
    c6 = TreeNode("Trenton")
    c7 = TreeNode("San Francisco")
    c8 = TreeNode("Mountain View")
    c9 = TreeNode("Palo Alto")

    root.addChild(a1)
    root.addChild(a2)
    a1.addChild(b1)
    a1.addChild(b2)
    a2.addChild(b3)
    a2.addChild(b4)
    b1.addChild(c1)
    b1.addChild(c2)
    b2.addChild(c3)
    b2.addChild(c4)
    b3.addChild(c5)
    b3.addChild(c6)
    b4.addChild(c7)
    b4.addChild(c8)
    b4.addChild(c9)

    root.printTree(2)

