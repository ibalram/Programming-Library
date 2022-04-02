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
a = ilist()
mp = Counter(a)
res = 0
aa = list(mp.keys())
for i in range(len(aa)):
    for j in range(i+1,len(aa)):
        res+= pow(abs(aa[i]-aa[j]),2)*(mp[aa[i]]*mp[aa[j]])
print(res)
