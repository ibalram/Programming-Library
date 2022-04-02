import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------

o = lambda:map(int,input().split())
n,m = o()
p=print
r=range(n)
g = [[] for i in r]
while m:
    x,y = o()
    x-=1
    y-=1
    m-=1
    g[x]+=[y]
    g[y]+=[x]
c = [0]*n
for i in r:
    if c[i]<1:
        c[i] = 1
        q =[i]
        while q:
            s = q.pop()
            for j in g[s]:
                if c[j]<1:
                    c[j] = c[s]%2+1
                    q+=[j]
                if c[j]==c[s]:
                    p("IMPOSSIBLE")
                    exit()
p(*c)

