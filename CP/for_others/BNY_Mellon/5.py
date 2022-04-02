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

n = int(input())
m = int(input())
d = int(input())
a = []
for i in range(m):
    a.append(int(input()))

# print(*a)





def solve(n,m,d,a):
    from collections import defaultdict, deque
    mp = defaultdict(int)
    for i in a:
        mp[i] = 1
    q = deque()
    q.append((0,0))
    while q:
        node,moves = q.popleft()
        if node>=n:
            return moves
        for j in range(min(n,node+d),node,-1):
            if j not in mp:continue
            q.append((j,moves+1))
    return -1




print(solve(n,m,d,a))

