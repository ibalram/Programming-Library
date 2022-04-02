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

for _ in range(int(input())):
    a,b,c,m = map(int,input().split())
    mx = a+b+c-3
    x = [a,b,c]
    x.sort()
    rem = x[2] - x[0]-x[1]
    # print(rem)
    # rem = max(0,x[2]-x[1])
    # print(rem)
    # x = [min(rem,x[0]), max(rem,x[0])]
    # rem = max(0,x[1]-x[0]-1)
    # print(rem)
    if m>mx or m<rem-1:
        print("no")
        continue
    print("yes")
