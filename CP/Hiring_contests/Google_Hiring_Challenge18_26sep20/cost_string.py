import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------

for _ in range(int(input())):
    a = list(mapi())[::-1]
    # print(len(a))
    w = int(input())
    res = []

    def rec(cur,w):
        if w==0:
            return True,""
        res = ""
        # print(cur,w)
        for i in range(cur,26):
            # print(w)
            # while a[i]<=w and w:
            # w-=a[i]
            # res.append(chr(25-i+ord("a")))
            if a[i]<=w:
                flag, st = rec(i,w-a[i])
                if flag: return True,chr(25-i+ord("a"))+st
        return False,""
    # print("".join(res))
    print(rec(0,w))
