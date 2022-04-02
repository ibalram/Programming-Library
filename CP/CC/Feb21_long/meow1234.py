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

n,t = map(int,input().split())
from collections import deque
mod = 10**9+7
a = []
mxn = 0
mxm = 0
for i in range(n):
    x,y = map(int,input().split())
    x-=1
    y-=1
    mxn = max(x+1,mxn)
    mxm = max(y+1,mxm)
    a.append((x,y))
a = list(set(a))
n = len(a)
sz = mxn*mxm

res = float("inf")
count = 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(1,1<<sz):
    bits = [0]*(sz)
    for j in range(sz):
        bits[j] =  i>>j&1
    sm = sum(bits)
    if sm<n:
        continue
    f = 1
    mat = []
    for k in range(0,sz,mxm):
        mat.append(bits[k:k+mxm])
    for x,y in a:
        # if not bits[x*mxm+y]:
        if not mat[x][y]:
            f = 0
            break
    if f==0:
        continue
    st = (-1,-1)
    for k in range(mxn):
        for j in range(mxm):
            if mat[k][j]:
                st = (k,j)
                break
        if st!=(-1,-1):
            break

    def bfs(st, fl=False):
        q = deque()
        q.append(st)
        vis = {st:0}
        # x,y = st//mxm,st%mxm
        x,y = st
        f = 1
        cnt = 0
        while q:
            cnt+=1
            s = q.popleft()
            ii,jj = s
            for k in range(4):
                xx = ii+dx[k]
                yy = jj+dy[k]
                # z = xx*mxm+yy
                z = (xx,yy)
                if 0<=xx<mxn and 0<=yy<mxm and mat[xx][yy] and z not in vis:
                    if abs(yy-y)+abs(xx-x)!=vis[s]+1:
                        f = 0
                        break
                    vis[z] = vis[s]+1
                    q.append(z)
            if f==0:
                break
        # if fl:
        #     return f and cnt==sm
        # else:
        #     if not (f and cnt==sm): return -1
        #     sz,nn =0,-1
        #     for i,v in vis.items():
        #         if v>sz:
        #             nn = i
        #     return nn
        if f==0:return -1
        for i in a:
            for j in a:
                if i==j: continue
                if i in vis and j in vis and abs(vis[i]-vis[j])!=abs(i[0]-j[0])+abs(i[1]-j[1]):
                    f = 0
                    break
            if f==0:
                break
        if cnt==sm==10:print(vis)
        if f==0: return -1
        else: return cnt
    nn = bfs(st)
    if nn==sm:#!=-1:# and bfs(nn,1):#all(bfs(i,1) for i in nn):

        if sm<res:
            res = sm
            count = 1
        elif sm==res:
            count+=1
        # if sm==10:
        #     for k in range(0,sz,mxm):
        #         print(*bits[k:k+mxm])
        #     print()
if t:
    print(res,count)
else:
    print(res)

