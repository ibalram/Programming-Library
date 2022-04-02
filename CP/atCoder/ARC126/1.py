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
    # def rec()
    # ap = a//2
    # ar = a-ap
    # bp = b//2
    def ttttt(t,T,f):
        x = t//5
        return x, t-5*x, T,f
    def tff(t,T,f):
        x = min(t,f//2)
        return x, t-x, T, f-2*x
    def tttf(t,T,f):
        x = min(t//3,f)
        return x, t-3*x, T, f-x
    def ttTT(t,T,f):
        x = min(t//2, T//2)
        return x, t-2*x, T-2*x, f
    def TTf(t,T,f):
        x = min(T//2, f)
        return x, t, T-2*x, f-x
    ls = [ttttt, tff, tttf, ttTT, TTf]
    a,b,c = imap()
    res = 0
    for i in range(5):
        for j in range(5):
            if j==i: continue
            for k in range(5):
                if k in [i,j]:continue
                for l in range(5):
                    if l in [i,j,k]:continue
                    for m in range(5):
                        if m in [i,j,k,l]: continue
                        X,Y,Z = a,b,c
                        cnt = 0
                        y,A,B,C = ls[i](a,b,c)
                        cnt+=y
                        y,A,B,C = ls[j](A,B,C)
                        cnt+=y
                        y,A,B,C = ls[k](A,B,C)
                        cnt+=y
                        y,A,B,C = ls[l](A,B,C)
                        cnt+=y
                        y,A,B,C = ls[m](A,B,C)
                        cnt+=y
                        a,b,c = X,Y,Z
                        # if cnt>900000000000000:
                        #     print(cnt, i,j,k,l,m, (A,B,C))
                        res = max(res,cnt)
    print(res)
