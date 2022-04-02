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
    n,k = mapi()
    a = []
    b = []
    for i in range(n):
        x,y = mapi()
        a.append([x,y])
    res = 0
    a.sort()
    cnt = 0
    lasted = 0
    for i in range(n):
        diff = max(a[i][1],lasted)-max(a[i][0],lasted)
        curst = max(a[i][0],lasted)
        # print(lasted, curst, diff)
        rem = (diff+k-1)//k
        res+=rem
        lasted = curst+rem*k
    print("Case #{}:".format(_),res)
