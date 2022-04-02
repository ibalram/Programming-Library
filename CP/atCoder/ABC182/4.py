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

prev = 0
cur = 0
mx = 0

pos = 0
res =0
for i in a:
    # print(prev,cur,pos)
    cur = prev+i
    res = max(res, pos+mx)
    pos+=cur
    prev = cur
    mx = max(mx,prev)
    res = max(res,pos)
# print(prev,cur,pos)
print(res)
