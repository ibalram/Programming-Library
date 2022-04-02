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

from math import atan

N,D,H = imap()
d = []
h = []
minRes = float("inf")
mAngle = float("inf")
for i in range(N):
    a,b = imap()
    d.append(a)
    h.append(b)
rn = sorted(list(range(N)), key = lambda x: d[x], reverse = True)
# for i in rn[::-1]:
#     angle = (H-h[i])/(D-d[i])
#     if angle<=mAngle:
#         minRes = min(minRes, H-(D/(D-d[i])*(H-h[i])))
#         mAngle = angle

for i in range(N):
    angle = (H-h[i])/(D-d[i])
    f = 1
    for j in range(N):
        if i==j:continue
        if (H-h[j])/(D-d[j])<angle:
            f = 0
            break
    if f:
        minRes = min(minRes, H-(D/(D-d[i])*(H-h[i])))
print(minRes if minRes>0 else 0)
