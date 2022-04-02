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


def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):
    a = [x[i]*p[i]-y[i]*(1-p[i]) for i in range(noOfTradesAvailable)]
    q = [1.0-i for i in p]
    print(p)
    print(q)
    a.sort()
    res = 0
    for i in range(noOfTradesAvailable-1,max(-1,noOfTradesAvailable-maximumTradesAllowed-1) ,-1):
        print("DSF")
        res += max(0,a[i])
    return "{0:.2f}".format(res)


def calculateMinimumSession(n, m, a, b):
    mat = [[0]*m for i in range(n)]
    for i in range(n):
        for j in a[i]:
            mat[i][j-1]=1
    for j in range(m):
        for i in b[j]:
            mat[i-1][j]=1
    res1 = 0
    res2 = 0
    res = 0
    for i in range(n):
        res=max(res, mat[i].count(1))
    for i in range(m):
        res=max(res, [mat[j][i] for j in range(n)].count(1))
    # for i in mat:
    #     print(*i)
    # return min(res1, res2)
    return res

n,a = input().strip().split()
m,b = input().strip().split()
n, m = int(n),int(m)
a = [list(map(int,i.split("&"))) for i in a.split(",")]
b = [list(map(int,i.split("&"))) for i in b.split(",")]

print(calculateMinimumSession(n,m,a,b))
