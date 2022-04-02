import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

h,w = imap()

mat = [["#"]*(w+2)]
for i in range(h):
    a = list(input().strip())
    mat.append(["#"]+a+["#"])
mat.append(["#"]*(w+2))


# for i in mat:
#     print(*i)
@lru_cache(None)
def rec(i,j):
    if i==h and j==w:
        # print(st)
        return 1
    res = 0
    for dx,dy in [[1,1],[1,0], [0,1]]:
        # for k in range(1,min(h-i+2,w-j+2)+2):
        k = 1
        while i+k*dx<=h and j+k*dy<=w:
            x = i+k*dx
            y = j+k*dy
            # print(i,j,h,w,x,y, mat[x][y])
            # print(k)
            if mat[x][y]==".":
                res+=rec(x,y)#, st+str(x)+" "+str(y)+", ")
                res%=mod
            else:
                break
            k+=1
    return res%mod

print(rec(1,1))
