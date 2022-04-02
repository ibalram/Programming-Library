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


s = input().strip()
key = input().strip()

# print(s,key)
def decode(s,key):
    n = len(s)
    m = len(key)
    t = key
    n //=m
    mat = [["0"]*(m+1) for i in range(n+1)]

    cnt = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if ord(s[cnt])==32:
                mat[j][i] = "0"
            else:
                mat[j][i] = s[cnt]
            cnt+=1
    key = sorted(list(key))
    cnt = 0
    for i in range(1,m+1):
        mat[0][i] = key[cnt]
        cnt+=1
    key = t
    # print(mat)
    matrix = [[0]*(m+1) for i in range(n+1)]
    cnt = 1
    for i in range(m):
        for j in range(1,m+1):
            if key[i]==mat[0][j]:
                for k in range(1,n+1):
                    matrix[k][cnt]=mat[k][j]
                cnt+=1
    v = []
    cnt = 0
    a = ""
    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j]=="0" or matrix[i][j]=="_":
                v.append(a)
                a = ""
                continue
            a+=matrix[i][j]
    mp = {}
    mp["Khardung"]=1
    mp["Lachulung"]=1
    mp["Gyong"]=1
    mp["Sasser"]=1
    mp["Zoji"]=1
    mp["Sia"]=1
    mp["Indira"]=1
    mp["Rezang"]=1
    mp["Tanglang"]=1
    mp["Pensi"]=1
    mp["Marsimik"]=1
    flag = 0
    for i in range(len(v)):
        if v[i] in ["not", "Not"]:
            flag = 1
    for i in range(len(v)):
        if v[i] in mp:
            mp[v[i]] = 0
    res = []
    # print(mp)
    if flag ==1:
        for key in sorted(mp.keys()):
            if mp[key] ==1:
                res.append(key)
    else:
        for key in sorted(mp.keys()):
            if mp[key]==0:
                res.append(key)
    print(*res)
decode(s,key)
