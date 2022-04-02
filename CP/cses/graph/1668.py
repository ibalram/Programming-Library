import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------

import sys
from collections import defaultdict, Counter, deque
input = lambda: sys.stdin.readline().strip()
# sys.setrecursionlimit(10**6)
mod = int(1e9+7)

n,m = map(int,input().split())
g = defaultdict(list)
for i in range(m):
    x,y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)
def dfs(s):
    for i in g[s]:
        if color[i]==0:
            color[i] = 1 if color[s]==2 else 2
            x = dfs(i)
            if x==False:
                return False
        elif color[i]==color[s]:
            return False
    return True
def bfs(s):
    q =deque()
    q.append(s)
    while q:
        s = q.popleft()
        for i in g[s]:
            if color[i]==0:
                color[i] = 1 if color[s]==2 else 2
                q.append(i)
            elif color[i]==color[s]:
                return False
    return True
color = [0]*(n+1)
for i in range(1,n+1):
    if color[i]==0:
        color[i] = 1
        x = bfs(i)
        if not x:
            print("IMPOSSIBLE")
            exit()

print(*color[1:])

