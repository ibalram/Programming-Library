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
    x = int(input())
    it = 1
    counter = 0
    cnt = 1
    while counter<x:
        counter+=cnt
        cnt+=1
    diff = counter-x
    if counter-1==x:
        print(cnt)
    else:
        print(cnt-1)
    # print(diff)
    # sm = 0
    # while sm<diff:
    #     sm+=it
    #     it+=1
    # print()
    # print(cnt-1-max(0,it-1)+sm-diff)


# 1 2 3
# 4
# 6
