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

n,k = imap()
s = input().strip()
t = input().strip()
f = 0
for i in range(n):
    if s[i]!=t[i]:
        f = 1
        s = s[i:]
        t = t[i:]
        break
if not f:
    print(n)
    exit()
res = n-len(s)
n = len(s)
for i in range(n):
    cur = 1
    for j in range(i+1):
        if t[j]=="b":
            cur+=1<<(i-j)
        if s[j]=="b":
            cur-=1<<(i-j)
    if cur<k:
        res+=cur
    else:
        res+=(n-i)*k
        break
print(res)


