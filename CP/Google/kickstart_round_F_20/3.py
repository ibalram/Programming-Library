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
    s, ra, pa, rb, pb, c = mapi()
    a = []
    res = 0
    for i in range(c):
        x,y = mapi()
        a.append([x,y])
    def nxt(x,y):
        res = []
        if y-1>=1:
            res.append([x,y-1])
        if y+1<=2*x-1:
            res.append([x,y+1])
        if y%2 and x+1<=s:
            res.append([x+1,y+1])
        if y%2==0 and x-1>=1:
            res.append([x-1,y-1])
            # print(x,y)
        return res
    # marked = 0
    # for i,j in a:
    #     marked|=1<<(i+i*j)
    # marked|=1<<(ra+ra*pa)
    # marked|=1<<(rb+rb*pb)
    marked = set([(i,j) for i,j in a]+[(ra,pa),(rb,pb)])
    # @lru_cache(None)
    def rec(x,y,xx,yy,marked,flg,cnt):
        res = -float("inf")
        if cnt==2:
            return 0
        # print(x,y,xx,yy,marked)
        f = 0
        for i,j in nxt(x,y):
            # if (marked>>(i+i*j))&1==0:# and (i!=xx or j!=yy):
            if (i,j) not in marked:
                marked.add((i,j))
                # res = max(res, (1 if flg==0 else -1) + rec(xx,yy,i,j, marked|(1<<(i+i*j)), flg^1,0))
                res = max(res, 1 - rec(xx,yy,i,j, marked, flg^1,0))
                marked.remove((i,j))
                f = 1
        if f==0:
            res = max(res, -rec(xx,yy,x,y, marked,flg^1, cnt+1))
            # return 0
        return res
    res = rec(ra,pa,rb,pb,marked,0,0)
    print("Case #{}:".format(_),res)
