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
    a = input().split()
    # st = set(a)
    res = 0
    mp = defaultdict(list)
    for word in a:
        mp[word[1:]].append(word[0])
    for i in mp:
        for j in mp:
            sz = len(set(mp[i]+mp[j]))
            res+=(sz-len(mp[i]))*(sz-len(mp[j]))
    print(res)





# for _ in range(int(input())):
#     n = int(input())
#     a = input().split()
#     st = set(a)
#     res = 0
#     for i in range(n):
#         for j in range(n):
#             res+=a[i][0]+a[j][1:] not in st and a[j][0]+a[i][1:] not in st
#     print(res)
