import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("xs_and_os_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

vowel = "AEIOU"

for _ in range(int(input())):
    res = float("inf")
    n = int(input())
    grid = [input().strip() for i in range(n)]
    rowX = [0]*(n)
    colX = [0]*(n)
    row = defaultdict(set)
    col = defaultdict(set)
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="X":
                rowX[i]+=1
                colX[j]+=1
            if grid[i][j]==".":
                row[i].add((i,j))
                col[j].add((i,j))
    st = set()
    mn = float("inf")
    for i in range(n):
        if rowX[i]+len(row[i])==n:
            if len(row[i])<mn:
                cnt = set([tuple(sorted(row[i]))])
            elif len(row[i])==mn:
                cnt.add(tuple(sorted(row[i])))
            mn = min(mn,len(row[i]))
        if colX[i]+len(col[i])==n:
            if len(col[i])<mn:
                cnt = set([tuple(sorted(col[i]))])
            elif len(col[i])==mn:
                cnt.add(tuple(sorted(col[i])))
            mn = min(mn,len(col[i]))
    if mn==float("inf"):
        print("Case #{}:".format(_+1), "Impossible")
    else:
        print("Case #{}: {} {}".format(_+1, mn,len(cnt)))

