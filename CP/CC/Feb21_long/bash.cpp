// # Referances:
// # https://www.geeksforgeeks.org/maximum-bipartite-matching/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 102;

int n, N, p[4], row[2*mxn];
array<int,2> inp[51][51];
char res[51][51];
string sym ="ULDR";
string rSym = "DRUL";
array<int,2> dirs[4] = {{-1,0},{0,-1},{1,0},{0,1}};
vector<int> adj;
bool isBipartite(int v, vector<bool>& visited, vector<int>& color){
    for (int u : adj[v]) {
        if (visited[u] == false) {
            visited[u] = true;
            color[u] = !color[v];
            if (!isBipartite(adj, u, visited, color))
                return false;
        }
        else if (color[u] == color[v])
            return false;
    }
    return true;
}

int flat(int x, int y){
    return x*n+y;
}

pair<int,int> aflat(int x){
    return {x/n,x%n};
}

void solve(){
    int i,j;
    cin>>n;
    for(i=0;i<4;++i)cin>>p[i];

    set<array<int,2>> st;
    set<array<int,4>> src;
    for(i=0; i<n;++i){
        for(j=0;j<2*n;++j){
            cin>>row[j];
            row[j]--;
        }
        for (j=0; j<n;++j){
            inp[i][j] = {row[2*j],row[2*j+1]};
            if (inp[i][j][0]!=i or inp[i][j][1]!=j){
                st.insert({i,j});
                src.insert({i,j,i,j});
            }
        }
    }
    queue<array<int,4>> q;
    for (auto x:src) q.push(x);
    int pri,prj,x,y,k;
    while(!q.empty()){
        array<int,4> s = q.front();
        i,j,pri,prj = s[0],s[1],s[2],s[3];
        q.pop();
        for(k=0; k<4;++k){
            x=i+dirs[k][0],y=j+dirs[k][1];
            if (0<=x<n and 0<=y<n and inp[x][y][0]==pri and inp[x][y][1]==prj and st.count({x,y})==0 and !res[x][y]){
                res[x][y] = rSym[k];
                q.push({x,y,pri,prj});
            }
        }
    }
    unordered_map<pair<int,int>,int> comp;
    vector<pair<int,int>> decomp;
    for(i=0; i<n;++i){
        for (j=0; j<n;++j){
            if (inp[i][j][0]==i and inp[i][j][1]==j){
                comp[(i,j)] = len(decomp)
                decomp.append((i,j))
            }
        }
    }

    vector<array<array<int,2>,2>> edges;
    for(i=0; i<n;++i){
        for (j=0; j<n;++j){
            if (inp[i][j][0]!=i or inp[i][j][1]!=j)
        }
    }
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}



// import os, sys, bisect
// from collections import defaultdict, Counter, deque;
// from functools import lru_cache   #use @lru_cache(None)
// if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
// if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
// #
// input = lambda: sys.stdin.readline().strip()
// imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
// #------------------------------------------------------------------
// sys.setrecursionlimit(10**6)
// mod = int(1e9+7)

// n = int(input())
// p = ilist()
// inp = [['']*n for i in range(n)]

// q = deque()
// st = set()
// src = set()
// for i in range(n):
//     a = [x-1 for x in imap()]
//     for j in range(n):
//         inp[i][j] = (a[2*j], a[2*j+1])
//         if inp[i][j]!=(i,j):
//             x,y = inp[i][j]
//             src.add((x,y,(x,y)))
//             st.add((x,y))
// sym = "ULDR"
// rSym = "DRUL"
// dirs = [[-1,0],[0,-1],[1,0],[0,1]]
// q = deque(src)
// res = [['']*n for i in range(n)]
// while q:
//     i,j,pr = q.popleft()
//     for idx,[dx,dy] in enumerate(dirs):
//         x,y = i+dx,j+dy
//         if 0<=x<n and 0<=y<n and inp[x][y]==pr and (x,y) not in st and not res[x][y]:
//             res[x][y] = rSym[idx]
//             q.append((x,y,pr))
// # for i in range(n):
// #     for j in range(n):
// #         if inp[i][j] != (i, j) or res[i][j]: continue
// #         for idx,[dx,dy] in enumerate(dirs):
// #             x,y = i+dx,j+dy
// #             if 0<=x<n and 0<=y<n and inp[x][y]==(x,y) and not res[x][y]:
// #                 res[i][j] = sym[idx]
// #                 res[x][y] = rSym[idx]
// #                 break
// #-
// decomp = []
// comp = defaultdict(int)
// for i in range(n):
//     for j in range(n):
//         if inp[i][j]==(i,j):
//             comp[(i,j)] = len(decomp)
//             decomp.append((i,j))
// N = len(decomp)

// edges = []
// for i in range(n):
//     for j in range(n):
//         if inp[i][j]==(i,j):
//             if i+1<n and inp[i+1][j]==(i+1,j):
//                 edges.append((comp[(i,j)],comp[(i+1,j)]))
//             if j+1<n and inp[i][j+1]==(i,j+1):
//                 edges.append((comp[(i,j)],comp[(i,j+1)]))
// # print(edges)

// gr = defaultdict(list)
// for i,j in edges:
//     gr[i].append(j)
//     gr[j].append(i)

// def is_bipartite(graph):
//     n = len(graph)
//     color = [-1] * N
//     for start in graph:
//         if color[start] == -1:
//             color[start] = 0
//             stack = [start]
//             while stack:
//                 parent = stack.pop()
//                 for child in graph[parent]:
//                     if color[child] == -1:
//                         color[child] = 1 - color[parent]
//                         stack.append(child)
//                     elif color[parent] == color[child]:
//                         return False, color
//     return True, color
// red = []
// black = []
// partite,color = is_bipartite(gr)
// if not partite or color.count(1)!=color.count(0):
//     print(-1)
//     exit()
// for i in range(len(color)):
//     if color[i]:red.append(i)
//     else: black.append(i)
// graph = defaultdict(list)
// for i,j in edges:
//     if color[j]: i,j=j,i
//     graph[i].append(j)
// #-
// def bpm(u, matchR, seen):
//     for v in graph[u]:
//         if not seen[v]:
//             seen[v] = True
//             if matchR[v] == -1 or bpm(matchR[v],matchR, seen):
//                 matchR[v] = u
//                 return True
//     return False
// def maxBPM(N):
//     matchR = defaultdict(lambda :-1)
//     result = 0
//     for i in graph:
//         seen = defaultdict(bool)
//         if bpm(i, matchR, seen):
//             result += 1
//     res_edges = []
//     for i,v in matchR.items():
//         if i!=-1 and v !=-1 and i!=v:
//             res_edges.append((i,v))
//     return result, res_edges
// result, res_edges = maxBPM(N)
// if result!=len(graph):
//     print(-1)
//     exit()
// # match1,match2 = hopcroft_karp(graph,N,N)
// for i,j in res_edges:
//     if i>N and j>N: break
//     x,y =decomp[i],decomp[j]
//     dif = [y[0]-x[0],y[1]-x[1]]
//     if dif in dirs:
//         idx = dirs.index(dif)
//         res[x[0]][x[1]] = sym[idx]
//         res[y[0]][y[1]] = rSym[idx]
//     else:
//         print(-1)
//         exit()
// cnt = 0
// cost = 0
// for i in range(n):
//     for j in range(n):
//         if res[i][j] in "ULDR":
//             cost+=p[sym.index(res[i][j])]
//             cnt+=1
// def check(inp, res, n):
//     def dfs(i,j, vis):
//         dx,dy = dirs[sym.index(res[i][j])]
//         x,y = i+dx,j+dy
//         if 0<=x<n and 0<=y<n:
//             if (x,y) not in vis:
//                 vis[(x,y)] = 1
//                 return dfs(x,y,vis)
//             return (x,y)
//         return (-1,-1)
//     for i in range(n):
//         for j in range(n):
//             vis = {(i,j):1}
//             if dfs(i,j, vis)!=inp[i][j]:
//                 return 0
//     return 1
// if cnt != n*n or not check(inp,res,n):
//     print(-1)
//     exit()
// print(cost)
// for i in res:
//     print(''.join(i))
