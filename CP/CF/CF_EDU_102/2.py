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

from math import gcd
lcm = lambda x,y: x*y//gcd(x,y)
for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    if len(s)>len(t):
        s,t = t,s
    # cnt = len(t)//len(s)
    # if cnt*s==t:
    #     x = int(lcm(len(t), len(s))//cnt)
    #     print("".join(list(s)*x))
    # elif len(set(i for i in s))==len(set(i for i in t))==1:
    #     print(s[0]*(lcm(len(s), len(t))))
    # else:
    #     print(-1)
    lc = lcm(len(s), len(t))
    s2 = s*(lc//len(s))
    t2 = t*(lc//len(t))
    print(s2 if s2==t2 else -1)
