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

from heapq import heapify, heappop, heappush
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    even  = []
    odd = []
    smEven = 0
    smOdd = 0

    for i in a:
        if i%2==0:
            smEven+=i
            even.append(i)
        else:
            smOdd+=i
            odd.append(i)
    # odd = n-even
    # if odd>even:
    #     print("Tie")
    # if smEven>smOdd:
    #     print("Alice")
    # elif smEven<smOdd:
    #     print("Bob")
    # else:
    #     print("Tie")
    x = 0
    even.sort()
    odd.sort()
    for i in range(n):
        # print(even,odd)
        if even and odd:
            xx = even[-1]
            yy = odd[-1]
            mx = max(xx,yy)
            if i%2==0:
                if mx==xx:
                    even.pop()
                    x+=mx
                else:
                    odd.pop()
            else:
                if mx==xx:
                    even.pop()
                else:
                    odd.pop()
                    x-=mx
            continue
        if i%2:
            #even
            if not even:
                x-=odd.pop()#-heappop(odd)
            else:
                even.pop()#heappop(even)
        else:
            #odd
            if not odd:
                x+=even.pop()#-heappop(even)
            else:
                odd.pop()#heappop(odd)
    # x = sum(even)-sum(odd)
    res = "Tie"
    if x>0: res = "Alice"
    elif x<0: res = "Bob"
    print(res)
