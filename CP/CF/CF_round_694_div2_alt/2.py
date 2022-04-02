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
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    # a = [1<<12]*(100000)
    # n = 100000
    res = 0
    for i in range(n):
        a[i] = [a[i],1]
    # for i in a:
    #     if i%x:
    #         break
    #     # res+=i
    #     a+=[i//x]*x
    q = deque(a)
    while q:
        s,cnt = q.popleft()
        # print(len(q))
        res+=s*cnt
        if s%x:
            res+=sum(i[0]*i[1] for i in q)
            break
        q.append([s//x, cnt*x])
    print(res)

    # print(len(a))
    # print(sum(a))
