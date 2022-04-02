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
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = -1
    mp = defaultdict(list)
    for i in range(n):
        mp[a[i]].append(i)
    for i in sorted(mp.keys()):
        if len(mp[i])==1:
            res = mp[i][0]+1
            break
    print(res)
