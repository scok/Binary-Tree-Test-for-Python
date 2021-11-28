from bst import BinaryTreeNode, BinaryTree, SplayTree
from avl import AVLTreeNode, AVLTree
from rbt import RedBlackTreeNode, RedBlackTree
from treap import TreapNode, Treap

from random import shuffle
import time

def RunData(data_num,tree,search_num):
    if tree == "BST":
        x = list(range(0,data_num))
        shuffle(x)

        binary_tree = BinaryTree()
        bt1 = time.time()
        for n in x:
            binary_tree.insert(n)
        bt2 = time.time() 
        print('{:.4f}'.format(round(bt2-bt1, 4)),"s             ",end="")

        binary_tree.find(search_num)
        return 0
    elif tree == "AVL":
        x = list(range(0,data_num))
        shuffle(x)
        
        avl_tree = AVLTree()
        at1 = time.time()
        for n in x:
            avl_tree.insert(n)
        at2 = time.time()
        print('{:.4f}'.format(round(at2-at1, 4)),"s             ",end="")
        
        if avl_tree.search(search_num) == False:
            print("ERROR: %d" % search_num)
        return 0
    elif tree == "RBT":
        x = list(range(0,data_num))
        shuffle(x)
        
        rbt = RedBlackTree()
        rt1 = time.time()
        for n in x:
            rbt.insert(n,None)
        rt2 = time.time()
        print('{:.4f}'.format(round(rt2-rt1, 4)),"s             ",end="")
        
        if rbt.find(search_num) == False:
            print("search failed", search_num)
    elif tree == "SPT":
        x = list(range(0,data_num))
        shuffle(x)
        
        spt = SplayTree()
        st1 = time.time()
        for n in x:
            spt.insert(n)
        st2 = time.time()
        print('{:.4f}'.format(round(st2-st1, 4)),"s             ",end="")
        
        if spt.find(search_num) == False:
            print("search failed", search_num)
    elif tree == "Treap":
        x = list(range(0,data_num))
        shuffle(x)
        
        treap = Treap()
        tt1 = time.time()
        for n in x:
            treap.insert(n)
        tt2 = time.time()
        print('{:.4f}'.format(round(tt2-tt1, 4)),"s             ",end="")
        
        if treap.find(search_num) == False:
            print("search failed", search_num)

print("===================================================")
print()
print("                     이진 탐색 트리 비교             ")
print()
print("===================================================")
print("                            BST                    ")
print("===================================================")
print("               삽입 시간     ||    키 값 비교 횟수")
print("===================================================")
print("데이터 갯수")
print("   1000    ||   ",end="")
RunData(1000,"BST",427)
print("   5000    ||   ",end="")
RunData(5000,"BST",2575)
print("  10000    ||   ",end="")
RunData(10000,"BST",5482)
print("  50000    ||   ",end="")
RunData(50000,"BST",25752)
print("===================================================")
print("                            AVL                    ")
print("===================================================")
print("               삽입 시간     ||    키 값 비교 횟수")
print("===================================================")
print("데이터 갯수")
print("   1000    ||   ",end="")
RunData(1000,"AVL",427)
print("   5000    ||   ",end="")
RunData(5000,"AVL",2575)
print("  10000    ||   ",end="")
RunData(10000,"AVL",5482)
print("  50000    ||   ",end="")
RunData(50000,"AVL",25752)
print("===================================================")
print("                            RBT                    ")
print("===================================================")
print("               삽입 시간     ||    키 값 비교 횟수")
print("===================================================")
print("데이터 갯수")
print("   1000    ||   ",end="")
RunData(1000,"RBT",427)
print("   5000    ||   ",end="")
RunData(5000,"RBT",2575)
print("  10000    ||   ",end="")
RunData(10000,"RBT",5482)
print("  50000    ||   ",end="")
RunData(50000,"RBT",25752)
print("===================================================")
print("                            SPT                    ")
print("===================================================")
print("               삽입 시간     ||    키 값 비교 횟수")
print("===================================================")
print("데이터 갯수")
print("   1000    ||   ",end="")
RunData(1000,"SPT",427)
print("   5000    ||   ",end="")
RunData(5000,"SPT",2575)
print("  10000    ||   ",end="")
RunData(10000,"SPT",5482)
print("  50000    ||   ",end="")
RunData(50000,"SPT",25752)
print("===================================================")
print("                           Treaps                  ")
print("===================================================")
print("               삽입 시간     ||    키 값 비교 횟수")
print("===================================================")
print("데이터 갯수")
print("   1000    ||   ",end="")
RunData(1000,"Treap",427)
print("   5000    ||   ",end="")
RunData(5000,"Treap",2575)
print("  10000    ||   ",end="")
RunData(10000,"Treap",5482)
print("  50000    ||   ",end="")
RunData(50000,"Treap",25752)