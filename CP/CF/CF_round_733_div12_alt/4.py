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


from collections import *
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    k = len(set(a))
    st = set()
    b = [0]*(n+1)
    fin = set()
    res = [0]*(n)
    graph = defaultdict(set)
    for i in range(n):
        if a[i] not in st:
            graph[i].add(a[i])
            st.add(a[i])
    for i in range(1,n+1):
        if i not in st:
            fin.add(i)
    newEdges = []
    for i in range(n):
        if i not in graph:
            for j in fin:
                if i+1!=j:
                    fin.remove(j)
                    graph[i].add(j)
                    newEdges.append((i,j))
                    break
    while fin:
        if newEdges:
            x,y = newEdges.pop()
        else:
            k-=1
            x = list(graph.keys())[0]
            y = list(graph[x])[0]
        graph[x].remove(y)
        xx = fin.pop()
        graph[x].add(xx)
        graph[xx-1].add(y)
    ans = 0
    for i in graph.keys():
        res[i] = list(graph[i])[0]
        if a[i]==res[i]:
            ans+=1
    print(ans)
    print(*res)

