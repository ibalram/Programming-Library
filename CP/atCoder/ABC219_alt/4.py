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
mp = defaultdict(set)
for i in range(n):
    x,y = imap()
    mp[x].add(y)
# for i in mp:
#     mp[x].sort()

keys = list(mp.keys())
m = len(keys)
res = 0
# print(mp)
for i in range(m):
    for j in range(i+1,m):
        x = len(mp[keys[i]]&mp[keys[j]])
        # print(mp[i]&mp[j],mp[i],mp[j])
        res+=x*(x-1)//2
print(res)



"""
    1 6   2,6

    1,2   2,2
"""
