import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("traffic_control_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    res = 0
    n,m,a,b = imap()
    if n+m-1>min(a,b):
        print("Case #{}: {}".format(_+1, "Impossible"))
        continue
    res = [[1]+[1000]*(m-2)+[1] for i in range(n)]
    res[-1] = [1]*m
    a-=m+n-1
    b-=m+n-1
    if a:
        res[0][0]+=a
    if b:
        res[0][-1]+=b
    print("Case #{}: {}".format(_+1, "Possible"))
    for i in res:
        print(*i)

