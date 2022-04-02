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

l,r = imap()

# # mxn = 1000002
# # spf = list(range(mxn))
# # def sieve():
# #     for i in range(4,mxn,2): spf[i]=2
# #     for i in range(3, int(mxn**.5)+1, 2):
# #         if spf[i]!=i: continue
# #         for j in range(i*i, mxn, i):
# #             if spf[j]==j: spf[j]=i
# # sieve()
# # def pFactor(x):
# #     ret = []
# #     while x>1:
# #         tmp,cnt = spf[x],1
# #         x//=tmp
# #         while x%tmp==0: x,cnt = x//tmp, cnt+1
# #         ret.append(tmp)
# #     return ret

# phi=[]
# def computeTotient(n):
#     for i in range(n + 2):
#         phi.append(0)
#     for i in range(1, n+1):
#         phi[i] = i
#     for p in range(2,n+1):
#         if (phi[p] == p):
#             phi[p] = p-1
#             for i in range(2*p,n+1,p):
#                 phi[i] = (phi[i]//p) * (p-1)
#     # for i in range(1,n+1):
#     #     print("Totient of ", i ," is ",
#     #     phi[i])

# computeTotient(2000001)

# mark = {i:0 for i  in range(l,r+1)}
# res = 0
# for i in range(l,r+1):
#     res += i-l-(phi[i]-phi[l])-mark[i]
#     # print(i,phi[i]-phi[l-1], mark[i])
#     x = i
#     while x<=r:
#         mark[x]+=1
#         x+=i
# # print(phi[:8])
# print(res)

# 392046112148
# 392047955148
# 392045955148
# 196024977574
# 644909296806



def get(g,x):
    return x//g
res = 0
mark = [0]*(r+2)
for g in range(r,1,-1):
    x = get(g,r)-get(g,l-1)
    if g>=l:
        x-=1
    cur = x*(x-1)
    for i in range(2*g,r+1, g):
        if i>=l:
            cur-=get(i,r)-1
        cur-=mark[i]
    mark[g] = cur
    res+=mark[g]
    # for i in range(2*)
    # print(g,x)
    # if g>=l:
    #     res-=get(g,r)
    #     print(get(g,r))
    # print(x)
print(res)

