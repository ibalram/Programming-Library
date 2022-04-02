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
class BIT:
    # https://juppy.hatenablog.com/entry/2018/11/17/%E8%9F%BB%E6%9C%AC_python_Binary_Indexed_Tree_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0
    def __init__(self,N):
        self.N = N + 1
        self.bit = [0]*(N+1)

    def __query__(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            # print(self.bit[idx])
            idx -= idx&(-idx) # 最後に立っている 1 のビットを減算
        return res

    def query(self, l, r=-1):
        if r==-1:
            return self.__query__(l)
        else:
            return self.__query__(r-1) - self.__query__(l-1)

    def add(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx) # 最後に立っている 1 のビットを加



def solve(n,k,b):
    a = [defaultdict(lambda :float("inf")) for i in range(n)]
    res = float("inf")
    for i in range(n):
        sm = sum(b[:i+1])
        for j in range(i+1):
            if sm==k:
                res = min(res, i-j+1)
            for l in range(j):
                if a[l][k-sm]!=float("inf"):
                    res = min(res, i-j+1+a[l][k-sm])
            a[i][sm] = min(a[i][sm],i-j+1)
            sm-=b[j]
    return res if res!=float("inf") else -1

    # a.sort()
    # res = float("inf")
    # for i in range(len(a)):
    #     x,y,sm = a[i]
    #     if sm==k:
    #         res = min(res,y-x+1)
    #         continue
    #     for j in range(i+1,len(a)):
    #         xx,yy,ssm = a[j]
    #         if xx<=y:continue
    #         if ssm+sm==k:
    #             res = min(res, y-x+1+yy-xx+1)
    return res if res<float("inf") else -1





for _test in range(int(input())):
    res = 0
    n,k = imap()
    b = ilist()
    res = solve(n,k,b)

    print('Case #{}:'.format(_test+1), res)
