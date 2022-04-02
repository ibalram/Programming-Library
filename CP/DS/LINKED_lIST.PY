import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtFront(self, node):
        if self.head==None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node
    def insertAtFront(self, node):
        if self.head==None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node
    def __str__(self):
        root = self.head
        res = []
        while root:
            res.append(str(root.val))
            root = root.next
        res.append("null")
        return "->".join(res)


ll = LinkedList()
ls = [4,7,5,2,1]
for i in ls:
    node = Node(i)
    ll.insertAtFront(node)
print("before adding at front:  ", ll)
node = Node(8)
ll.insertAtFront(node)
print("after adding at front:  ", ll)

