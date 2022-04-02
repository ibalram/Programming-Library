import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)










import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict, Counter

def solve(N, x, y, edges, s):
    x-=1
    y-=1
    gr = defaultdict(list)
    a = [ord(i)-ord("a") for i in s]
    for u,v in edges:
        gr[u-1].append(v-1)
        gr[v-1].append(u-1)
    counts = defaultdict(Counter)
    def dfs(u,par, y):
        mp = Counter()
        mp[a[u]]+=1
        for i in gr[u]:
            if i==par: continue
            mp+=dfs(i,u, y)
        if u==y: counts[u] = mp.copy()
        return mp
    dfs(x,-1,y)
    dfs(y,-1,x)
    res = [counts[x][i]*counts[y][i] for i in range(26)]
    return res

T = int(input())
for _ in range(T):
    [N,x,y] = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(N-1)]
    s = input()

    out_ = solve(N, x, y, edges, s)
    print(' '.join(map(str, out_)))





# def solve(N, x, y, edges, s):
#     x-=1
#     y-=1
#     gr = defaultdict(list)
#     a = [ord(i)-ord("a") for i in s]
#     for u,v in edges:
#         gr[u-1].append(v-1)
#         gr[v-1].append(u-1)
#     counts = defaultdict(Counter)
#     def dfs(u,par):
#         mp = Counter()
#         mp[a[u]]+=1
#         for i in gr[u]:
#             if i==par: continue
#             mp+=dfs(i,u)
#         print(u,mp)
#         if u in (x,y):
#             counts[u] = mp.copy()
#         return mp
#     final = dfs(x,-1)
#     final[a[x]]+=1
#     res = [0]*26
#     print(final)
#     print(counts)
#     for i in range(26):
#         print(i, final[i], counts[x][i], counts[y][i])
#         res[i] = (final[i]-counts[x][i])*counts[y][i]
#     return res



n = 4
x = 2
y = 4
edges = [(1,2), (2,3), (2, 4)]
s = "abaa"

print(*solve(n,x,y,edges,s))
