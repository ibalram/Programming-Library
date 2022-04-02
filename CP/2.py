# matrix
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

# import sys
# sys.setrecursionlimit(6*10**5+10)
# from types import GeneratorType
# #use:- put @bootstrap overrecursive function
# def bootstrap(func, stack=[]):
#     def wrapped_function(*args, **kwargs):
#         if stack: return func(*args, **kwargs)
#         else:
#             call = func(*args, **kwargs)
#             while True:
#                 if type(call) is GeneratorType:
#                     stack.append(call)
#                     call = next(call)
#                 else:
#                     stack.pop()
#                     if not stack: break
#                     call = stack[-1].send(call)
#             return call
#     return wrapped_function
# # import sys
# # sys.setrecursionlimit(10**5)

mod = int(1e9+7)
# for _ in range(int(input())):
n,k = map(int,input().split())
col = [0]*(n+1)
row = [0]*(n+1)

empRows = n
empCols = n
res = []
for i in range(k):
    x,y = map(int,input().split())
    x-=1
    y-=1
    if row[x]==0:
        row[x]=1
        empRows-=1
    if col[y]==0:
        col[y] = 1
        empCols-=1
    res.append(empCols*empRows)
print(*res)


# res = 0
# empRows = row.count(row)
# empCols = col.count(col)
# for i in range(n+1):
#     if col[i]==0:
#         res+=empRows
# print(res)
