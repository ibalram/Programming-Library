from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    res = 0
    x,y,s = input().split()
    x = int(x)
    y = int(y)
    a = [i for i in s if i!='?']
    for i in range(1,len(a)):
        res+=x*(a[i-1:i+1]==['C','J'])
        res+=y*(a[i-1:i+1]==['J','C'])
    print("Case #{}:".format(_+1),res)

