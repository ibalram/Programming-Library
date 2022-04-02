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

n = int(int(input()))
a = list(map(int,input().split()))
q = int(input())
gr = defaultdict(list)
sz = [0]*(n+1)
for i in range(n-1):
    gr[a[i]].append(i+2)
    sz[a[i]]+=1

p = [i for i in range(n+1)]
par = [i for i in range(n+1)]
def find(x):
    if x==par[x]: return par[x]
    par[x] = find(par[x])
    return par[x]
def union(x,y):
    par[find(y)] = find(x)
qe = deque([1])
while qe:
    s = qe.popleft()
    if sz[s]==1:
        union(s,gr[s][0])
    for i in gr[s]:
        p[i] = s
        qe.append(i)

prods = [defaultdict(int) for i in range(n+1)]
def dfs(s):
    if sz[s]==0:
        prod = 1
        while s!=1:
            prod*=sz[p[s]]
            s = par[p[s]]
            prods[s][prod]+=1
        return
    for i in gr[s]:
        dfs(i)
        # print(prods[i])
dfs(1)
# print(*par)
# print(*p)

def get(s, val):
    if sz[s] == 0: return 0
    if val%sz[s]: return val
    cnt = 0
    s = par[s]
    for i in prods[s].keys():
        if val%i==0:
            cnt += val//i*prods[s][i]
    return val-cnt
for _ in range(q):
    x, y = map(int,input().split())
    print(get(x,y))

