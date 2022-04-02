# tribonacci
# zs

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

import sys
sys.setrecursionlimit(6*10**5+10)
from types import GeneratorType
#use:- put @bootstrap overrecursive function
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack: return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack: break
                    call = stack[-1].send(call)
            return call
    return wrapped_function
# import sys
# sys.setrecursionlimit(10**5)

mod = int(1e9+7)
for _ in range(int(input())):
    n,k = map(int,input().split())
    dp = [[-1]*(k+1) for i in range(n+1)]
    @bootstrap
    def rec(i,k):
        if i==n:
            yield 1
        res = 0
        if dp[i][k]!=-1:
            yield dp[i][k]
        if i+1<=n:
            res += yield rec(i+1,k)
            res%=mod
        if i+2<=n:
            res+= yield rec(i+2,k)
            res%=mod
        if i+3<=n and k:
            res+=yield rec(i+3,k-1)
            res%=mod
        dp[i][k] = res
        yield res
    print(rec(0,k))
    # for i in range(n):
    #     print(*dp[i])


"""5
7 3
4 2
3 3
7 1
500000 50



44
7
4
41
934580754"""


# 6
# 7 3
# 4 2
# 3 3
# 7 1
# 2 3
# 500000 50


# 44
# 7
# 4
# 41
# 2
# 934580754
