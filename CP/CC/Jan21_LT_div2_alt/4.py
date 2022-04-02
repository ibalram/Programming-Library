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


import os, sys, bisect
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    f = 1
    b =[]
    for i in a:
        b.append(i%k)
    b.sort(reverse=True)
    i = 0
    # while i<n and b[i]==0:i+=1
    # b = b[i:]
    while b and b[-1]==0:b.pop()
    # print(*b)
    j = b[i-1]
    while b:
        x = b.pop()
        y = k-x
        i =0
        while i<32 and x*(1<<i)<y:
            i+=1
        curF = 0
        if x*(1<<i)==y:
            curF = 1
        if curF==0 and b:
            while y>0:
                idx = bisect.bisect_right(b,y)-1
                if idx<0:
                    break
                y-=b[idx]*(y//b[idx])
                if y<=0:
                    if y==0:
                        curF = 1
                    break
        if curF==0:
            f = 0
            break
    print("YES" if f else "NO")




    # a.sort()
    # from math import gcd
    # gc = 0
    # for i in range(1,n):
    #     gc = gcd(gc, a[i]-a[i-1])
    # res = "YES"
    # for i in a:
    #     if abs(i-k)%gc!=0:
    #         res = "NO"
    #         break
    # print(res)
