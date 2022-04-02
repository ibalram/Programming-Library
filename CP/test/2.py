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
from collections import Counter, defaultdict

for _ in range(int(input())):
    n = int(input())
    char = input().strip().split()
    from collections import defaultdict
    gr = defaultdict(list)
    for i in range(n-1):
        u,v = map(int,input().split())
        gr[u].append(v)
        gr[v].append(u)
    parent = [i for i in range(n+1)]
    leaf = []
    def dfs(s, p):
        cntr = Counter()
        for i in gr[s]:
            if i==p: continue
            parent[i] = s
            cntr+=dfs(i,s)
        res[s] = cntr[char[s-1]]+1
        return cntr+Counter(char[s-1])
    res = [0]*(n+1)
    dfs(1,-1)
    print(*res[1:])

    # graphs = [defaultdict(list) for i in range(26)]
    # for i in leaf:
    #     g = defaultdict(list)
    #     for i in range
