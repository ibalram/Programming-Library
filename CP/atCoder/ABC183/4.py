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

n,w = imap()

arr = []
for i in range(n):
    s,t,p = imap()
    arr.append([s,-1,p])
    arr.append([t-1,+1,p])
arr.sort()
bal = 0
no = 0
# print(arr)
for time, f, use in arr:
    if f==-1:
        bal+=use
    else:
        bal-=use
    # print(time,use,f, bal)
    if bal>w:
        no = 1
        break
print("No" if no else "Yes")
