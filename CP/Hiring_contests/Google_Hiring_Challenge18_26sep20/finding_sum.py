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


for _ in range(int(input())):
    a = int(input())
    xx = 0
    yy = 0
    x = a
    y = a+1
    res = 0
    while x-yy>1:
        res+=sum(range(yy+1,x))
        xx,yy = x,y
        x+=a
        y+=a+1
    print(res)

