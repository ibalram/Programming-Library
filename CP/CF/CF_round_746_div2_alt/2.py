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

for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(sorted(a))
    if n==1:
        print("YES")
        continue
    res = "YES"
    # if n==x:
    #     print("NO")
    #     continue
    if x<=n-x:
        print("YES")
        continue
    pa = a[x:]
    pb = a[:n-x]
    pc = a[n-x:x]
    pa+=pb
    pa.sort()
    # print(pa,pc)
    c = pa[:n-x]+pc+pa[n-x:]
    print("YES" if c==b else "NO")
    # for i in range(n-x, x):
    #     # print(i,a[i])
    #     if a[i]!=b[i]:
    #         res = "NO"
    #         break
    # print(res)
    # if n==1:
    #     print("YES")
    # elif a==b:
    #     print("YES")
    # elif x==n:
    #     print("NO")
    # elif x==n-1:
    #     print("YES" if b==[a[-1]]+a[1:-1]+[a[0]] else "NO")
    # else:
    #     print("YES")
"""
1 3 2 4 5
"""

