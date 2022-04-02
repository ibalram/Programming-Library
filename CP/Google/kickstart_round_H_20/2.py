from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

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

for _ in range(int(input())):
    l,r = imap()
    res = 0
    ldig = len(str(l))
    rdig = len(str(r))
    def getOdd(x):
        cnt = 0
        for i in range(x,10):
            if i%2:
                cnt+=1
        # print(cnt,"odd")
        return cnt
    def getEven(x):
        cnt = 0
        for i in range(x,10):
            if i%2==0:
                cnt+=1
        # print(cnt)
        return cnt

    def rec2(num):
        num = str(num)
        sz = len(str(num))
        ret = 1
        # print(num)
        for i in range(len(num)):
            if i%2==0:
                ret*=getOdd(int(num[i]))
            else:
                ret*=getEven(int(num[i]))
        print(ret)
        return ret

    dp = {}
    @lru_cache(None)
    def rec(st):
        # if st in dp:
        #     return dp[st]
        pos = len(st)+2
        if l<=int(st)<=r:
            res = 1+sum(rec(st+str(i)) for i in range(10) if pos%2 == i%2)
            # dp[st] = res
            return res
        if int(st)>r:
            return 0
        res = 0
        for i in range(10):
            if pos%2 == i%2:
                res+= rec(st+str(i))
        # dp[st] = res
        return res

    @lru_cache(None):
    def rec3(cnt):
        if cnt>rdig:
            return 0
        if cnt==rdig:
            if cnt==ldig:
                lnum = str(l-1)
                rnum = str(r)
                ret = 1
                for i in range(cnt):
                    if i%2==0:
                        ret*=getOdd(int(lnum[i]))-getOdd(int(rnum[i]))
                    else:
                        ret*=getEven(int(lnum[i]))-getEven(int(rnum[i]))
                return ret
            else:
                lnum = str(l-1)
                rnum = str(r)
                ret = 1
                for i in range(cnt):
                    if i%2==0:
                        ret*=getOdd(int(lnum[i]))-getOdd(int(rnum[i]))
                    else:
                        ret*=getEven(int(lnum[i]))-getEven(int(rnum[i]))
                return ret
    # def brute(l,r):
    #     ret = 0
    #     def check(x):
    #         num = str(x)
    #         for i in range(len(num)):
    #             j = i+1
    #             if j%2!=int(num[i])%2:
    #                 return False
    #         return True

    #     for i in range(l,r+1):
    #         ret+=check(i)
    #     return ret
    # print(brute(l,r))
    res = rec("0")
    # print(list(dp.items())[:10])
    # dp = [5, 5]+[0]*18
    # for i in range(2,20):
    #     dp[i] = dp[i-1]*5+5
    # dp[1] = 6
    # # print(dp)

    # seq = [l]
    # i = 10**(ldig)
    # j = 10**(rdig-1)
    # while i<r:
    #     if i>l:
    #         seq.append(i)
    #     i*=10
    # seq.append(r)

    print("Case #{}:".format(_+1), res)
dp = [5, 5]+[0]*18
for i in range(2,20):
    dp[i] = dp[i-1]*5+5
print(dp)

# 1 1000000000 Case #4: 2441405
