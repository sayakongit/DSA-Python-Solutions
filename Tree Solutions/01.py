class TreeNode:
    def __init__(self, name, desg):
        self.data = [name, desg]
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self, param):
        spaces = self.getLevel() * "  " * 2
        prefix = spaces + "|--" if self.parent else ""
        print(prefix, end="")
        if param == "both":
            print(self.data[0], " (", self.data[1], ")", sep="")
        elif param == "name":
            print(self.data[0])
        elif param == "desg":
            print(self.data[1])

        if self.children:
            for i in self.children:
                i.printTree(param)

    def getLevel(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent

        return level


if __name__ == '__main__':
    ceo = TreeNode("Nilupul", "CEO")
    cto = TreeNode("Chinmay", "CTO")
    ihead = TreeNode("Vishwa", "Infrastructure Head")
    hrhead = TreeNode("Gels", "HR Head")
    ahead = TreeNode("Aamir", "Application Head")
    cm = TreeNode("Dhaval", "Cloud Manager")
    am = TreeNode("Abhijit", "App Manager")
    rm = TreeNode("Peter", "Recruitment Manager")
    pm = TreeNode("Waqas", "Policy Manager")

    ceo.addChild(cto)
    ceo.addChild(hrhead)
    cto.addChild(ihead)
    cto.addChild(ahead)
    ihead.addChild(cm)
    ihead.addChild(am)
    hrhead.addChild(rm)
    hrhead.addChild(pm)

    ceo.printTree("both")
    ceo.printTree("name")
    ceo.printTree("desg")
