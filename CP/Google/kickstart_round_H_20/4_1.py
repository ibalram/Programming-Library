from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    n,q= imap()
    a = list(input().strip().split())
    # trie = defaultdict(set)
    # for word in a:
    #     for i in range(len(word)):
    #         for j in range(i+1, len(word)):
    #             trie[word[i]].add(word[j])
    #             trie[word[j]].add(word[i])

    def bfs(s,dest):
        q = deque(s)
        dist = {}
        dist[s] = 1
        while q:
            s = q.popleft()
            if s==dest:
                return dist[s]+1
            for i in trie[s]:
                if i not in dist:
                    dist[i] = dist[s]+1
                    q.append(i)
        # print(dist)
        return 1000000000
    res = [-1]*q
    dist = defaultdict(dict)
    def floyedWarshal():
        import string
        st = string.ascii_uppercase
        # print(st)
        for i in st:
            for j in st:
                dist[i][j] = float("inf")
        for word in a:
            for i in range(len(word)):
                for j in range(i, len(word)):
                    dist[word[i]][word[j]] = 1*(i!=j)
                    dist[word[j]][word[i]] = 1*(i!=j)
        for k in st:
            for i in st:
                for j in st:
                    if dist[i][k]==float("inf") or dist[k][j]==float("inf"):
                        continue
                    if dist[i][j]>dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]
    floyedWarshal()
    for k in range(q):
        x,y = imap()
        x-=1
        y-=1
        cur = float("inf")
        for i in a[x]:
            for j in a[y]:
                # print(i,j,bfs(i,j),dist[i][j]+2)
                cur = min(cur, dist[i][j]+2)
        if cur!=float("inf"):
            res[k] = cur

    print("Case #{}:".format(_+1), *res)
