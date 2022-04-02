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

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from functools import lru_cache
for _ in range(int(input())):
    n = int(input())
    # @lru_cache(None)
    # def rec(n):
    #     if n==0:
    #         return False
    #     m = n
    #     cnt = 0
    #     while m%2==0:
    #         m//=2
    #         cnt+=1
    #     res = False
    #     if cnt==0:
    #         if not rec(n-1):
    #             return True
    #     for i in range(1,cnt+1):
    #         if not rec(n//(1<<i)):
    #             return True
    #     return False
    bits = bin(n)[2:][::-1]
    m = len(bits)
    nxt = []
    dp = [[[-1]*2 for i in range(2)] for j in range(m+1)]
    # @lru_cache(None)
    def DP(i, turn, changed):
        if i>=m:
            return True
        if dp[i][turn][changed]!=-1:
            return dp[i][turn][changed]
        if bits[i]=="1":
            if not changed:
                dp[i][turn][changed] = not DP(i, turn^1, changed^1)
                return dp[i][turn][changed]
        res = (not DP(i+1,turn^1, 0))
        # lst = i
        # for j in range(i+1, m):
        #     if bits[j]=="1":
        #         lst = j-1
        #         break
        # res |= (not dp(i+1,turn^1, 0))
        if i+1<m and bits[i+1]=="0":
            res |= DP(i+1, turn, 0)
        # res |= (not dp(lst+1,turn^1, 0))
        dp[i][turn][changed] = res
        return dp[i][turn][changed]
    ans = DP(0,0,0)
    # ans2 = rec(n)
    print("Alice" if ans else "Bob")
    # print("Alice" if ans2 else "Bob")
    # print()


# print(18*18)
