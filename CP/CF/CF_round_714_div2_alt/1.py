import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)








# n = input()

def soln(n):
    if n==3:
        return 4
    if n==2:
        return 2
    if n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    # return soln(n)
    # return soln(n-1)+soln(n-2)+soln(n-3)
    dp[n] = soln(n-1)+soln(n-2)+soln(n-3)
    return dp[n]
dp = [-1]*(51)
print(soln(50))
