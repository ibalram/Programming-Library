import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------

for _ in range(1,int(input())+1):
    n,x = mapi()
    a = list(mapi())
    b = []
    for i in range(n):
        b.append([(a[i]+x-1)//x, i])
    b.sort()
    res = []
    for i,idx in b:
        res.append(idx+1)
    print("Case #{}:".format(_),*res)
