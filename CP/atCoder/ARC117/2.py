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

from math import log2
print(log2(20192492160000))

n = int(input())
a = ilist()
a.sort(reverse=True)
print(pow(2,max(a)-min(a)+1))
mn = min(a)
mx = max(a)
print(mx-mn)
# print(mn*mx)
# a.append(0)
# n+=1
# res = [0]*(n+1)
# for i in range(1,n):
#     res[i]+=a[i-1]-a[i]+res[i-1]+1

# print(res[n-1])
