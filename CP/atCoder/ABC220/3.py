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
a = ilist()
x = int(input())
for i in range(1,n):
    a[i]+=a[i-1]
if x<a[-1]:
    print(bisect.bisect_right(a,x)+1)
else:
    copies = x//a[-1]
    rem = x%a[-1]
    # print(copies,rem, copies(a[-1]))
    print(copies*n + bisect.bisect_right(a,rem)+1)
