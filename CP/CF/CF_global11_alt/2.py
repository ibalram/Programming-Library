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

for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(input().strip())
    from collections import defaultdict
    mp = defaultdict(list)
    i = 0
    while i<n and s[i]=="L":
        i+=1
    cnt = 0
    lst = i
    while i<n:
        if s[i]=="L":
            cnt+=1
        else:
            if cnt:
                mp[cnt].append(lst)
            cnt = 0
            lst = i+1
        i+=1
    for i in sorted(mp.keys()):
        for idx in mp[i]:
            j = idx
            while j< n and s[j]=="L" and k>0:
                s[j] = "W"
                j+=1
                k-=1
                if k<=0:
                    break
            if k<=0:
                break
        if k<=0:
            break

    i =0
    mp2 = []
    # while i<n and s[i]=="L":
    #     i+=1
    cnt = 0
    res = 0
    while i<n:
        if s[i]=="W":
            cnt+=1
        else:
            if cnt:
                res+= 1+ 2*(cnt-1)
                mp2.append(cnt)
            cnt = 0
        i+=1

    if cnt:
        res+=1+2*(cnt-1)
        mp2.append(cnt)
    # print(mp2)
    if "W" in s:
        res += max(0,2*min(s.count("L"),k))
        pass
    else:
        res += max(0,2*min(s.count("L"),k)-1)
        pass
    # print("".join(s))
    print(res)
