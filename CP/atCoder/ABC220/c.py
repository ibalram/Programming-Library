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

s = list(input().strip())
s.sort(reverse = True)
s = "".join(s)
n = len(s)
res = 0
for mask in range(1,1<<n-1):
    a = ''
    b = ''
    for i in range(n):
        if mask>>i&1:
            a+=s[i]
        else:
            b+=s[i]
    # print(a,b)
    if int(a)>=1 and int(b)>=1 and len(a)+len(b)==n:
        res = max(res, int(a)*int(b))
print(res)
# a,b = int(s[::2]), int(s[1::2])
# print(a*b)


