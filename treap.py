import random

class TreapNode(object):
    def __init__(self, k, p):
        self.key = k
        self.priority = p
        self.left = None
        self.right = None
    
class Treap(object):
    def __init__(self):
        self.root = None
        self.__priorityList = self.__randomNum()
        
    def __randomNum(self):
        choices = list(range(500000))
        random.shuffle(choices)
        return choices
    
    def __getPriority(self):
        if self.__priorityList[0]:
            return self.__priorityList.pop()
        else:
            raise Exception("Max nodes reached")
    
    def __createNode(self, k):
        priority = self.__getPriority()
        return TreapNode(k, priority)
    
    def insert(self, k):
        if not self.root:
            self.root = self.__createNode(k)
        else:
            self.root = self.__insert(k, self.root)
    
    def __insert(self, k, parent):
        if not parent: return self.__createNode(k)
        
        if k <= parent.key:
            parent.left = self.__insert(k, parent.left)
            if parent.left.priority > parent.priority:
                parent = self.rotateRight(parent)
        else:
            parent.right = self.__insert(k, parent.right)
            if parent.right.priority > parent.priority:
                parent = self.rotateLeft(parent)
        return parent
    
    def rotateRight(self, parent):
        child = parent.left
        parent.left = child.right
        child.right = parent
        return child
    
    def rotateLeft(self, parent):
        child = parent.right
        parent.right = child.left
        child.left = parent
        return child
    
    def __findR(self, key, cur = "start", parent = "start", rel = "left", count=0):
        if cur == "start":
            cur = self.root
            parent = self.root
            
        if not cur:
            return (None, None, None)
        
        if cur.key == key:
            print("  ",count)
            return (parent,cur,rel)
        elif key > cur.key:
            return self.__findR(key, cur.right, cur, "right", count+1)
        else:
            return self.__findR(key, cur.left, cur, "left", count+1)
        
    def find(self, key):
        parent, cur, rel = self.__findR(key)
        
        if parent is not None:
            return True
        else:
            return False
    
    def __isLeaf(self, node):
        if node.right is None and node.left is None:
            return True
        else:
            return False