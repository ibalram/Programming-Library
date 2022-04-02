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


def solve2(n,a):
    count = 0
    n = len(a)
    for i in range(0,n,2):
        fd = a[i]+1
        if a[i]&1:
            fd = a[i]-1
        if a[i+1]==fd:
            continue
        for j in range(i+2,n):
            #print(a[j],fd)
            if a[j]==fd:
                a[i+1],a[j]=a[j],a[i+1]
                count+=1
    return count




def solve(n,a):
    if n%2:
        return -1
    res = 0
    f = 0
    for i in range(0,n,2):
        if a[i]==a[i+1]:
            continue
        for j in range(i+2, n):
            if a[i]==a[j]:
                for k in range(i+1,j):
                    a[k+1] = a[k]
                a[i+1] = a[j]
                res+=j-i-1
                f = 1
                break
        if f==0: return -1
    return res


def solve3(n,a):
    mp = [0]*(100002)
    res = 0
    for i in range(n):
        if mp[a[i]] == 0:
            mp[a[i]] = 1
            cnt = 0
            for j in range(i+1, n) :
                if mp[a[j]] == 0:
                    cnt+=1
                elif a[i] == a[j]:
                    res+=cnt
    return res



n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

print(solve(n,a))
