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
mod = int(1e9+7)

n = int(input())
c = ilist()
gr = defaultdict(list)
for i in range(n-1):
    a,b = imap()
    gr[a].append(b)
    gr[b].append(a)


def dfs(s,par):
    for i in gr[s]:
        if i==par: continue
        if col[c[i-1]]==0:
            res.append(i)
        col[c[i-1]]+=1
        dfs(i,s)
        col[c[i-1]]-=1
col = [0]*(max(c)+1)
res = [1]
col[c[0]]+=1
dfs(1,-1)
print(*sorted(res), sep="\n")

