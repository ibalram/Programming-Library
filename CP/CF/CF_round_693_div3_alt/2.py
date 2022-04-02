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
    n = int(input())
    a = list(map(int,input().split()))
    two = 0
    for i in a:
        two+=i==2
    one = n-two
    if sum(a)%2:
        print("No")
    elif one%2==two%2==0:
        print("Yes")
    else:
        sm1  =0
        sm2 = 0
        while two:
            if sm1<sm2:
                sm1+=2
            else:
                sm2+=2
            two-=1
        while one:
            if sm1<sm2:
                sm1+=1
            else:
                sm2+=1
            one-=1
        print("No" if sm1!=sm2 else "Yes")

