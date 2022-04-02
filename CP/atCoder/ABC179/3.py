from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------
# mxn = 1000002
# spf = [0]*1000002
# def sieve():
#     spf[1]=1
#     for i in range(2,mxn): spf[i]=i
#     for i in range(4,mxn,2): spf[i]=2
#     for i in range(3,int(mxn**.5)+1):
#         if spf[i]==i:
#             for j in range(i*i, mxn, i):
#                 if spf[j]==j: spf[j]=i
# sieve()
# def pFactor(x):
#     res = 0
#     cnt = 0
#     while x>1:
#         tmp,cnt = spf[x],1
#         x//=tmp
#         cnt+=1
#         while x%tmp==0:
#             x,res = x//tmp, res+1
#     return (res,cnt)


n = int(input())

res = 0
cnt = 0
for i in range(1,n):
    res+=(n//i)
    cnt+=n%i==0
print(res-cnt)
