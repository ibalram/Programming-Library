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


def getXor(m):
    n =m%4
    if n == 0 :
        return n
    if n == 1 :
        return 1
    if n== 2 :
        return n + 1
    return 0

pre = list(range(300010))
for i in range(1,300010):
    pre[i]^=pre[i-1]
for _ in range(int(input())):
    a,b = map(int,input().split())
    res = a
    xor = pre[a-1] #getXor(a-1)
    if xor==b:
        print(res)
    elif xor^b==a:
        print(res+2)
    else:
        print(res+1)

    # if xor==b:
    #     print(res)
    #     # elif xor==0 and a!=b or b==0:
    # elif xor==0 and a==b:
    #     print(res+2)
    # elif xor^b==a:
    #     print(res+1)

