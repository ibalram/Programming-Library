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

s = input().strip()
a = []
mn = s
mx = s
n = len(s)
for i in range(n):
    # a.append(s[i:]+s[:i])
    cur = s[i:]+s[:i]
    mn = min(mn,cur)
    mx = max(mx,cur)
print(mn,mx, sep="\n")
# print(a)
# a.sort()
# print(a[0])
# print(a[1])
