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
sys.setrecursionlimit(2*10**6)

mod = int(1e9+7)

for _test in range(int(input())):
    res = 0
    n,m,k = imap()
    l = [0]*n
    r = [0]*n
    a = [0]*n
    for i in range(n):
        l[i],r[i],a[i] = imap()
    gr = defaultdict(list)
    for i in range(m):
        x,y = imap()
        gr[x].append(y)
        gr[y].append(x)
    count = 0
    def dfs(points, candidates, vis):
        global count
        if points==k:
            # count+=1
            # print(path)
            return 1
        # if len(vis)==n:
        #     return 0
        if not candidates:
            return 0
        ln = len(candidates)
        res = 0
        for i in range(ln):
            cand = candidates[i]
            if l[cand]<=points<=r[cand]:
                new = []
                for j in gr[cand]:
                    if j not in vis:
                        new.append(j)
                # newVis = vis|set(new)
                # newCands = candidates[:i]+candidates[i+1:]+new
                res+=dfs(points+a[cand], candidates[:i]+candidates[i+1:]+new, vis|set(new))
        return res
    res = 0
    for i in range(n):
        res += dfs(a[i], gr[i][:], set(gr[i][:]+[i]))
    print('Case #{}:'.format(_test+1), res)
# print(8*7*6*5*4*3*2*8)
