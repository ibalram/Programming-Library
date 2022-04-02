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
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(input().strip()))
    res = 0
    for cnt in range(2,0,-1):
        for i in range(n):
            for j in range(n):
                if mat[i][j]!="X": continue
                count1 = 0
                count1+=i>0 and mat[i-1][j]=="X" and i<n-1 and mat[i+1][j]=="X"
                count1+=j>0 and mat[i][j-1]=="X" and j<n-1 and mat[i][j+1]=="X"
                if count1==cnt:
                    mat[i][j] = "O"
                    res+=1
    print(res)
    for i in mat:
        print("".join(i))
