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

n,q = imap()
a = ilist()
a.sort()
mp = Counter(a)
b = []
# for i in range(1,2*n+1):
#     if i not in mp:
#         b.append(i)

# 1 2 3 4 5 6 7 8 9 10
#     -   - - -
# 2 3 3 3
c = [a[0]-1]
for i in range(1,n):
    c.append(c[-1]+a[i]-a[i-1]-1)
# print(c)
for i in range(q):
    k = int(input())
    idx = bisect.bisect_left(c, k)

    # if idx>=n or a[idx]>2*k:
    #     idx-=1
    print(idx+k)
