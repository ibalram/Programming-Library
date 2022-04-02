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


for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        r = list(map(int,input().split()))
        a.append(r)
    aux = [[0]*5 for i in range(n)]
    for i in range(5):
        b = [[a[j][i],j] for j in range(n)]
        b.sort()
        for j in range(n):
            aux[b[j][1]] = j
    for i in range(n):
        sm = sum(n-aux[])









# for _ in range(int(input())):
#     n = int(input())
#     ls = []
#     for i in range(n):
#         a = list(map(int,input().split()))
#         # a.sort()
#         ls.append([a,i])
#     if n==1:
#         print(1)
#         continue
#     # mp = defaultdict(int)
#     # for i in range(5):
#     #     ls.sort(key=lambda x: x[0][i])
#     #     j = n-1
#     res = -2
#     for i in range(5):
#         ls.sort(key=lambda x: x[0][i])
#         if ls[0][0][i]==ls[1][0][i]:
#             continue
#         x = ls[0][1]
#         for j in range(i+1,5):
#             ls.sort(key=lambda x: x[0][j])
#             if ls[0][0][j]==ls[1][0][j]:
#                 continue
#             y = ls[0][1]
#             for k in range(j+1,5):
#                 ls.sort(key=lambda x: x[0][k])
#                 if ls[0][0][k]==ls[1][0][k]:
#                     continue
#                 z = ls[0][1]
#                 if x==y==z:
#                     res = x
#                     break
#             if res>-1:
#                 break
#         if res>-1:
#             break
#     print(res+1)

