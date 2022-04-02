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

n = int(input())
a = [0]*n
b = [0]*n
c = []
for i in range(n):
    a[i],b[i] = imap()
    c.append(a[i]/b[i])
pf = c[:]
for i in range(1,n):
    pf[i]+=pf[i-1]
if n==1:
    print(a[0]/2)
    exit()
left = 0
right = pf[-1]
i = 0
while left<right and i<n:
    left+=c[i]
    right-=c[i]
    i+=1
i-=1
if left==right:
    print(1.0*sum(a[:i+1]))
else:
    left-=c[i]
    print(sum(a[:i])+(b[i]*(right-left)+a[i])/2)

