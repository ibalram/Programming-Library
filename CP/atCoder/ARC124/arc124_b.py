# https://atcoder.jp/contests/arc124/submissions/24537084


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


n = int(input())
a = ilist()
b = ilist()

possibles = set()
for i in range(n):
    possibles.add(a[0]^b[i])

res = []
for x in possibles:
    mp = Counter(b)
    f = 1
    for i in a:
        if i^x in mp:
            mp[i^x]-=1
            if mp[i^x]==0:
                del mp[i^x]
        else:
            f = 0
            break
    if f:
        res.append(x)
print(len(res))
print(*sorted(res), sep="\n")

