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


s= input()
mp = defaultdict(int)
for i in range(26):
    mp[s[i]] = i
n = int(input())
a = []
for i in range(n):
    a.append(input())
a.sort(key = lambda x: [mp[i] for i in x])
print(*a, sep="\n")
