import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------

n = 4
a = [[1,2,2],[2,4,1], [4,3,10],[3,1,1]]
c = [[1,1]]

from collections import defaultdict
gr = defaultdict(list)
for i in range(n):
    x,y,w = a[i]
    gr[x].append((w,y))
    gr[y].append((w,x))
res = set()
dist = [-float("inf")]*(n+1)
from heapq import heapify, heappop as pp, heappush as pus
# for i in ran
q = []
vis = {}
for i,j in c:
    q.append((-j,i))
    res.add(i)
    vis[i] = 1
    dist[i] = j
while q:
    wt,node = pp(q)
    wt = -wt
    # print(node)
    for w,i in gr[node]:
        nw = wt-w
        # print(node,i,w,wt)
        # if nw>0: res.add(i)
        if nw>dist[i]:
            pus(q,(-nw,i))
            dist[i] = nw
for i in dist:
    if i>=0:res.add(i)
print(len(res))



# print(res)

"""
 TreeSet<Integer> MIS(int n) {
    TreeSet<Integer> is = new TreeSet<>();
    TreeSet<Pair> set = new TreeSet<>();
    int deg[] = new int[n + 1];
    for (int i = 0; i < n; ++i) {
        set.add(new Pair(graph[i].size(), i));
        deg[i] = graph[i].size();
    }
    while (!set.isEmpty()) {
        Pair v = set.pollFirst();
        for (int e : graph[v.y]) {
            if (set.contains(new Pair(deg[e], e))) {
                for (int f : graph[e]) {
                    if (set.contains(new Pair(deg[f], f))) {
                        set.remove(new Pair(deg[f], f));
                        set.add(new Pair(--deg[f], f));
                    }
                }
                set.remove(new Pair(deg[e], e));
            }
        }
        is.add(v.y);
    }
    return is;
}
"""
