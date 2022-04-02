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
mod = 998244353

n = int(input())
a = ilist()
b = list(range(n))
b.sort(key=lambda x: a[x])
# st = []
# dp = [0]*(n+1)
# for i,v in enumerate(b):
#     while st and b[st[-1]]>v:
#         st.pop()
#     if st:
#         dp[i] = dp[st[-1]]+v-b[st[-1]]
#     st.append(i)
# res = 0
# print(b)
# print(dp)
# for i in dp[1:n]:
#     if i>1:
#         res += pow(2,i-1,mod)
#         res%=mod
# Binary Indexed Tree (Fenwick Tree; フェニック木)
# 数列A1,..Anが与えられたときに以下のそれぞれをO(logN)で実現するデータ構造
# 要素の更新：任意のi, xに対してAi += x を行う
# 部分和：任意のiに対して A1+A2+..+Aiの値を求める
class BIT:
    # https://juppy.hatenablog.com/entry/2018/11/17/%E8%9F%BB%E6%9C%AC_python_Binary_Indexed_Tree_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0
    # SegTreeより軽いので積極的に使う
    def __init__(self,N):
        self.N = N + 1
        self.bit = [0]*(N+1)

    def __query__(self,i):
        # return sum of [0, i]
        # return 0 if i == -1
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            # print(self.bit[idx])
            idx -= idx&(-idx) # 最後に立っている 1 のビットを減算
        return res

    def query(self, l, r=-1):
        """sum of [l, r) if r else [0, l+1)
        Returns:
            int: sum of [l, r) if r else [0, l+1)
        """
        if r==-1:
            return self.__query__(l)
        else:
            return self.__query__(r-1) - self.__query__(l-1)

    def add(self,i,x):
        """Ai += x: O(log N)
        """
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx) # 最後に立っている 1 のビットを加

res = 0
dp = BIT(n)
print(b)
for i in b:
    dp.add(i,1)
    dp.add(n,-1)
    x = dp.query(i)
    print(x, i)
    if x>1:
        res = (res+pow(2,x-2,mod))%mod
    print(dp.bit)

    # print(dp)
# for i in dp[:n]:
#     if i>1:
#         res = (res+pow(2,i-2, mod))%mod
print(res)



