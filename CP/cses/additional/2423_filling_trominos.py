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

for _ in range(int(input())):
    n,m = imap()
    # AABB
    # ABAB
    # BBAA
    proto = [["A", "A","B", "B"],["A", "B", "A", "B"],["B", "B", "A", "A"]]
    if n%3==0 and m%2==0 or m%3==0 and n%2==0:
        flag = 0
        if m%3==0 and n%2==0:
            proto = list(map(list,zip(*proto)))
            flag = 1
        print("YES")
        # mat = [["A"]*m for i in range(n)]
        mat = [[""]*m for i in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if flag:
                    x = i%4
                    y = j%3
                else:
                    x = i%3
                    y = j%4
                mat[i][j] = proto[x][y]
        for i in mat:
            print("".join(i))
    else:
        print("NO")
