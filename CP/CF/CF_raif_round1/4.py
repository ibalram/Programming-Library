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


from heapq import heapify, heappop, heappush

n = int(input())
a = list(map(int,input().split()))
col = [0]*(n+1)
row = [0]*(n+1)
res = []

ro = n

from collections import defaultdict
col2Row = defaultdict(int)
row2Col = defaultdict(int)
mat = [[0]*(n+1) for i in range(n+1)]
for i in range(n,0,-1):
    if a[i-1]==1:
        mat[ro][i] = 1
        res.append([ro,i])
        col[i]+=1
        row[ro]+=1
        col2Row[i] = ro
        row2Col[ro] = i
        ro-=1
ones = []
for i in range(n+1):
    if row[i]:ones.append(i)

f = 0
if a[-1]>1:
    f = 1
for i in range(n,0,-1):
    if a[i-1]==2:
        if ones and row2Col[ones[-1]]>i:
            ro = ones.pop()
            mat[ro][i]=1
            res.append([ro,i])
            col[i]+=1
            row[ro]+=1
            col2Row[i] = ro
        else:
            f = 1
            break
empRows = []
oneCols = []
for i in range(1,n+1):
    if row[i]==0:
        empRows.append(i)
    if col[i] == 1 and row[col2Row[i]]>=1:
        # oneCols.append(i)
        heappush(oneCols,-i)

for i in range(n,0,-1):
    if a[i-1]==3:
        if empRows and oneCols:# and oneCols[-1]>i:
            col2 = -heappop(oneCols)
            if col2>i:
                col1 = i
                ro = empRows.pop()
                mat[ro][col1]=1
                mat[ro][col2] = 1
                col[col1]+=1
                col[col2]+=1
                row[ro]+=1
                res.append([ro,col1])
                res.append([ro,col2])
                heappush(oneCols, -i)
            else:
                f = 1
        else:
            f = 1
            break
if f:
    print(-1)
else:
    print(len(res))
    for i in res:
        print(*i)
for i in mat:
    print(*i)
