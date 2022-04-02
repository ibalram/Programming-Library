# https://atcoder.jp/contests/arc124/submissions/24549261


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

mod = 998244353
n,k = imap()
mark = [0]*(n+1)
st = set()
for i in range(k):
    a,b = input().split()
    b = int(b)
    st.add(b)
    for j in range(1,n+1):
        if a=="L" and j>=b:
            mark[j]+=1
        if a=="R" and j<=b:
            mark[j]+=1
res = 1
for i in range(1,n+1):
    if i not in st:
        res *= mark[i]
        res%=mod
print(res)


