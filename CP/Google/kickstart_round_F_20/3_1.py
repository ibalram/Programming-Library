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
    it = 0
    res = 0
    st = set([(i,j) for i,j in a]+[(ra,pa),(rb,pb)])
    x,y = ra,pa
    sm = 0
    prev = 0
    while True:
        f = 1
        cur = 0
        if it%2==0:
            x,y = ra,pa
        else:
            x,y = rb,pb
        for i,j in nxt(x,y):
            if (i,j) not in st:# and (i!=xx or j!=yy):
                res += (1 if it%2==0 else -1)
                if it%2==0:
                    ra,pa = i,j
                else:
                    rb,pb = i,j
                f = 0
                # print(i,j,x,y)
                st.add((i,j))
                break
        if len(st)==s*s:
            break
        if f:
            cur = 1
        if cur and prev:
            break
        prev = cur
        it+=1
    # print(nxt(2,2))
    # res = rec(ra,pa,rb,pb,marked)
    print("Case #{}:".format(_),res)
