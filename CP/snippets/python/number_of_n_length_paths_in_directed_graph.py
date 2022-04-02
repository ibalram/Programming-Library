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



def usingBruteForce(graph, m, n):
    """
    # graph: m*m adjacency matrix of graph
    # m: number of nodes
    # n: length of path
    # return number of n length paths
    # TC: O(m^n)
    # SC: O(n)
    """

    def rec(cur,n):
        if n<=0:
            return 1
        res = 0
        for i in range(m):
            if not graph[cur][m]: continue
            res+=rec(m,n-1)
            res%=mod
        return res


def usingMemoizedRecursion(graph, m, n):
    """
    # graph: m*m adjacency matrix of graph
    # m: number of nodes
    # n: length of path
    # return number of n length paths
    # TC: O(n*m)
    # SC: O(n)
    """
    @lru_cache(None)
    def rec(cur,n):
        if n<=0:
            return 1
        res = 0
        for i in range(m):
            if not graph[cur][m]: continue
            res+=rec(m,n-1)
            res%=mod
        return res
    return sum(rec(i,n) for i in range(m))

def usingMatrixExpo(graph, m, n):
    """
    # graph: m*m adjacency matrix of graph
    # m: number of nodes
    # n: length of path
    # return number of n length paths
    # TC: O(m^3*log(n))
    # SC: O(m^3)
    """
    res = UnitMatrix(m,m)
    n-=1 #because path with (n) nodes will be of (n-1) length(edges)
    while n>0:
        if n&1:
            res = Multiply(res,graph)
        graph = Multiply(graph,graph)
        n>>=1
    return sum(sum(i) for i in res)%mod






