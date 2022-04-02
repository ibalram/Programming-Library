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

# for _ in range(1,int(input())+1):
#     res = 0
#     n = int(input())
#     a = ilist()
#     b = []
#     # for i in range(1,n):
#     #     b.append(a[i]-a[i-1])
#     for i in range(n):
#         if i>0:
#             b.append(a[i-1]-a[i])
#     b+=[0,0]
#     ln= ans=2
#     index=0
#     f=False
#     for i in range(1,n):
#         if b[i]!=b[i-1] and not f:
#             f = True
#             temp=b[i-1]
#             ln+=1
#             index=i
#             if b[i]>b[i-1]:
#                 b[i+1]+=abs(b[i]-b[i-1])
#             else:
#                 b[i+1]-=abs(b[i]-b[i-1])
#             b[i]=temp
#         elif b[i]!=b[i-1] and f:
#             f=False
#             ans = max(ln, ans)
#             ln= i-index-1
#             i=index+3
#         else:
#             ln+=1

#     # for i in range(n):
#     #     done = 0
#     #     for j in range(i+1,n):
#     #         diff = a[i]-a[j]

#     # for ln in range(1,n-1):
#     #     for i in range(n-ln):

#     # print(*b)
#     # mark = [0]*(n)
#     # bad = [0]*(n)
#     # for i in range(1,n-1):
#     #     if a[i]-a[i-1] != a[i+1]-a[i]:
#     #         mark[i] = 1
#     #         if (a[i-1]+a[i+1])&1:
#     #             bad[i] = 1
#     # print(bad)
#     # print(mark)
#     print("Case #{}: {}".format(_, max(ln,ans)))



"""
Given an array A of size n (1<=n<=10^6). Find the number of pairs (i,j)
such that (1<=i<j<=n) and A[i]*A[j]==A[i]+A[j]

def solve(a):
    n = len(a)
    # m = len(b)
    res = 0
    for i in range(n):
        # for j in range(m):
        for j in range(i+1,n):
            if a[i]*a[j]==a[i]+a[j]:
                res+=1
    return res
a = [1,2,3,4]
# b = [1,2,3,4]
print(solve(a))
"""
