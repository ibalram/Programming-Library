import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("consistency_chapter_2_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

vowel = "AEIOU"

for _ in range(int(input())):
    res = float("inf")
    s = [ord(i)-ord("A") for i in input().strip()]
    n = len(s)
    k = int(input())
    dist = [[float("inf")]*(26) for i in range(26)]
    for i in range(26): dist[i][i] = 0
    for i in range(k):
        u,v = [ord(i)-ord("A") for i in input().strip()]
        dist[u][v] = 1
    for k in range(26):
        for i in range(26):
            for j in range(26):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    for cand in range(26):
        f = 1
        ans = 0
        for i in s:
            if dist[i][cand]==float("inf"):
                f = 0
                break
            ans+=dist[i][cand]
        if f:
            res = min(res, ans)
    if res==float("inf"): res = -1
    print("Case #{}: {}".format(_+1, res))

