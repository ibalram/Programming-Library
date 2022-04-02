import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)


for _ in range(int(input())):
    n = int(input())
    gr = defaultdict(list)
    for i in range(n-1):
        u,v = imap()
        gr[u].append(v)
        gr[v].append(u)
    def bfs(s):
        q = deque()
        q.append(s)
        vis ={s:0}
        while q:
            s = q.popleft()
            for i in gr[s]:
                if i in vis: continue
                vis[i] = vis[s]+1
                q.append(i)
        farth = -1
        mx = -1
        for i,val in vis.items():
            if val>mx:
                farth = i
                mx = val
        return farth, mx
    farth,mx = bfs(1)
    end,dia = bfs(farth)
    print((dia+1)//2)

