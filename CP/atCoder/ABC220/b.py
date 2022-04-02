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
t = input().strip()
n = len(s)
if s==t:
    print("Yes")
else:
    res = "No"
    for i in range(n-1):
        if s[i:i+2]==t[i:i+2][::-1] and s[:i]==t[:i] and s[i+2:]==t[i+2:]:
            res = "Yes"
            break
    print(res)
