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


def solve(a,b,k):
    arr = []
    b = set(b)
    n = len(a)
    for i in range(n):
        if a[i] in b:
            arr.append(i)
    if k>len(arr):
        return -1
    res = float("inf")
    st = Counter()
    l = 0
    for i in range(len(arr)):
        while len(st)>k and l<i:
            st[a[arr[l]]]-=1
            if st[a[arr[l]]]==0:
                del st[a[arr[l]]]
            l+=1
        if len(st)==k:
            res = min(res, arr[i]-arr[l]+1)
        st[a[arr[i]]]+=1
    while (len(st)>k or len(st)==k and st[a[arr[l]]]>1) and l<i:
        st[a[arr[l]]]-=1
        if st[a[arr[l]]]==0:
            del st[a[arr[l]]]
        l+=1
    if len(st)==k:
        res = min(res, arr[i]-arr[l]+1)
    return res if res<float("inf") else -1

n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(a,b,k))


#         # if a[i] in bset:
#         #     st.add(a[i])
#         # if len(st)>=k:
#         #     res = min(res, i-lst+1)
#         # while len(st)>=k:
#         #     if a[lst] in


# a = [4,2,5,23,62]
# b = [4,2,23]
# k = 1

# print(solve(a,b,k))



# for _ in range(int(input())):
#     n = int(input())
#     char = input().strip().split()
#     from collections import defaultdict
#     gr = defaultdict(list)
#     for i in range(n-1):
#         u,v = map(int,input().split())
#         gr[u].append(v)
#         gr[v].append(u)
#     parent = [i for i in range(n+1)]
#     leaf = []
#     def dfs(s, p):
#         global leaf
#         # if len(gr[s])==1:
#         #     leaf.append(s)
#         for i in gr[s]:
#             if i==p: continue
#             parent[i] = s
#             dfs(i,s)

#     # graphs = [defaultdict(list) for i in range(26)]
#     # for i in leaf:
#     #     g = defaultdict(list)
#     #     for i in range
