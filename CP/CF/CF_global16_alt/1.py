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
    n,s = map(int,input().split())
    first = (n//2 if n&1 else n//2-1)
    # s-=first
    av = s//(n-first)
    print(av)

    # av = s//n
    # rem = s-av*n
    # if n&1:
    #     rest = s-n//2
    #     av = rest//(n//2+1)
    #     rem = rest  - av*(n//2+1)
    #     print(av+(rem>=(n//2)+1))
    # else:
    #     rest = s-n//2+1
    #     av = rest//(n//2+1)
    #     rem = rest  - av*(n//2+1)
    #     if rem>=n//2+1:
    #         print(av+1)
    #     else:
    #         print(av)

"""
14//4 = 3
2 4 4 4
3 5
1 2 2

"""
