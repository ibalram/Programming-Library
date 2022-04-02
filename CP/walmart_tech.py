# import os, sys, bisect
# from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
# if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
# #
# input = lambda: sys.stdin.readline().strip()
# imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
# #------------------------------------------------------------------
# mod = int(1e9+7)


# import sys
# from collections import *
# sys.setrecursionlimit(10**6)
# n,m1,m2 = map(int,input().split())
# g1 = defaultdict(list)
# g2 = defaultdict(list)

# for i in range(m1):
#     u,v = map(int,input().split())
#     g1[u].append(v)
#     g1[v].append(u)
# for i in range(m2):
#     u,v = map(int,input().split())
#     g2[u].append(v)
#     g2[v].append(u)



# def comps(g):
#     vis = [0]*(n+1)
#     comps = []
#     def dfs(s):
#         vis[s] = 1
#         for i in g[s]:
#             if vis[i]:continue
#             dfs(i)
#     for i in range(1,n+1):
#         if vis[i]==0:
#             dfs(i)
#             newComp = []
#             for j in range(1,n+1):
#                 if vis[j]==1:
#                     newComp.append(j)
#                     vis[j]+=1
#             comps.append(newComp)
#     return comps
# comps1 = comps(g1)
# comps2 = comps(g2)

# class DSU:
#     def __init__(self, n):
#         self.par = list(range(n+1))

#     def addComp(self, comps):
#         for comp in comps:
#             p = comp[0]
#             for i in comp[1:]:
#                 self.par[i] = p

#     def find(self, a):
#         if self.par[a]==a:return a
#         self.par[a] = self.find(self.par[a])
#         return self.par[a]

#     def union(self, a,b):
#         a = self.par[a]
#         b = self.par[b]
#         if a==b: return
#         self.par[b] = a

# ds1 = DSU(n)
# ds2 = DSU(n)
# ds1.addComp(comps1)
# ds2.addComp(comps2)

# res = 0
# ans = []
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         a = ds1.find(i)
#         b = ds1.find(j)
#         if a==b: continue
#         c = ds2.find(i)
#         d = ds2.find(j)
#         if c==d: continue
#         ds1.union(a,b)
#         ds2.union(c,d)
#         res+=1
#         ans.append((i,j))

# print(res)
# for i, j in ans:
#     print(i,j)


"""

class Employee

List<Employee> list = new ArrayList<
Comparator comparator = new Comparator( (Employee a, Employee b) -> (a.age-b.age));

Arrays.sort(list, comparator);






int n = 4; // (0<=n<=20);

matrix -> n*n
1 -> n*n

1->2->3->4
8 7 6 5
5 6 7 8

9 10 11 12
16 15 14 13

cell(i,j) = (i+1)*n+(j+1) + ()

time: O(n*n) // n = number of rows, m = number of cols
aux. space: O(1)

int counter = 1;
for (int i = 0; i<n; ++i){
    if (i%2==0){
        for (int j = 0; j<n; j++){
            matrix[i][j] = counter++;
        }
    }
    else{
        for (int j = n-1; j>=0; j--){
            matrix[i][j] = counter++;
        }
    }
}


# arr(i) =   {0,1,2}

# arr = {0,1,2,1,2,2,1,2,1,0,0,1};
k = 0
i = 0
j = n-1

k = 1
i = 1
j = n-1

k = 2
i = 1
j = n-1
swap(arr[k], arr[j--])

k = 3
i = 1
j = n-2

k = 4
i = 1
j = n-2
swap(arr[k], arr[j--]);
swap(arr[i++], arr[k]);

arr = {0,0|,1,1,1,2,1,2,1,0,|2,2};
                              k

public int[] solve( int[] arr, int n){
    int i = 0, j = n-1;
    for (int k = 0; k<n; ++k){
        if (k>=j){
            break;
        }
        if (arr[k]==0){
            swap(arr[k], arr[i++]);
        }
        else if (arr[k]==2){
            swap( arr[k], arr[j--]);
            if (arr[k]==0){
                swap(arr[k], arr[i++]);
            }
        }
    }
}

















"""
