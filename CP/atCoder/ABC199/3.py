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

n = int(input())
s = list(input().strip())
one = s[:n]
two = s[n:]
# print(one,two)
q = int(input())

for i in range(q):
    t,a,b = imap()
    a-=1
    b-=1
    ai = []
    bi = []
    if t==1:
        if a>=n:
            bi.append(a%n)
        else:
            ai.append(a)
        if b>=n:
            bi.append(b%n)
        else:
            ai.append(b)
        if len(ai)==2:
            a,b = ai
            one[a],one[b] = one[b],one[a]
        elif len(bi)==2:
            a,b = bi
            two[a],two[b] = two[b],two[a]
        else:
            a = ai[0]
            b = bi[0]
            # print(a,b, one,two)
            one[a],two[b] = two[b],one[a]
    else:
        one,two = two,one
print("".join(one+two))




