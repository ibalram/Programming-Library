import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("gold_mine_chapter_1_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**4)
mod = int(1e9+7)


for _ in range(int(input())):
    res = float("inf")
    n = int(input())
    c = ilist()
    gr = defaultdict(set)
    for i in range(n-1):
        u,v = imap()
        u-=1
        v-=1
        gr[u].add(v)
        gr[v].add(u)

    res = 0
    mxPath = []
    def dfs(s, par, sm, path):
        global res, mxPath
        for i in gr[s]:
            if i==par: continue
            path.append(i)
            dfs(i,s,sm+c[i], path)
            path.pop()
        else:
            if res<sm:
                res = sm
                mxPath = path[:]
    dfs(0,-1, c[0], [0])
    # print(mxPath)
    for i in range(1,len(mxPath)):
        gr[mxPath[i-1]].remove(mxPath[i])
        gr[mxPath[i]].remove(mxPath[i-1])
    ans = res
    res = 0
    mxPath =[]
    dfs(0,-1,0,[0])
    ans+=res
    print("Case #{}: {}".format(_+1, ans))

