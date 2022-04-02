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

s = input().strip()
a = list(map(int,s.split()))
mod = int(1e9+7)
n = len(a)

# def sumOfSubstrings(num):
#     n = len(num)
#     sumofdigit = []
#     sumofdigit.append(int(num[0]))
#     res = sumofdigit[0]
#     for i in range(1, n):
#         numi = int(num[i])
#         sumofdigit.append((i + 1) * numi + 10 * sumofdigit[-1])
#         res += sumofdigit[i]
#     return res
# def rec(i):
#     if i>=n:return 0
#     res = 0
#     for j in range(i)

def calc(n):
    # res = 1*(pow(10,n,mod)-1)//(9)
    res = (n*pow(10,n,mod)%mod - (pow(10,n,mod)-1)%mod*pow(9,mod-2,mod)%mod)*pow(9,mod-2,mod)%mod
    return res
num = 0
n = len(s)
# for i in s:
#     num = (num*10%mod+int(i))%mod
# print(num,sumOfSubstrings(s))
res = 0
for i in range(n):
    if i<n-1:
        x = n-i-1
        res+=int(s[i])*calc(n-i-1)%mod
        # print(s[i],n-i-1,calc(n-i-1))
    if i>0:
        x = n-i
        res+=int(s[i])*calc(n-i)%mod*(i*(i+1)//2)%mod
        # print(s[i],n-i,calc(n-i))
print(res)

