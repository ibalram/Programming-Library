import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

a,b,x,y = imap()

@lru_cache(None)
def rec(pos, typ, last):
    # print(pos, typ,last)
    if pos==b and typ==1:
        return 0
    if pos<1 or pos>100:
        return float("inf")
    res = float("inf")
    if typ==0:
        if pos>b:
            res = min(res,x+ rec(pos-1,typ^1, pos),y+rec(pos-1, typ, pos))
            if pos!=last:
                res = min(res, x+rec(pos,typ^1, pos))
        elif pos<b:
            res = min(res,y+rec(pos+1, typ, pos))
            if pos !=last:
                res = min(res, x+rec(pos,typ^1, pos))
        else:
            if pos!=last:
                res= min(res, x+rec(pos,typ^1,pos))
    else:
        if pos>b:
            res = min(res,y+rec(pos-1, typ, pos))
            if pos !=last:
                res = min(res,x+rec(pos,typ^1, pos))
        elif pos<b:
            res = min(res,x+ rec(pos+1,typ^1,pos),y+rec(pos+1, typ, pos))
            if pos!=last:
                res= min(res, x+rec(pos,typ^1,pos))
        else:
            if pos!=last:
                res= min(res, x+rec(pos,typ^1,pos))
    return res
print(rec(a,0, -1))
