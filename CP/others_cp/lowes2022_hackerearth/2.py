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

n = int(input())
s = list(int(i) for i in input().strip())
q = list(int(i) for i in input().strip())




def maxProfit2(N,S,Q):
    S = [int(i) for i in S]
    Q = [int(i) for i in Q]
    res = 0
    for ln in range(1,n+1):
        mn = 100000000
        for s1 in range(n-ln+1):
            for s2 in range(n-ln+1):
                val = 0
                for i in range(ln):
                    val = 2*val+(S[s1+i]^Q[s2+i])
                mn = min(mn, val)
        res = max(res, ln/(2**mn))
    return int(res)




def maxProfit(N,S,Q):
    S = [int(i) for i in S]
    Q = [int(i) for i in Q]
    dp = [[0 for j in range(N+1)]for i in range(2)]
    turn = 0
    idxS = 0
    idxQ = 0
    maxSoFar = 0
    for i in range(N+1):
        for j in range(N+1):
            if (i == 0 or j == 0):
                dp[turn][j] = 0
            elif (S[i-1] == Q[j-1]):
                dp[turn][j] = dp[(1-turn)%2][j-1]+1
                if dp[turn][j]>maxSoFar:
                    maxSoFar = dp[turn][j]
                    # idxS = i-1
                    # idxQ = j-1
                # elif dp[turn][j]==maxSoFar:
                #     if i-1<=idxS and j-1<=idxQ:
                #         idxS = i-1
                #         idxQ = j-1
            else:
                dp[turn][j] = 0
        turn ^= 1
    # print(maxSoFar, idxS, idxQ)
    return maxSoFar #+(maxSoFar!=0 and idxS!=N-1 and idxQ!=N-1)


from random import *
t = 1
while t:
    n = randint(1,10)
    s = [randint(0,1) for i in range(n)]
    q = [randint(0,1) for i in range(n)]
    res1 = maxProfit(n,s,q)
    res2 = maxProfit2(n,s,q)
    if res1==res2:
        print(n)
        print(*s)
        print(*q)
        print(res1, res2)
        break
    t-=1



# print(maxProfit(n,s,q))
# print(maxProfit2(n,s,q))
