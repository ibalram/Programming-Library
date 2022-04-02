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
    res = float("inf")
    st = set(a)
    mp = {i:[-1] for i in st}
    for i in range(n):
        # if i>0 and a[i]==a[i-1]: continue
        # if mp[a[i]][-1]+1==i: continue
        mp[a[i]].append(i)
    for i in st:
        # if mp[i][-1]+1!=n:
        mp[i].append(n)
    # print(mp)
    for i in mp.keys():
        cnt = 0
        for j in range(1, len(mp[i])):
            if mp[i][j-1]+1!=mp[i][j]: cnt+=1
        res = min(res, cnt)
    print(res)
