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
    n = int(input())
    b = list(map(int,input().split()))
    a = b[::-1]
    nxt = [n]*(n+1)
    st = []
    for i,v in enumerate(a):
        while st and a[st[-1]]<v:
            nxt[st.pop()] = i
        st.append(i)
    while st: st.pop()
    i = 0
    res = 0
    while nxt[i]!=n:
        i = nxt[i]
        res+=1
    if b.index(max(b))!=0:
        print(-1)
    else:
        print(res+(i!=n-1))

