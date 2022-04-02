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
mod = 998244353

n,m = imap()
st = set()
for i in range(m):
    st.add(tuple(i for i in ilist()))

# Wrong
def rec(i,j):
    if (j-i+1)%2:
        return 0
    if i>j:
        return 1
    if i+1==j:
        return 1*((i,j) in st)
    res = 0
    for x in range(i,j):
        if (x,x+1) in st:
            res = (res+rec(i,x-1)*rec(x+2,j)%mod)%mod
    sta = []
    for x in range(i,j+1):
        if sta and (sta[-1],x) in st:
            y = sta.pop()
            res = (res+rec(i,y-1)*rec(x+1,j)%mod)%mod
        else:
            sta.append(x)
    return res
print(rec(1,2*n))
