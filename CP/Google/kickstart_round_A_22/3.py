import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)

mod = int(1e9+7)
palins = []
# @lru_cache(None)
def mak(i,s, sz):
    if i>=sz:
        if s[::-1]==s:
            palins.append(s)
        return
    mak(i+1, s+'0',sz)
    mak(i+1, s+'1',sz)
mak(0,'',5)
mak(0,'',6)
# print(len(palins))
print(*palins, sep="\n")
for _test in range(int(input())):
    res = 0
    n = int(input())
    s = list(input().strip())
    def rec(i):
        if i>=n:
            st = "".join(s)
            # print(st)
            # for i in range(4,n):
            #     print(st[i-4:i+1], palins)
            #     if st[i-4:i+1] in palins:
            #         return False
            for i in palins:
                if i in st:
                    return False
            return True
        if s[i]!='?':
            return rec(i+1)
        else:
            flag = False
            s[i] = '0'
            flag|=rec(i+1)
            s[i] = '1'
            flag|=rec(i+1)
            s[i] = '?'
            return flag
    res = "POSSIBLE" if rec(0) else "IMPOSSIBLE"
    print('Case #{}:'.format(_test+1), res)
