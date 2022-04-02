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


from collections import defaultdict, Counter, deque;

for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        a[i] = [a[i],i]
    mark = [0]*(m+1)
    a.sort(reverse=True, key = lambda x: b[x[0]-1])
    res =0
    cntr = 0
    for i in range(n):
        if cntr<a[i][0]:
            res+=b[cntr]
            cntr+=1
        else:
            res+=b[a[i][0]-1]
    print(res)
