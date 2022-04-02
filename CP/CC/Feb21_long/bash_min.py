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

n = int(input())
p = ilist()
inp = [['']*n for i in range(n)]

q = deque()
st = set()
src = set()
for i in range(n):
    a = [x-1 for x in imap()]
    for j in range(n):
        inp[i][j] = (a[2*j], a[2*j+1])
        if inp[i][j]!=(i,j):
            x,y = inp[i][j]
            src.add((x,y,(x,y)))
            st.add((x,y))
sym = "DURL"
rSym = "UDLR"
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
q = deque(src)
res = [['']*n for i in range(n)]
while q:
    i,j,pr = q.popleft()
    for idx,[dx,dy] in enumerate(dirs):
        x,y = i+dx,j+dy
        if 0<=x<n and 0<=y<n and inp[x][y]==pr and (x,y) not in st and not res[x][y]:
            res[x][y] = rSym[idx]
            q.append((x,y,pr))
for i in range(n):
    for j in range(n):
        if inp[i][j] != (i, j) or res[i][j]: continue
        for idx,[dx,dy] in enumerate(dirs):
            x,y = i+dx,j+dy
            if 0<=x<n and 0<=y<n and inp[x][y]==(x,y) and not res[x][y]:
                res[i][j] = sym[idx]
                res[x][y] = rSym[idx]
                break
cnt = 0
for i in range(n):
    for j in range(n):
        if res[i][j]:
            cnt+=1
if cnt != n*n:
    print(-1)
    exit()
print(p[0]*n*n)
for i in res:
    print(''.join(i))
