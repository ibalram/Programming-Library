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
import sys
import math
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):

    n,m = map(int,input().split())
    mp = defaultdict(int)
    a = defaultdict(list)
    b = defaultdict(list)
    for i in range(m):
        x = list(map(int,input().split()))
        for j in x[1:]:
            # mp[j]+=1
            a[i].append(j)
            b[j].append(i)
    c = [(len(j),i) for i,j in a.items()]
    c.sort()
    f = 0
    res = [0]*m
    mx = math.ceil(m/2)
    for i,j in c:
        if i==1:
            res[j] = a[j][0]
            mp[a[j][0]]+=1
            if mp[a[j][0]]>mx:
                f = 1
                break
        else:
            mn = float("inf")
            mnidx = -1
            for k in range(i):
                if mp[a[j][k]]<mn:
                    mn = mp[a[j][k]]
                    mnidx = a[j][k]
            res[j] = mnidx
            mp[mnidx]+=1
            if mp[mnidx]>mx:
                f = 1
                break
    if f:
        print("NO")
    else:
        print("YES")
        print(*res)

    # mx = math.ceil(m/2)
    # lsb = sorted(b.items(), key=lambda x: len(x[1]))
    # res = [0]*m
    # for i,lis in lsb:
    #     # lis.sort(key=lambda x:-mp[x])
    #     cntr = 0
    #     for j in lis:
    #         if cntr<mx and res[j]==0:
    #             res[j] = i
    #             cntr+=1
    #         if cntr>=mx:break

    #     # for j in lis:
    #     #     if track[j]+1<=mx:
    #     #         track[j]+=1
    #     #         res[i] = j
    # ls = sorted(a.items(), key=lambda x: len(x[1]))
    # track = [0]*(n+1)
    # idx = 0
    # res = [0]*m
    # mx = math.ceil(m/2)
    # for i,lis in ls:
    #     lis.sort(key=lambda x:-mp[x])
    #     for j in lis:
    #         if track[j]+1<=mx:
    #             track[j]+=1
    #             res[i] = j
    # if res.count(0):
    #     print("NO")
    # else:
    #     print("YES")
    #     print(*res)




