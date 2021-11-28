class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return ("node[%s]" % self.val)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val, parent=None):
        if (parent == None):
            parent = self.root
        if (parent == None):
            self.root = BinaryTreeNode(val)
            return
        elif (val < parent.val):
            if (parent.left == None):
                parent.left = BinaryTreeNode(val)
                return
            else:
                self.insert(val, parent.left)
        else:
            if (parent.right == None):
                parent.right = BinaryTreeNode(val)
                return
            else:
                self.insert(val, parent.right)

    def find(self, val, node=None, count=0):
        if (node == None):
            node = self.root
        if (node == None):
            return None
        elif (val == node.val):
            print("  ",count+1)
            return True
        elif (val < node.val):
            if (node.left != None):
                leftrv = self.find(val, node.left, count+1)
                if leftrv != None:
                    return leftrv
        elif (val > node.val):
            if (node.right != None):
                rightrv = self.find(val, node.right, count+1)
                if rightrv != None:
                    return rightrv
        return False

class SplayTree(BinaryTree):
    def find(self, val, node=None, p=None, g=None, gg=None, count=0):
        if (node == None):
            node = self.root
        if (node == None):
            return None
        elif (val == node.val):
            if (p != None):
                if (g == None):
                    self.rotateup(node, p, g)
                elif ((g.left == p and p.left == node) or
                      (g.right == p and p.right == node)):
                    self.rotateup(p, g, gg)
                    self.rotateup(node, p, gg)
                else:
                    self.rotateup(node, p, g)
                    self.rotateup(node, g, gg)
            print("  ",count)
            return node
        elif (val < node.val):
            if (node.left != None):
                leftrv = self.find(val, node.left, node, p, g, count+1)
                if leftrv != None:
                    return leftrv
        elif (val > node.val):
            if (node.right != None):
                rightrv = self.find(val, node.right, node, p, g, count+1)
                if rightrv != None:
                    return rightrv
        return None

    def rotateup(self, node, parent, gp=None):
        if node == parent.left: 
            parent.left = node.right
            node.right = parent
            if (self.root == parent):
                self.root = node
        elif node == parent.right:
            parent.right = node.left
            node.left = parent
            if (self.root == parent):
                self.root = node
        else:
            print("This is impossible")

        if (gp != None):
            if (gp.right == parent):
                gp.right = node
            elif (gp.left == parent):
                gp.left = node