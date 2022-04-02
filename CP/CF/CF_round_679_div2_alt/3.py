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

a = list(map(int,input().split()))
a.sort()
n = int(input())
b = list(map(int,input().split()))
b.sort()

mn = b[0]-a[0]
mx = b[-1]-a[-1]
for i in range(n):
    f = 0
    arr = []
    for j in range(6):
        x = b[i]-a[j]
        arr.append(x)
        # if mn<=x<=mx:
        #     f = 1
        #     break

    arr.sort()
    for k in arr:
        if mn<=k<=mx:
            f = 1
            break
    if f:
        continue
    l = 0
    r = 5
    mindiff = float("inf")
    maxdiff = float("inf")
    while l<6 and arr[l]<=mn:
        mindiff = min(mindiff, mn-arr[l])
        l+=1
    while r>=0 and arr[r]>=mx:
        maxdiff = min(maxdiff, -mx+arr[r])
        r-=1
    if mindiff<maxdiff:
        mn = mn-mindiff
    else:
        mx = mx+maxdiff
    # if f:
print(mx-mn)
