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

n,k = imap()
a = ilist()
mp = Counter(a)
kk = defaultdict(list)
for i in range(n):
    x = mp[i]
    j = 0
    while x>0 and j<k:
        kk[j].append(i)
        x-=1
        j+=1
res = 0
for ls in kk.values():
    i = 0
    while i<len(ls):
        if i!=ls[i]:
            break
        i+=1
    res+=i
print(res)

