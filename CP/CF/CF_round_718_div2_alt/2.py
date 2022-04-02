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


from heapq import heapify, heappop, heappush
for _ in range(int(input())):
    n, m = map(int,input().split())
    b = []
    piv = 0
    for i in range(n):
        x = sorted(list(map(int,input().split())), reverse = True)

        b.append([x,i])
    res = [[0]*(m) for i in range(n)]
    for i in range(m):
        idx = -1
        val = float("inf")
        y = -1
        for j in range(n):
            if b[j][0] and b[j][0][-1]<val:
                idx =b[j][1]
                val = b[j][0][-1]
                y = j
        b[y][0].pop()
        res[idx][i] = val
    for x,i in b:
        j = 0
        k = 0
        while j<m:
            if res[i][j]:
                j+=1
                continue
            res[i][j] = x[k]
            k+=1
            j+=1

    for i in res:
        print(*i)
        # piv+=1
    # dp = [[[0]*(n+1) for j in range(m+1)] for i in range(n+1)]
    # def rec(i,j,k):
    #
    # mins =
    # heapify(b)
    # res = [[] for i in range(m)]
    # # b.sort()
    # cnt = 0
    # while b:
    #     x,i = heappop(b)
    #     res[cnt].append([x[0],i])
    #     if len(x)>1:
    #         heappush(b,[x[1:],i])
    #     cnt+=1
    #     cnt%=m
    # ans = [[0]*m for i in range(n)]
    # for i in res:
    #     print(*i)
    # for i in range(m):
    #     for j in range(n):
    #         ans[res[i][j][1]][i] = res[i][j][0]



    # for i in range(n):
    #     x = b[i][0]
    #     res[b[i][1]] = x[piv:]+x[:piv]
    #     piv+=1
    # for i in range(n):
    #     print(*ans[i])
