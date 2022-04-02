# https://atcoder.jp/contests/abc213/tasks/abc213_d
# https://atcoder.jp/contests/abc213/submissions/24871360

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
g = defaultdict(list)
for i in range(n-1):
    u,v = imap()
    g[u].append(v)
    g[v].append(u)

for i in g:
    g[i].sort()

def dfs(s,par):
    st.append(s)
    f = 0
    for i in g[s]:
        if i==par: continue
        f = 1
        dfs(i,s)
        st.append(s)

st = []
dfs(1,-1)
print(*st)

