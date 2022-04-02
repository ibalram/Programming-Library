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

def nextGreater(h,n):
    st =[]
    nxt = [-1]*(n+1)
    for i in range(n):
        while st and h[st[-1]]>h[i]:
            nxt[st.pop()] = i
        st.append(i)
    while st: nxt[st.pop()] = -1
    prv = [-1]*(n+1)
    for i in range(n-1,-1,-1):
        while st and h[st[-1]]>h[i]:
            prv[st.pop()] = i
        st.append(i)
    return nxt,prv

n,m = imap()
a = ilist()

nxt,prv = nextGreater(a,n)
for i in range(n):
    left = nxt[i]
    right = prv[i]
    if right==-1:
        right = n
    if right-left
