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

for _ in range(1,int(input())+1):
    res = 0
    n = int(input())
    s = input().strip()
    lst = 1
    res = [1]
    for i in range(1,n):
        if s[i]>s[i-1]:
            lst+=1
        else:
            lst = 1
        res.append(lst)

    print("Case #{}:".format(_), *res)
