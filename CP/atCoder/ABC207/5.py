import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

n = int(input())
a = ilist()

dp = {}
def rec2(start, cur, cnt, sm, ends):
    if cur>=n:
        if sm%cnt==0:
            print(ends+[cur])
        return sm%cnt==0

    # if (start,cur,cnt,sm) in dp:
    #     return dp[(start,cur,cnt,sm)]
    res = rec2(start, cur+1, cnt, sm+a[cur], ends[:])
    if sm%cnt==0:
        res+=(res+ rec2(cur, cur+1, cnt+1, a[cur], ends[:]+[cur]))%mod
    # dp[(start,cur,cnt,sm)] = res
    return res
# print(rec(0,1,1,a[0], []))
# print(dp)


pf = a[:]
for i in range(1,n):
    pf[i]+=pf[i-1]

@lru_cache(None)
def rec(n,idx):
    if idx<=1:
        return 1
    res = 0
    for i in range(idx-2,n):
        if (pf[n]-pf[i])%idx==0:
            res+=rec(i,idx-1)
            res%=mod
    return res

def dp(N,Idx):
    dp = [[0]*(Idx+1) for i in range(N+1)]
    for n in range(N+1):
        dp[n][0] = 1
        dp[n][1] = 1
        for idx in range(2,Idx+1):
            dp[n][idx] = 0
            for i in range(idx-2, n):
                if (pf[n]-pf[i])%idx==0:
                    dp[n][idx]+=dp[i][idx-1]
    return dp[N][Idx]

res = 0
for idx in range(1,n+1):
    res+=dp(n-1,idx)
    res%=mod
print(res)




