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

from math import floor, ceil
def encrypt(words):
    a = words.replace(" ", "")
    mx = len(a)
    sqr = mx**.5
    n = floor(sqr)
    m = floor(sqr)
    if n*m<mx:
        m = ceil(sqr)
    if n*m<mx:
        n = ceil(sqr)
    # print(n,m)
    res = ["".join(a[j] for j in range(i,len(a),m)) for i in range(m)]
    return " ".join(res)

a = input().strip()

print(encrypt(a))
