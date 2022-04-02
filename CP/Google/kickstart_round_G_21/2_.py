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

def solve2(k,rectangles):
    def fx(mid):
        sm = 0
        for x1,x2,y1,y2 in rectangles:
            sm+=min(abs(mid-x1),abs(mid-x2))
        return -sm
    def fy(mid):
        sm = 0
        for x1,x2,y1,y2 in rectangles:
            sm+=min(abs(mid-y1),abs(mid-y2))
        return -sm
    def tern(lo,hi,f):
        while (hi - lo > 1):
            mid = (hi + lo)>>1
            if (f(mid) > f(mid + 1)):
                hi = mid
            else:
                lo = mid
        return lo
    lx = min(min(i[0],i[2]) for i in rectangles)
    rx = max(max(i[0],i[2]) for i in rectangles)
    ly = min(min(i[1],i[3]) for i in rectangles)
    ry = max(max(i[1],i[3]) for i in rectangles)
    return tern(lx,rx+1,fx),tern(ly,ry+1,fy)

def solve(k,rectangles):
    coord = (-1,-1)
    minDist = float("inf")
    x = []
    y = []
    for x1,y1,x2,y2 in rectangles:
        x.append(x1+x2>>1)
        y.append(y1+y2>>1)
    x.sort()
    y.sort()
    n = k
    x1, y1= (x[n//2-1]+x[n//2]), (y[n//2-1]+y[n//2])
    if k%2==0: print(x1,y1)
    x = max(x)+min(x)>>1
    y = max(y)+min(y)>>1
    return x,y
    # for i in range(-100,101):
    #     for j in range(-100,101):
    #         tot = 0
    #         for x1,y1,x2,y2 in rectangles:
    #             tot+=dist((i,j),(x1,y1))
    #             tot+=dist((i,j),(x2,y2))
    #             tot+=dist((i,j),(x1,y2))
    #             tot+=dist((i,j),(x2,y1))
    #         if tot<minDist:
    #             coord = (i,j)
    #             minDist = tot
    return coord

for _test in range(int(input())):
    res = 0
    k = int(input())
    rectangles = []
    for i in range(k):
        rectangles.append(ilist())
    res = solve2(k,rectangles)
    print('Case #{}:'.format(_test+1), *res)
