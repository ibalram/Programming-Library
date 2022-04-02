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

k = int(input())
a,b = imap()

n,m = 0,0
power = 1
def change(a):
    n = 0
    power = 1
    for i in str(a)[::-1]:
        n+=power*(int(i))
        a//=k
        power*=k
    return n
n,m = change(a), change(b)
# print(n,m)
print(n*m)
