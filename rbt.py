class RedBlackTreeNode():
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 'Red'
          
class RedBlackTree:
    
    def find_grandparent_node(self,node):
        if (node != None and node.parent != None):
            return node.parent.parent
        else:
            return None
    
    def find_uncle_node(self,node):
        grandparent_node = self.find_grandparent_node(node)
        if grandparent_node == None:
            return None
    
        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left
        
    def insert_case1(self,node):
        if node.parent == None:
            node.color = 'Black'
        else:
            self.insert_case2(node)
        
    def insert_case2(self,node):
        if node.parent.color == 'Black':
            return
        else:
            self.insert_case3(node)
    
    def insert_case3(self,node):
        uncle = self.find_uncle_node(node)
    
        if (uncle != None and uncle.color == 'Red'):
            node.parent.color = 'Black'
            uncle.color = 'Black'
            grandparent = self.find_grandparent_node(node)
            grandparent.color = 'Red'
            self.insert_case1(grandparent)
        else:
            self.insert_case4(node)
    
    def insert_case4(self,node):
        
        grandparent = self.find_grandparent_node(node)
    
        if(node == node.parent.right and node.parent == grandparent.left):
            self.rotate_left(node.parent)
            node = node.left
        elif (node == node.parent.left and node.parent == grandparent.right):
            self.rotate_right(node.parent)
            node = node.right
    
        self.insert_case5(node)
    
    def rotate_left(self,node):
        c = node.right
        p = node.parent
    
        if (c.left != None):
            c.left.parent = node
    
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
    
        if (p != None):
            if (p.left == node):
                p.left = c
            else:
                p.right = c

    def rotate_right(self,node):
        c = node.left
        p = node.parent
    
        if (c.right != None):
            c.right.parent = node
    
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
            
        if (p != None):
            if (p.right == node):
                p.right = c
            else:
                p.left = c
     
    def insert_case5(self,node):
        grandparent = self.find_grandparent_node(node)
    
        node.parent.color = 'Black'
        grandparent.color = 'Red'

        if (node == node.parent.left):
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

            
    def __init__(self):
        self.root = None
        self.inserted_node = None

    def insert(self, data, parent_node):
        self.root = self.insert_value(self.root, data, parent_node)
        self.insert_case1(self.inserted_node)
        return 
    
    def insert_value(self, node, data, parent_node):
        if node is None:
            node = RedBlackTreeNode(data)
            node.parent = parent_node
            self.inserted_node = node
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left,data,node)
            else:
                node.right = self.insert_value(node.right,data,node)
        return node
  
    def find(self,search_key):
        count = 0
        
        while self.root:
            if self.root.data == search_key:
                count += 1
                print("  ",count)
                return True
            elif self.root.data > search_key:
                count += 1
                self.root = self.root.left
            elif self.root.data < search_key:
                count += 1
                self.root = self.root.right
        return False   