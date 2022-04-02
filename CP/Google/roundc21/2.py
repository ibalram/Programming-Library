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

for _ in range(1,int(input())+1):
    res = 0
    gg = 2*int(input())
    for i in range(1,int(gg**.5)+1):
        if gg%i==0:
            div = i
            x = (gg-div*div+div)
            if x>0 and x%(2*div)==0:
                res+=1
            # res+=max(0,gg//div-1)
            if gg//i!=i:
                # res+=max(0,i-1)
                div = gg//i
                x = (gg-div*div+div)
                if x>0 and x%(2*div)==0:
                    res+=1

    print("Case #{}: {}".format(_, res))
