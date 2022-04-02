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

def findSmallest(n):
    if n < 10:
        return n
    for i in range(9,1,-1):
        while n % i == 0:
            n = n / i
            res.append(i)
    if n > 10:
        return
    n = res[len(res)-1]
    for i in range(len(res)-2,-1,-1):
        n = 10 * n + res[i]
    print n

for _ in range(int(input())):
    k= int(input())
    a = [9]*(k)
    prod =
