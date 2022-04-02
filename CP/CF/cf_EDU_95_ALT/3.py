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
sys.setrecursionlimit(10**6+10)
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
for _ in  range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    dp = [[-1]*2 for i in range(n+1)]
    @bootstrap
    def rec(i,turn):
        if i>=n:yield 0
        res = float("inf")
        if dp[i][turn]!=-1:
            yield dp[i][turn]
        if turn:
            if i<n:
                res = min(res,a[i]+ (yield rec(i+1,turn^1)))
            if i+1<n:
                res = min(res,a[i]+a[i+1]+ (yield rec(i+2,turn^1)))
        else:
            if i<n:
                res = min(res,(yield rec(i+1,turn^1)))
            if i+1<n:
                res = min(res,(yield rec(i+2,turn^1)))
        dp[i][turn] = res
        yield res
    print(rec(0,1))
