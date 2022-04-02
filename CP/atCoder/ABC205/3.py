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

a,b,c = imap()

# a = pow(a,c)
# b = pow(b,c)
if c%2==0:
    a = abs(a)
    b = abs(b)

s = "="
if a>b:
    s = ">"
elif a<b:
    s = "<"
print(s)
