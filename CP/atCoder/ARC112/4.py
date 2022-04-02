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

n,m,k = imap()
mat = [["."]*(m+1) for i in range(n+1)]
for i in range(k):
    x = input().split()
    mat[int(x[0])][int(x[1])] = x[2]

nxt = [[1,0], [0,1]]

# @lru_cache(None)
def rec(i,j,sgn, ss):
    if i>=n and j>=m:
        # print(ss)
        return 1
    res = 0
    if sgn=="D" or sgn=="X":
        dx,dy = nxt[0]
        x = i+dx
        y = j+dy
        if n>=x>=1 and m>=y>=1:
            res+=rec(x,y,mat[x][y],ss+[sgn])
    if sgn=="R" or sgn=="X":
        dx,dy = nxt[1]
        x = i+dx
        y = j+dy
        if n>=x>=1 and m>=y>=1:
            res+=res+2*rec(x,y,mat[x][y],ss+[sgn])
    if sgn==".":
        # dx,dy = nxt[1]
        # x = i+dx
        # y = j+dy
        # cnt1 = 0
        # if n>=x>=1 and m>=y>=1:
        #     cnt1+=rec(x,y)
        #     # res+=3*cnt
        # dx,dy = nxt[0]
        # x = i+dx
        # y = j+dy
        # cnt2 = 0
        # if n>=x>=1 and m>=y>=1:
        #     cnt2+=rec(x,y)
        #     # res+=3*cnt
        # cnt = cnt1+cnt2
        # res+=cnt+cnt1+cnt2
        # res+= res+rec(i,j,"R",ss+[sgn])
        # res+=res+rec(i,j,"X",ss+[sgn])
        # res+=res+rec(i,j,"D",ss+[sgn])
        res+= res+rec(i,j,"R",ss+[sgn])+rec(i,j,"X",ss+[sgn])+rec(i,j,"D",ss+[sgn])
    # print(i,j,sgn,res)
    return res
print(rec(1,1, mat[1][1],[]))



