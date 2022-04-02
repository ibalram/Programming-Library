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

def two(n,q,m,a,qe):
    # n,q,m = map(int,input().split())
    # a = list(map(int,input().split()))
    pre = []
    queries = []
    rl = [0]*(m+2)
    p = [0]*(q)
    A = [0]*(q)
    for i in range(q):
        # l,r = map(int,input().split())
        l,r = qe[i]
        l-=1
        r-=1
        p[i] = a[l]+a[r]
        A[i] = a[l]
        # ll = a[l]
        # rr = a[r]+a[l]-1
        # while ll<=m:
        #     diff = rr-ll+1
        #     rl[min(m,ll)]+=1
        #     rl[min(m,rr)+1]-=1
        #     ll+=a[l]+diff
        #     rr+=a[l]+diff
    # x = list(range(q))
    # x.sort(key = lambda x: p[i])
    b = int(m**.5+1)
    # difference = defaultdict(int)
    difference = [0]*(m+1)
    groups = defaultdict(list)
    for i in  range(q):
        if p[i]>=b:
            j = 0
            while j*p[i]<=m:
                difference[p[i]*j]-=1
                if p[i]*j+A[i]<=m:
                    difference[p[i]*j+A[i]]+=1
                j+=1
        else:
            groups[p[i]].append(A[i])
    # for i in range(1,m+1):
    #     difference[i]+=difference[i-1]
    for pp,aa in groups.items():
        cur = [0]*pp
        cur[0]-=len(aa)
        for i in aa:
            cur[i]+=1
        # for i in range(1,len(cur)):
        #     cur[i]+=cur[i-1]
        for i in range(0,m+1,pp):
            for j in range(pp):
                if i+j<m+1:
                    difference[i+j]+=cur[j]

    # for i in range(1,m+1):
    #     rl[i]+=rl[i-1]
    # print(difference)
    mn = q
    for i in range(1,m+1):
        difference[i]+=difference[i-1]
        mn = min(mn, -difference[i])
    # print(difference)
    # print(q-min(difference[1:m+1]))
    return q-mn, difference

def one(n,q,m,a,qe):
    # n,q,m = map(int,input().split())
    # a = list(map(int,input().split()))
    pre = []
    queries = []
    rl = [0]*(m+2)
    for i in range(q):
        # l,r = map(int,input().split())
        l,r = qe[i]
        l-=1
        r-=1
        ll = a[l]
        rr = a[r]+a[l]-1
        # diff = rr-ll+1+a[l]
        # tot = m+a[l]-rr-1
        # st = tot//diff
        # ll+=st*diff
        # rr+=st*diff
        # rl[min(m,ll)]+=1
        # rl[min(m,rr)+1]-=1
        # print(ll,rr)

        while ll<=m:
            diff = rr-ll+1
            rl[min(m,ll)]+=1
            rl[min(m,rr)+1]-=1
            ll+=a[l]+diff
            rr+=a[l]+diff
        # st = [0]*(m+1)
        # # mx = a[r]
        # # for j in range(l,r+1):
        # #     st[j] = 1
        # # mx = max(a[l:r+1])
        # def check(x):
        #     for j in range(l,r+1):
        #         if x-a[j]>=0:
        #             if st[x-a[j]]==0:return True
        #         else: return False
        #     return False
        # for j in range(1,m+1):
        #     if a[l]<=j<=a[r]:
        #         st[j]=1
        #         continue
        #     if j<a[l]:
        #         continue
        #     if check(j):
        #         st[j]=1
        # pre.append(st)
    for i in range(1,m+1):
        rl[i]+=rl[i-1]
    # print(max(rl))
    return max(rl),rl
    # res = 0
    # for i in range(1,m+1):
    #     cnt = 0
    #     for j in range(q):
    #         if pre[j][i]:cnt+=1
    #     res = max(res,cnt)
    # print(res)

from random import *
tt = 10
for _ in range(tt):
    n,q,m = [randint(1,100) for i in range(3)]
    a = [randint(1,100)]+[0]*(n-1)
    for i in range(1,n):
        a[i] = a[i-1]+randint(1,a[0])
    qe = []
    for i in range(q):
        l = randint(1,n)
        r = randint(l,n)
        qe.append([l,r])
    ans1, diff1 = one(n,q,m,a,qe)
    ans2, diff2 = two(n,q,m,a,qe)
    if ans1!=ans2:
        print("correct:",ans1)
        print(diff1)
        print("wrong:",ans2)
        print(diff2)
        print(n,q,m)
        print(*a)
        for i in qe:
            print(*i)
        break
