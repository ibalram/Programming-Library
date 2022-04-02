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

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def solve(k,rectangles):
    coord = (-1,-1)
    minDist = float("inf")
    for i in range(-100,101):
        for j in range(-100,101):
            tot = 0
            for x1,y1,x2,y2 in rectangles:
                tot+=dist((i,j),(x1,y1))
                tot+=dist((i,j),(x2,y2))
                tot+=dist((i,j),(x1,y2))
                tot+=dist((i,j),(x2,y1))
            if tot<minDist:
                coord = (i,j)
                minDist = tot
    return coord

for _test in range(int(input())):
    res = 0
    k = int(input())
    rectangles = []
    for i in range(k):
        rectangles.append(ilist())
    res = solve(k,rectangles)
    print('Case #{}:'.format(_test+1), *res)
