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
from collections import defaultdict, Counter, deque
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n,m = map(int,input().split())
    mp = defaultdict(dict)
    mat = []
    ln = defaultdict(int)
    for i in range(n):
        a = list(map(int,input().split()))[::-1]
        mat.append(a)
        for j in range(m):
            # print(mp)
            mp[i+j][a[j]]=mp[i+j].get(a[j],0)+1

            ln[i+j]+=1
    q = int(input())
    for _q in range(q):
        x,y,z = map(int,input().split())
        x-=1
        y = m-y
        k = x+y
        mp[k][mat[x][y]]-=1
        mat[x][y] = z
        mp[k][z]=mp[k].get(z,0)+1
        print("Yes" if mp[k][z]==ln[k] else "No")

