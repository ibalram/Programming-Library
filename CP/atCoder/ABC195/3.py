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
m = len(str(n))

def get(n):
    m = len(str(n))
    res = 0
    prev = 0
    mm = 0
    for i in range(1,m):
        cur = 10**(i)
        res+=(i-1)//3 *(cur-prev)
        prev = cur
    res+=(m-1)//3 *(n-prev+1)

    return res


mx = 0
cnt = 0
print(get(n))
