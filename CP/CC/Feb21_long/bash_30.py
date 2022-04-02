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

import sys
sys.setrecursionlimit(10**7)
from collections import deque
import copy
# n = int(input())
# mat = [[1]*n for i in range(n)]
# inp = [[""]*n for i in range(n)]
# p = list(map(int,input().split()))
# tot = 0
# for i in range(n):
#     ar = list(map(int,input().split()))
#     for j in range(0, 2*n, 2):
#         x,y = ar[j]-1,ar[j+1]-1
#         inp[i][j//2] = [x,y]
#         mat[i][j//2] = ([x,y] if (i,j//2)!=(x,y) else 0)
#         tot+=mat[i][j//2]==0
def main():
    n = int(input())
    p = list(map(int,input().split()))

    res = [[''] * n for _ in range(n)]

    data = [[None] * n for _ in range(n)]


    q = deque()
    st = set()
    cnt = 0
    num_nodes = 0
    for i in range(n):
        row = [int(x) - 1 for x in input().split()]
        # row = a[i]
        for j in range(n):
            data[i][j] = (row[j * 2], row[j * 2 + 1])
            if (i, j) != data[i][j]:
                # q.append((i, j))
                # res[i][j] = 'x'
                x,y = data[i][j]

                st.add((x,y,x,y))
            else:
                num_nodes += 1
    q = deque(list(st))
    # print(q)
    while q:
        cnt += 1
        i, j,pi,pj = q.popleft()
        if 0 <= i + 1 < n and 0 <= j < n and data[i+1][j] == (pi,pj) and not res[i+1][j] and (i+1,j,i+1,j) not in st:
            res[i + 1][j] = 'U'
            q.append((i + 1, j, pi,pj))
        if 0 <= i - 1 < n and 0 <= j < n and data[i-1][j] == (pi,pj) and not res[i-1][j] and (i-1,j,i-1,j) not in st:
            res[i - 1][j] = 'D'
            q.append((i - 1, j, pi,pj))
        if 0 <= i < n and 0 <= j + 1 < n and data[i][j+1] == (pi,pj) and not res[i][j+1] and (i,j+1,i,j+1) not in st:
            res[i][j + 1] = 'L'
            q.append((i, j + 1, pi,pj))
        if 0 <= i < n and 0 <= j - 1 < n and data[i][j-1] == (pi,pj) and not res[i][j-1] and (i,j-1,i,j-1) not in st:
            res[i][j - 1] = 'R'
            q.append((i, j - 1, pi,pj))

    # for e in res:
    #     print(''.join(e))
    # def do(res, one=False, two=False):
    #     rr = list(range(n))
    #     cc = list(range(n))
    #     if one:rr = rr[::-1]
    #     if two:cc = cc[::-1]
    #     for i in rr:
    #         for j in cc:
    #             if data[i][j] == (i, j) and not res[i][j]:
    #                 # cnt += 1
    #                 if 0 <= i + 1 < n and 0 <= j < n and data[i+1][j] == (i+1, j) and not res[i+1][j]:
    #                     res[i][j] = 'D'
    #                     res[i+1][j] = 'U'
    #                 elif 0 <= i - 1 < n and 0 <= j < n and data[i-1][j] == (i-1, j) and not res[i-1][j]:
    #                     res[i][j] = 'U'
    #                     res[i-1][j] = 'D'
    #                 elif 0 <= i < n and 0 <= j + 1 < n and data[i][j+1] == (i, j+1) and not res[i][j+1]:
    #                     res[i][j] = 'R'
    #                     res[i][j+1] = 'L'
    #                 elif 0 <= i < n and 0 <= j - 1 < n and data[i][j-1] == (i, j-1) and not res[i][j-1]:
    #                     res[i][j] = 'L'
    #                     res[i][j-1] = 'R'
    #                 else:
    #                     # print("SD",)
    #                     # for e in res:
    #                     #     print(''.join(e))
    #                     # print("-1")
    #                     # exit()
    #                     return -1
    #     cnt = 0
    #     # for e in res:
    #     #     print(''.join(e))
    #     for i in range(n):
    #         for j in range(n):
    #             if res[i][j]:cnt+=1
    #     if cnt != n * n:
    #         # print("-1")
    #         # exit()
    #         return -1
    #     return res
    # xy = copy.deepcopy(res)
    # res = -1
    # for i,j in [[0,0],[1,1],[1,0],[0,1]]:
    #     x = do(copy.deepcopy(xy), i,j)
    #     if x!=-1:
    #         res = x
    #         break
    from collections import defaultdict
    g = defaultdict(list)
    root = None
    edges = []
    for i in range(n):
        for j in range(n):
            if data[i][j]==(i,j):
                if i+1<n and data[i+1][j]==(i+1,j):
                    g[(i+1,j)].append((i,j))
                    g[(i,j)].append((i+1,j))
                    edges.append(((i,j),(i+1,j)))
                    if not root: root = (i+1,j)
                if j+1<n and data[i][j+1]==(i,j+1):
                    g[(i,j+1)].append((i,j))
                    g[(i,j)].append((i,j+1))
                    edges.append(((i,j),(i,j+1)))
                    if not root: root = (i,j+1)
    # N = len(g)
    # def isBipartite(v):
    #     for u in g[v]:
    #         if (visited[u] == False):
    #             visited[u] = True
    #             color[u] = not color[v]
    #             if (not isBipartite(u)):
    #                 return False
    #         elif (color[u] == color[v]):
    #             return False
    #     return True
    # visited = defaultdict(int)
    # color = defaultdict(int)
    # bipar = True
    # for i in g.keys():
    #     if not visited[i]:
    #         visited[i] = True
    #         bipar = bipar and isBipartite(i)


    # def do(res, one=False, two=False):
    #     rr = list(range(n))
    #     cc = list(range(n))
    #     if one:rr = rr[::-1]
    #     if two:cc = cc[::-1]
    #     for i in rr:
    #         for j in cc:
    #             if data[i][j] == (i, j) and not res[i][j]:
    #                 # cnt += 1
    #                 if 0 <= i + 1 < n and 0 <= j < n and data[i+1][j] == (i+1, j) and not res[i+1][j]:
    #                     res[i][j] = 'D'
    #                     res[i+1][j] = 'U'
    #                 elif 0 <= i - 1 < n and 0 <= j < n and data[i-1][j] == (i-1, j) and not res[i-1][j]:
    #                     res[i][j] = 'U'
    #                     res[i-1][j] = 'D'
    #                 elif 0 <= i < n and 0 <= j + 1 < n and data[i][j+1] == (i, j+1) and not res[i][j+1]:
    #                     res[i][j] = 'R'
    #                     res[i][j+1] = 'L'
    #                 elif 0 <= i < n and 0 <= j - 1 < n and data[i][j-1] == (i, j-1) and not res[i][j-1]:
    #                     res[i][j] = 'L'
    #                     res[i][j-1] = 'R'
    #                 else:
    #                     # print("SD",)
    #                     # for e in res:
    #                     #     print(''.join(e))
    #                     # print("-1")
    #                     # exit()
    #                     return -1
    #     cnt = 0
    #     # for e in res:
    #     #     print(''.join(e))
    #     for i in range(n):
    #         for j in range(n):
    #             if res[i][j]:cnt+=1
    #     if cnt != n * n:
    #         # print("-1")
    #         # exit()
    #         return -1
    #     return res
    # xy = copy.deepcopy(res)
    # res = -1
    # for i,j in [[0,0],[1,1],[1,0],[0,1]]:
    #     x = do(copy.deepcopy(xy), i,j)
    #     if x!=-1:
    #         res = x
    #         break
    # if res==-1:
    #     print(-1)
    #     exit()
    # res = xy

    def is_bipartite(graph):
        n = len(graph)
        color = defaultdict(int)
        for start in graph.keys():
            if start not in color: #color[start] == -1:
                color[start] = 0
                stack = [start]
                while stack:
                    parent = stack.pop()
                    for child in graph[parent]:
                        if child not in color:#[child] == -1:
                            color[child] = 1 - color[parent]
                            stack.append(child)
                        elif color[parent] == color[child]:
                            return False, color
        return True, color
    is_bipar, color = is_bipartite(g)
    if not is_bipar:
        print(-1)
        exit()
    adj = defaultdict(dict)
    N = sum(v==1 for v in color.values())
    M = sum(v==0 for v in color.values())
    zeroColor = []
    for i,v in color.items():
        if v: adj[i] = defaultdict(int)
        else: zeroColor.append(i)
    fail = 0
    for w in edges:
        v,u = sorted(w, key=lambda x: color[x])
        if color[u]==color[v]:
            fail = 1
            break
        adj[u][v] = 1
    if fail:
        print(-1)
        exit()
    def bpm(u, matchR, seen):
        for v in zeroColor:
            if adj[u][v] and not seen[v]:
                seen[v] = True
                '''If job 'v' is not assigned to an applicant OR previously
                assigned applicant for job v (which is matchR[v])
                has an alternate job available.
                Since v is marked as visited in the
                above line, matchR[v]  in the following
                recursive call will not get job 'v' again'''
                if matchR[v] == (-1,-1) or bpm(matchR[v],matchR, seen):
                    matchR[v] = u
                    return True
        return False
    def maxBPM(N,M):
        '''An array to keep track of the applicants assigned to jobs.
           The value of matchR[i] is the applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = defaultdict(lambda :(-1,-1))#[-1] * M
        result = 0
        for i in adj.keys():
            seen = defaultdict(bool)
            if bpm(i, matchR, seen):
                result += 1
        res_edges = []
        for i,v in matchR.items():
            if i!=(-1,-1) and v !=(-1,-1) and i!=v:
                res_edges.append((i,v))
        return result, res_edges
    result, res_edges = maxBPM(N,M)
    # print(result)
    # print(res_edges)
    if len(color)%2 or num_nodes//2!=result:
        print(-1)
        exit()
    for (i,j),(x,y) in res_edges:
        # if x==i+1:
        if (x,y)==(i+1,j):
            res[i][j] = 'D'
            res[i+1][j] = 'U'
        elif (x,y)==(i-1,j): #x==i-1:
            res[i][j] = 'U'
            res[i-1][j] = 'D'
        elif (x,y)==(i,j+1): #y == j+1:
            res[i][j] = 'R'
            res[i][j+1] = 'L'
        elif (x,y)==(i,j-1): #y == j-1:
            res[i][j] = 'L'
            res[i][j-1] = 'R'
    cnt = 0
    for i in res:
        for j in i:
            cnt+= j in "UDRL"
    if cnt!=n*n:
        print(-1)
        exit()
    if not check(data,res,n):
        print(-1)
        exit()
    print(n*n*p[0])
    for e in res:
        print(''.join(e))

def check(data, mat, n):
    dd = [[1,0],[0,1],[-1,0],[0,-1]]
    ii = "DRUL"
    def dfs(i,j, vis):
        dx,dy = dd[ii.index(mat[i][j])]
        x,y = i+dx,j+dy
        if 0<=x<n and 0<=y<n:
            if (x,y) not in vis:
                vis[(x,y)] = 1
                return dfs(x,y,vis)
            else:
                return (x,y)
        return (-1,-1)
    for i in range(n):
        for j in range(n):
            vis = {}
            vis[(i,j)]=1
            if dfs(i,j, vis)!=data[i][j]:
                return False
    return True
main()

