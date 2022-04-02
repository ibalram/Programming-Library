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

s = input().strip()
a = []
for i in s:
    if i in ["a", "b"]:a.append(i)
n = len(a)
tota = []
cnt = 0
for i in range(n):
    if a[i]=="a":
        cnt+=1
    else:
        if cnt: tota.append(cnt)
        cnt = 0
if cnt:
    tota.append(cnt)
res = 1
for i in tota:
    res+=res*i%mod
    res%=mod
print(res-1)
