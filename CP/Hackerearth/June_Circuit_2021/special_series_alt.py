import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

"""
f1 = 1
f2 = 1
f3 = 2
f4 = 3
f5 = 9+1/2 = 5
f6 = 25-1/3 = 8
f7 = 64+1/5 = 13
f8 = 169-1/8 = 21
"""
