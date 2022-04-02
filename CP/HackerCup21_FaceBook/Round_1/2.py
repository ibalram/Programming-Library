import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("weak_typing_chapter_2_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    res = 0
    n = int(input())
    s = input().strip()
    distinct = []
    ns = []
    for i in range(n):
        if s[i]!="F": ns.append([s[i],i])
    for i in range(1,len(ns)):
        if ns[i][0]!=ns[i-1][0]:
            distinct.append([ns[i-1][1],ns[i][1]])
    res = 0
    for i,j in distinct:
        res = (res + (i+1)*(n-j))%mod

    print("Case #{}: {}".format(_+1, res))

