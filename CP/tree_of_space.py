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

# lock(x,uid)
# unlock(x,uid)
# upgradeLock(x,uid)

class WorldMap:
    def __init__(self, inp, m):
        self.users = set()
        self.nodes = set()
        self.graph = defaultdict(set)
        self.parent = {}
        self.m = m
        q = deque()
        idx = 1
        q.append(inp[0])
        self.parent[inp[0]] = inp[0]
        while q and idx<len(inp):
            node = q.popleft()
            for j in range(idx, min(idx+m, len(inp))):
                self.graph[node].add(inp[j])
                self.parent[inp[j]] = node
                q.append(inp[j])
            idx = min(idx+m, len(inp))
        self.locked = defaultdict(bool)
        self.childLocked = defaultdict(bool)
        self.uid = defaultdict(lambda:None)

    def lock(self,x,uid):
        if self.locked[x] or self.childLocked[x]:
            return False
        current = self.parent[x]
        self.locked[x] = True
        self.uid[x] = uid
        while current!=self.parent[current]:
            self.childLocked[current]+=1
            current = self.parent[current]
        return True

    def unlock(self,x,uid):
        if not self.locked[x] or self.uid[x]!=uid:
            return False
        current = x
        while current!=self.parent[current]:
            current = self.parent[current]
            self.childLocked[current]-=1
        self.locked[x] = False
        self.uid[x] = None
        return True

    def upgradeLock(self,x,uid):
        if self.locked[x]:
            return False
        current = x
        # while current!=self.parent[x]:
        #     current = self.parent[current]
        #     if self.locked[current]:
        #         return False
        if self.checkSubTree(x,uid):
            count = self.removeSubTree(x,uid)-1  #-1 because we are locking x
            current = x
            self.locked[x] = True
            self.uid[x] = uid
            while current!=self.parent[current]:
                current = self.parent[current]
                self.childLocked[current]-=count
        return True

    def removeSubTree(self,x,uid):
        count = 0
        for node in self.graph[x]:
            count += self.removeSubTree(node,uid)
        self.childLocked[x]-=count
        count += self.locked[x]
        self.locked[x] = False
        self.uid[x] = None
        return count

    def checkSubTree(self,x,uid):
        flag = True
        for node in self.graph[x]:
            flag &= self.checkSubTree(node,uid)
        if self.locked[x]:
            flag &= (self.uid[x]==uid)
        return flag

    def __repr__(self):
        pass



def do(tree, typ, node, uid):
    if typ==1:
        return tree.lock(node,uid)
    elif typ==2:
        return tree.unlock(node,uid)
    elif typ==3:
        return tree.upgradeLock(node,uid)

if __name__=="__main__":
    n = 7
    m = 2
    nodes = ['World', 'Asia', \
            'Africa', 'China', \
            'India', 'SouthAfrica', 'Egypt']
    # queries = ['1 China 9', '1 India 9', '3 Asia 9', '2 India 9', '2 Asia 9']
    tree = WorldMap(nodes, m)
    queries = [[1,'China',9], [1,'India',9], \
    [3,'Asia',9], [2,'India',9],\
    [2,'Asia',9], [2,'World',9],
    [1,'World',9], [3,'World',9]]
    result = []
    for typ,node,uid in queries:
        result.append(do(tree,typ,node,uid))
    print(*result)

"""
             world
          /         \
     asia             africa
   /     |           /      \
india    china     sa      egypt
"""
# o/p: True True True False True False False True
