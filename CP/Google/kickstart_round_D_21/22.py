import os, sys, bisect
from heapq import heapify, heappop, heappush
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

for _test in range(int(input())):
    res = 0
    n,c = imap()
    intervels = []
    a = []
    # start =
    mp = [0]*(10**5)
    for i in range(n):
        intervels.append(ilist())
        x,y = intervels[i]
        a.append((x,-1))
        a.append((y,1))
        for j in range(x+1,y):
            mp[j]+=1
    mp.sort(reverse = True)
    if
    print('Case #{}:'.format(_test+1), res)
