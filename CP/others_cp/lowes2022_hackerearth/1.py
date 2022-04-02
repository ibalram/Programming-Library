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
b = list(range(n))


def awesomeSort(N, arr):
    b = list(range(N))
    b.sort(key = lambda x: (((0,0,-arr[x]) if arr[x]%5==0 else (0,1,-x)) if arr[x]%2==0 else (1,1,1)))
    return [arr[i] for i in b]






print(awesomeSort(n,a))
