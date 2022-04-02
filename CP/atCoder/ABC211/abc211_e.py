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
k = int(input())

grid = []
for i in range(n):
    grid.append(list(input().strip()))

tran =[(1,0),(-1,0),(0,1),(0,-1)]
print(64*(3**6))

# def dfs(i, j):
#     for dx,dy in tran:
#         x = i+dx
#         y = j+dy
#         val = x*8+y
#         if 0<=x<n and 0<=y<n and val not in st:
#             st[val] = st[(i*8+j)]+1
#             dfs(x,y)
# for i in range(n):
#     for j in range(n):
#         st ={(i*8+j):1}
#         dfs(i,j)
#         cntr = Counter(st.value())









