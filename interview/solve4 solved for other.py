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



import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict, Counter
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = input().split()
    graph = defaultdict(list)
    for i in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    def dfs(s, par):
        mp = Counter([a[s-1]])
        for i in graph[s]:
            if i==par: continue
            mp+=dfs(i,s)
        res[s-1] = mp[a[s-1]]
        return mp
    res = [0]*n
    dfs(1,-1)
    print(*res)


