import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)

mod = int(1e9+7)

for _test in range(int(input())):
    res = 0
    ans = 0
    n,c = imap()
    intervels = []
    a = []
    # start =
    # mp = [0]*(10**5)
    mp = defaultdict(int)
    for i in range(n):
        intervels.append(ilist())
        x,y = intervels[i]
        a.append((x,-1))
        a.append((y,1))
        mp[x+1]+=1
        mp[y]-=1

    preSum = 0
    prev = 1
    mp1 = defaultdict(list)
    for key, val in mp.items():
        if key ==1:
            preSum+=val
            prev = 1
        else:
            mp1[preSum].append((prev, key-1))
            preSum+=val
            prev = key

    res = n
    for key in sorted(mp1.keys(), reverse=True):
        val = mp1[key]
        for i,j in val:
            if c>0:
                mn = min(c, j-i+1)
                ans+=mn*key
                c-=mn

    print('Case #{}:'.format(_test+1), ans)
