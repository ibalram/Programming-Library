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


from heapq import heapify, heappop, heappush
n = int(input())

a = list(map(int,input().split()))

mat = [[0]*(i+1) for i in range(n)]
for i in range(n):
    mat[i][i] = a[i]

dr = [(-1,0),(0,-1),(1,0),(0,1)]
def safe(i,j):
    return 0<=i<n and 0<=j<=i and mat[i][j]==0
res = 0
for i in range(n):
    cnt = mat[i][i]-1
    q = [(i,i)]
    backup = []
    while cnt>0:
        if not q:
            fnd = 0
            # print(i)
            for j in range(len(backup)-1,-1,-1):
                if safe(backup[j][0],backup[j][1]):
                    s = backup[j]
                    mat[s[0]][s[1]] = mat[i][i]
                    cnt-=1
                    backup = backup[:j]
                    fnd = 1
                    break
            if not fnd:
                # for i in mat:
                #     print(*i)
                break
        else:
            s = q.pop()
        dn = 1
        for dx,dy in dr:
            x,y = s[0]+dx,s[1]+dy
            if dn and safe(x,y) and cnt>0:
                cnt-=1
                mat[x][y] = mat[i][i]
                q.append((x,y))
                dn = 0
                # break
            elif dn==0 and safe(x,y):
                backup.append((x,y))
    if cnt:
        res = -1
if res==-1:
    print(-1)
else:
    for i in mat:
        print(*i)

# q = []
# for i in range(n):
#     mat[i][i] = a[i]
#     sf = []
#     for dx,dy in dr:
#         x = i+dx
#         y = i+dy
#         if safe(x,y):
#             sf.append((x,y))
#     for k in sf:
#         heappush(q,(len(sf), a[i], sf))
# while q:
#     ln,num,ls = heappop(q)
#     used = []
#     nls = []
#     for i in len(ls):
#         if safe(i):
#             mat[ls[i][0]][ls[i][1]] = num
#             x,y = ls.pop(i)
#             for dx,dy in dr:
#                 x = x+dx
#                 y = y+dy
#                 if safe(x,y):
#                     nls.append((x,y))
#             heappush(q,(len(nls), num, ))
#             break
#     for



