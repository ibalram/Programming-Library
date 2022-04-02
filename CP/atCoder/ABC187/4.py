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
smb = 0
for i in range(n):
    x = ilist()
    a.append([sum(x)+x[0],x[0]])
    smb+=a[i][1]
a.sort(reverse=True)
cnt = 0
res = n
# print(a)
for i in range(n):
    cnt+=a[i][0]-a[i][1]
    smb-=a[i][1]
    if smb<cnt:
        # print(smb,cnt)
        res = i+1
        break
print(res)
