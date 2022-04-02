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


from random import *
for _ in range(int(input())):
    n,k = map(int, input().split())
    st = set(range(n))
    f = 0
    for i in range((n+1)//2):
        idx = 0
        while True:
            idx = randint(0,n-1)
            if idx in st:
                break
        st.remove(idx)
        print(idx, flush=True)
        r = int(input())
        if r==0:
            f = 1
            break
        else:
            print(idx, flush=True)
            r = int(input())
    if f==0:
        break


