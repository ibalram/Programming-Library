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


# def solve(a,b,k):
#     arr = []
#     b = set(b)
#     n = len(a)
#     for i in range(n):
#         if a[i] in b:
#             arr.append(i)
#     if k>len(arr):
#         return -1
#     res = float("inf")
#     st = Counter()
#     l = 0
#     for i in range(len(arr)):
#         while len(st)>k and l<i:
#             st[a[arr[l]]]-=1
#             if st[a[arr[l]]]==0:
#                 del st[a[arr[l]]]
#             l+=1
#         if len(st)==k:
#             res = min(res, arr[i]-arr[l]+1)
#         st[a[arr[i]]]+=1
#     while (len(st)>k or len(st)==k and st[a[arr[l]]]>1) and l<i:
#         st[a[arr[l]]]-=1
#         if st[a[arr[l]]]==0:
#             del st[a[arr[l]]]
#         l+=1
#     if len(st)==k:
#         res = min(res, arr[i]-arr[l]+1)
#     return res if res<float("inf") else -1


def solve(a,b,k):
    arr = []
    b = set(b)
    n = len(a)
    heap = []
    mp = Counter()
    l,r = 0,0
    res = float("inf")
    while l<n and r<n:
        if a[r] in b:
            mp[a[r]]+=1
        while l<n and (len(mp)>k or len(mp)==k and mp[a[l]]>1):
            if a[l] in b:
                mp[a[l]]-=1
                if mp[a[l]]==0:
                    del mp[a[l]]
            l+=1
        if len(mp)==k:
            res = min(res, r-l+1)
        r+=1
    return res if res<float("inf") else -1


n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(a,b,k))
