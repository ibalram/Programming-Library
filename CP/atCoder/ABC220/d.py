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
a = []
mp = defaultdict(int)
for i in range(n):
    x,y = imap()
    mp[x]+=1
    mp[x+y]-=1
keys = list(sorted(mp.keys()))
prev = mp[keys[0]]
res = [0]*(n+1)
for i in range(1,len(keys)):
    mp[keys[i]]+=mp[keys[i-1]]
    length = keys[i]-keys[i-1]
    res[mp[keys[i-1]]]+=length
# print(sorted(mp.items()))
print(*res[1:])




