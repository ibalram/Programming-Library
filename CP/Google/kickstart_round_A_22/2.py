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
    number = 0
    n = input().strip()
    for i in n:
        number = (number*10+int(i))%9
    if number==0:
        res = n[:1]+"0"+n[1:]
    else:
        idx = 0
        number = 9-number
        while idx<len(n) and int(n[idx])<=number:
            idx+=1
        res = n[:idx]+str(number)+n[idx:]
    print('Case #{}:'.format(_test+1), res)
