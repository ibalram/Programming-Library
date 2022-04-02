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


def min_cost_max_flow(graph,a_group,b_group):
    # Function to check if it is possible to have a flow from the src to sink
    def search(src, sink):
        # Initialise found[] to false
        # found = [False for _ in range(N)]
        found = defaultdict(lambda :False)
        # Initialise the dist[] to INF
        # dist = [INF for _ in range(N + 1)]
        dist = defaultdict(lambda : INF)
        # Distance from the source node
        dist[src] = 0

        for _ in len(all_nodes):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            # for u, v, w in self.graph:
            for u in cost:
                for v in cost[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w


        # Iterate untill src reaches N
        # while (src != N):
        # while src!=t:
        #     # best = N
        #     best = t
        #     found[src] = True
        #     # for k in range(N):
        #     for k in all_nodes:
        #         # If already found
        #         if (found[k]):
        #             continue
        #         # Evaluate while flow is still in supply
        #         if (flow[k][src] != 0):
        #             # if src not in flow[k]:
        #             # Obtain the total value
        #             val = (dist[src] + pi[src] - pi[k] - cost[k].get(src,0))
        #             # If dist[k] is > minimum value
        #             if (dist[k] > val):
        #                 # Update
        #                 dist[k] = val
        #                 dad[k] = src
        #         if (flow[src][k] < cap[src][k]):
        #             val = (dist[src] + pi[src] - pi[k] + cost[src][k])
        #             # If dist[k] is > minimum value
        #             if (dist[k] > val):
        #                 # Update
        #                 dist[k] = val
        #                 dad[k] = src
        #         print(dist[k],dist[best],k,best)
        #         if (dist[k] < dist[best]):
        #             best = k
        #     # Update src to best for next iteration
        #     src = best
        # # for k in range(N):
        for k in all_nodes:
            pi[k] = min(pi[k] + dist[k], INF)
        # Return the value obtained at sink
        return found[sink]
    # Function to obtain the maximum Flow
    def getMaxFlow(capi, costi, src, sink):
        global cap, cost, found, dist, pi, N, flow, dad
        cap = capi
        cost = costi
        N = len(capi)
        found = defaultdict(lambda :False)
        flow = defaultdict(Counter)
        dist = defaultdict(lambda :INF)
        dad = defaultdict(lambda :(-1,-1))
        pi = defaultdict(lambda :(-1,-1))
        totflow = 0
        totcost = 0
        # If a path exist from src to sink
        while (search(src, sink)):
            # Set the default amount
            amt = INF
            x = sink
            while x != src:
                # print(cap[dad[x]][x])
                amt = min(amt, flow[x][dad[x]] if (flow[x][dad[x]] != 0) else cap[dad[x]][x] - flow[dad[x]][x])
                x = dad[x]
            x = sink
            while x != src:
                if (flow[x][dad[x]] != 0):
                    flow[x][dad[x]] -= amt
                    totcost -= amt * cost[x][dad[x]]
                else:
                    flow[dad[x]][x] += amt
                    totcost += amt * cost[dad[x]][x]
                x = dad[x]
            totflow += amt
        # Return pair total cost and sink
        return [totflow, totcost]

    from sys import maxsize
    from typing import List
    # Stores the found edges
    found = []
    # Stores the number of nodes
    N = 0
    # Stores the capacity of each edge
    # cap = []
    # flow = []
    # # Stores the cost per unit flow of each edge
    # cost = []
    # # Stores the distance from each node and picked edges for each node
    # dad = []
    # dist = []
    und = defaultdict(lambda :False)
    flow = defaultdict(Counter)
    dist = defaultdict(lambda :INF)
    dad = defaultdict(lambda :(-1,-1))
    pi = defaultdict(lambda :0)
    # pi = []
    INF = maxsize // 2 - 1
    # Driver Code
    # s = (-1,-1)
    # t = (-2,-2)
    s = (51,51)
    t = (52,52)
    cap = copy.deepcopy(graph)
    cost = copy.deepcopy(graph)
    for i in cap:
        for j in cap[i]:
            if cap[i][j]:
                cap[i][j] = 1
    for i in a_group:
        cap[s][i] = 1
        cost[s][i] = 0
    for j in b_group:
        cap[j][t] = 1
        cost[j][t] = 0
    all_nodes = list(set(a_group+b_group+[s,t]))
    # for i in all_nodes:
    #     flow[i] = defaultdict(int)


    # cap = [ [ 0, 3, 1, 0, 3 ],
    #         [ 0, 0, 2, 0, 0 ],
    #         [ 0, 0, 0, 1, 6 ],
    #         [ 0, 0, 0, 0, 2 ],
    #         [ 0, 0, 0, 0, 0 ] ]
    # cost = [ [ 0, 1, 0, 0, 2 ],
    #          [ 0, 0, 0, 3, 0 ],
    #          [ 0, 0, 0, 0, 0 ],
    #          [ 0, 0, 0, 0, 1 ],
    #          [ 0, 0, 0, 0, 0 ] ]
    ret = getMaxFlow(cap, cost, s, t)
    print("{} {}".format(ret[0], ret[1]))


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
                x,y = data[i][j]
                st.add((x,y,x,y))
            else:
                num_nodes += 1
    q = deque(list(st))
    # print(q)
    cost1 = 0
    while q:
        cnt += 1
        i, j,pi,pj = q.popleft()
        if 0 <= i + 1 < n and 0 <= j < n and data[i+1][j] == (pi,pj) and not res[i+1][j] and (i+1,j,i+1,j) not in st:
            res[i + 1][j] = 'U'
            cost1+=p[0]
            q.append((i + 1, j, pi,pj))
        if 0 <= i - 1 < n and 0 <= j < n and data[i-1][j] == (pi,pj) and not res[i-1][j] and (i-1,j,i-1,j) not in st:
            res[i - 1][j] = 'D'
            cost1+=p[2]
            q.append((i - 1, j, pi,pj))
        if 0 <= i < n and 0 <= j + 1 < n and data[i][j+1] == (pi,pj) and not res[i][j+1] and (i,j+1,i,j+1) not in st:
            res[i][j + 1] = 'L'
            cost1+=p[1]
            q.append((i, j + 1, pi,pj))
        if 0 <= i < n and 0 <= j - 1 < n and data[i][j-1] == (pi,pj) and not res[i][j-1] and (i,j-1,i,j-1) not in st:
            res[i][j - 1] = 'R'
            cost1+=p[3]
            q.append((i, j - 1, pi,pj))
    from collections import defaultdict
    g = defaultdict(list)
    root = None
    edges = []
    graph = defaultdict(Counter)

    edges = []
    for i in range(n):
        for j in range(n):
            if data[i][j]==(i,j):
                if i+1<n and data[i+1][j]==(i+1,j):
                    # g[(i+1,j)].append((i,j,p[0]))
                    # g[(i,j)].append((i+1,j,p[2]))
                    graph[(i+1,j,1)][(i,j,2)] = p[0]
                    graph[(i,j,1)][(i+1,j,2)] = p[2]
                    edges.append(((i,j,1),(i+1,j,2),p[2]))
                    edges.append(((i+1,j,1),(i,j,2),p[0]))
                    if not root: root = (i+1,j)
                if j+1<n and data[i][j+1]==(i,j+1):
                    # g[(i,j+1)].append((i,j,p[1]))
                    # g[(i,j)].append((i,j+1,p[3]))
                    graph[(i,j+1,1)][(i,j,2)] = p[1]
                    graph[(i,j,1)][(i,j+1,2)] = p[3]
                    edges.append(((i,j,1),(i,j+1,2),p[3]))
                    edges.append(((i,j+1,1),(i,j,2),p[1]))
                    if not root: root = (i,j+1)
    a_group = set()
    b_group = set()
    for i in graph:
        a_group.add(i)
        for j in graph[i]:
            b_group.add(j)
    a_group = list(a_group)
    b_group = list(b_group)
    all_nodes = a_group[:]
    # min_cost_max_flow(graph, a_group,b_group)
    def mincost(edges,a_group,b_group):
        inf = 1<<30
        adj = defaultdict(list)
        cost = defaultdict(Counter)
        cap = defaultdict(Counter)
        s = (51,51)
        t = (52,52)
        for i in a_group:
            edges.append((s,i,0))
        for i in b_group:
            edges.append((i,t,0))
        for u,v,w in edges:
            adj[u].append(v)
            adj[v].append(u)
            cost[u][v] = w
            cost[v][u] = -w
            cap[u][v] = 1

        flow = 0
        cst =0
        d,p = defaultdict(lambda:inf),defaultdict(lambda:(-1,-1))
        K = len(a_group)

        def shortest_paths(s,d,p):
            d = defaultdict(lambda:inf)
            p = defaultdict(lambda:(-1,-1))
            d[s] = 0
            inq = defaultdict(bool)
            q = deque()
            q.append(s)
            while q:
                u = q.popleft()
                inq[u] = False
                for v in adj[u]:
                    # print(cap[u][v],d[v],d[u]+cost[u][v])
                    if cap[u][v]>0 and d[v]>d[u]+cost[u][v]:
                        d[v] = d[u]+cost[u][v]
                        p[v] = u
                        if not inq[v]:
                            inq[v] = True
                            q.append(v)
            return d,p
        matches = []
        while flow<K:
            d,p = shortest_paths(s,d,p)
            if d[t]==inf:
                break
            f = K-flow
            cur = t
            while cur!=s:
                f = min(f,cap[p[cur]][cur])
                cur = p[cur]
            flow+=f
            cst+=f*d[t]
            cur = t
            pth = set()
            pathh = []
            while cur!=s:
                cap[p[cur]][cur]-=f
                cap[cur][p[cur]]+=f
                pathh.append([p[cur],cur])
                # if cur not in [s,t] and p[cur] not in [s,t] and cap[p[cur]][cur]==0:
                #     pth.add(cur)
                #     # if f and p[cur][2]==1 and cur[2]==2:
                #     #     matches.append((p[cur],cur))
                #     #     print(*matches[-1])
                cur = p[cur]
            if pathh:
                # matches.append(sorted(pathh,key=lambda x:x[2]))
                matches.append(pathh[::-1])
        # if flow<K:
        #     return -1
        return cst,matches
    cost,matches = mincost(edges,a_group,b_group)
    print(*matches,cost+cost1,sep="\n")
    print(len(matches))
    matches = [i[1] for i in matches][:10]
    cost3 = 0
    for (i,j,q),(x,y,r) in matches:
        # if x==i+1:
        if (x,y)==(i+1,j):
            res[i][j] = 'D'
            cost3+=p[2]
        elif (x,y)==(i-1,j): #x==i-1:
            res[i][j] = 'U'
            cost3+=p[0]
        elif (x,y)==(i,j+1): #y == j+1:
            res[i][j] = 'R'
            cost3+=p[3]
        elif (x,y)==(i,j-1): #y == j-1:
            res[i][j] = 'L'
            cost3+=p[1]
    print(96-cost3-cost1)
    for e in res:
        print(''.join(e))
    if not check(data,res,n) and solve2(data,edges,res,a_group,b_group,all_nodes):
        print(-1)
        exit()
    # print(n*n*p[0])
    print(cost+cost1)
    for e in res:
        print(''.join(e))

    # print(cost,cost+cost1)
    # def is_bipartite(graph):
    #     n = len(graph)
    #     color = defaultdict(int)
    #     for start in graph.keys():
    #         if start not in color: #color[start] == -1:
    #             color[start] = 0
    #             stack = [start]
    #             while stack:
    #                 parent = stack.pop()
    #                 for child in graph[parent]:
    #                     if child not in color:#[child] == -1:
    #                         color[child] = 1 - color[parent]
    #                         stack.append(child)
    #                     elif color[parent] == color[child]:
    #                         return False, color
    #     return True, color
    # is_bipar, color = is_bipartite(g)
    # if not is_bipar:
    #     print(-1)
    #     exit()

    # adj = defaultdict(dict)
    # N = sum(v==1 for v in color.values())
    # M = sum(v==0 for v in color.values())
    # zeroColor = []
    # for i,v in color.items():
    #     if v: adj[i] = defaultdict(int)
    #     else: zeroColor.append(i)
    # fail = 0
    # for w in edges:
    #     v,u = sorted(w, key=lambda x: color[x])
    #     if color[u]==color[v]:
    #         fail = 1
    #         break
    #     adj[u][v] = 1
    # if fail:
    #     print(-1)
    #     exit()
    # def bpm(u, matchR, seen):
    #     for v in zeroColor:
    #         if adj[u][v] and not seen[v]:
    #             seen[v] = True
    #             '''If job 'v' is not assigned to an applicant OR previously
    #             assigned applicant for job v (which is matchR[v])
    #             has an alternate job available.
    #             Since v is marked as visited in the
    #             above line, matchR[v]  in the following
    #             recursive call will not get job 'v' again'''
    #             if matchR[v] == (-1,-1) or bpm(matchR[v],matchR, seen):
    #                 matchR[v] = u
    #                 return True
    #     return False
    # def maxBPM(N,M):
    #     '''An array to keep track of the applicants assigned to jobs.
    #        The value of matchR[i] is the applicant number assigned to job i,
    #        the value -1 indicates nobody is assigned.'''
    #     matchR = defaultdict(lambda :(-1,-1))#[-1] * M
    #     result = 0
    #     for i in adj.keys():
    #         seen = defaultdict(bool)
    #         if bpm(i, matchR, seen):
    #             result += 1
    #     res_edges = []
    #     for i,v in matchR.items():
    #         if i!=(-1,-1) and v !=(-1,-1) and i!=v:
    #             res_edges.append((i,v))
    #     return result, res_edges
    # result, res_edges = maxBPM(N,M)
    # # print(result)
    # # print(res_edges)
    # if len(color)%2 or num_nodes//2!=result:
    #     print(-1)
    #     exit()
    # for (i,j),(x,y) in res_edges:
    #     # if x==i+1:
    #     if (x,y)==(i+1,j):
    #         res[i][j] = 'D'
    #         res[i+1][j] = 'U'
    #     elif (x,y)==(i-1,j): #x==i-1:
    #         res[i][j] = 'U'
    #         res[i-1][j] = 'D'
    #     elif (x,y)==(i,j+1): #y == j+1:
    #         res[i][j] = 'R'
    #         res[i][j+1] = 'L'
    #     elif (x,y)==(i,j-1): #y == j-1:
    #         res[i][j] = 'L'
    #         res[i][j-1] = 'R'
    # cnt = 0
    # for i in res:
    #     for j in i:
    #         cnt+= j in "UDRL"
    # if cnt!=n*n:
    #     print(-1)
    #     exit()
    # if not check(data,res,n):
    #     print(-1)
    #     exit()
    # print(n*n*p[0])
    # for e in res:
    #     print(''.join(e))

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

def solve2(data, edges, res,a_group,b_group,all_nodes):
    inf = 1<<30
    # a_group.remove((51,51))
    # b_group.remove((52,52))
    n = len(a_group)
    # for i in range(len(a_group)):
    #     aa_group = {}
    adj = defaultdict(list)
    cost = defaultdict(Counter)
    # s = (51,51)
    # t = (52,52)
    # for i in a_group:
    #     edges.append((s,i,0))
    # for i in b_group:
    #     edges.append((i,t,0))
    Lmate = defaultdict(lambda :(-1,-1))
    Rmate = defaultdict(lambda :(-1,-1))
    for u,v,w in edges:
        if u in [(51,51),(52,52)] or v in [(51,51),(52,52)]:continue
        adj[a_group.index(u)].append(b_group.index(v))
        adj[b_group.index(v)].append(a_group.index(u))
        # Lmate[a_group.index(u)] = b_group.index(v)
        # Rmate[v] = u
        cost[a_group.index(u)][b_group.index(v)] = w
        cost[b_group.index(v)][a_group.index(u)] = w

    def mincostmatch(cost,Lmate, Rmate):
        n = len(cost);
        u = defaultdict(int)
        v = defaultdict(int)
        for i in range(n):
            u[i] = cost[i][0]
            for j in range(1,n):
                u[i] = min(u[i], cost[i][j])
        for j in range(n):
            v[i] = cost[i][b_group[0]]
            for j in range(1,n):
                v[j] = min(v[j], cost[i][j]-u[i])
        # construct primal solution satisfying complementary slackness
        Lmate = defaultdict(lambda :-1)
        Rmate = defaultdict(lambda :-1)
        mated = 0;
        from math import fabs
        for i in range(n):
            for j in range(n):
              if (Rmate[j] != -1): continue
              if (fabs(cost[i][j] - u[i] - v[j]) < 1e-10):
                Lmate[i] = j;
                Rmate[j] = i;
                mated+=1;
                break;
        dist = defaultdict(int)
        dad = defaultdict(int)
        seen = defaultdict(int)

        # // repeat until primal solution is feasible
        while (mated < n):
            # // find an unmatched left node
            s = 0;
            while (Lmate[s] != -1): s+=1;
            # // initialize Dijkstra
            # fill(dad.begin(), dad.end(), -1);
            dad = defaultdict(lambda :-1)
            # fill(seen.begin(), seen.end(), 0);
            seen = defaultdict(int)
            for k in range(n):
                dist[k] = cost[s][k] - u[s] - v[k];
            j = 0;
            while (True) :
                # // find closest
                j = -1;
                for k in range(n):
                    if (seen[k]): continue;
                    if (j == -1 or dist[k] < dist[j]): j = k;

                seen[j] = 1;

                # // termination condition
                if (Rmate[j] == -1): break;

                # // relax neighbors
                i = Rmate[j];
                for k in range(n):
                    if (seen[k]): continue
                new_dist = dist[j] + cost[i][k] - u[i] - v[k];
                if (dist[k] > new_dist):
                  dist[k] = new_dist;
                  dad[k] = j;

            # // update dual variables
            for k in range(n):
                if (k == j or not seen[k]): continue;
                i = Rmate[k];
                v[k] += dist[k] - dist[j];
                u[i] -= dist[k] - dist[j];

            u[s] += dist[j];

            # // augment along path
            while (dad[j] >= 0):
                d = dad[j];
                Rmate[j] = Rmate[d];
                Lmate[Rmate[j]] = j;
                j = d;

            Rmate[j] = s;
            Lmate[s] = j;

            mated+=1;


        value = 0;
        for i in range(n):
            value += cost[i][Lmate[i]];
        print(value)
        return value;
    print(mincostmatch(cost,Lmate,Rmate))


main()

