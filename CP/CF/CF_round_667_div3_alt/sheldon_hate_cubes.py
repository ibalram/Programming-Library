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

a = [10,3,3,19,10,8,14,17,12,3,10,4,2,20,5,18,19]
n = len(a)

# a = [3, 2,6]
# n = 3

a = [5,4,2,6]
n = 4
from collections import defaultdict
gr = defaultdict(list)
for i in range(n):
    for j in range(n):
        if i==j:continue
        x = a[i]*a[j]
        if int(x**(1/3))**3 == x:
            gr[i].append(j)
            gr[j].append(i)
res = set()
st = set()
deg = [0]*(n+1)
for i in range(n):
    st.add((len(gr[i]),i))
    deg[i] = len(gr[i])
while st:
    v = st.pop()
    for i in gr[v[1]]:
        if (deg[i], i) not in st: continue
        for j in gr[i]:
            if (deg[j],j) not in st: continue
            st.remove((deg[j],j))
            st.add((deg[j]-1,j))
        st.remove((deg[i],i))
    res.add(v[1])
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
