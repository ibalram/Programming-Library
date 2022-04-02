import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------


import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    # def rec(l,r):
    #     if l==r:
    #         return 1
    #     mid = (l+r)>>1
    #     res = rec(l,mid)+rec(mid+1,r)
    #     if a[mid]==a[mid+1]:
    #         res-=1
    #     # print(l,r,"-",res,"'",a[mid],a[mid+1])
    #     return res

    st = [[] for i in range(4*n+1)]
    def build(root, l,r):
        if l==r:
            st[root] = [a[l],a[l],1]
            return [a[l],a[l],1]
        mid = (l+r)>>1
        ll = build(2*root+1, l,mid)
        rr = build(2*root+2, mid+1,r)
        if ll[1]==rr[0]:
            ll[2]-=1
        st[root] = [ll[0],rr[1], ll[2]+rr[2]]
        return [ll[0],rr[1], ll[2]+rr[2]]
    def update(root, l,r,idx):
        if idx<l or idx>r:
            return st[root]
        if l==r:
            st[root] = [a[l],a[l],1]
            return [a[l],a[l],1]
        mid = l+r>>1
        if idx<=mid:
            update(2*root+1, l,mid,idx)
            ll = st[2*root+1][:]
            rr = st[2*root+2][:]
            if ll[1]==rr[0]:
                ll[2]-=1
        else:
            update(2*root+2, mid+1,r,idx)
            ll = st[2*root+1][:]
            rr = st[2*root+2][:]
            if ll[1]==rr[0]:
                ll[2]-=1
        st[root] = [ll[0],rr[1], ll[2]+rr[2]]
        return st[root]
    build(0, 0,n-1)
    # print(st)
    for j in range(q):
        x,y = map(int,input().split())
        x-=1
        a[x] = y
        print(update(0, 0,n-1,x)[2])
        # print(st)

    # for j in range(q):
    #     x,y = map(int,input().split())
    #     a[x] = y
    #     res = 0
    #     cnt = 1
    #     b = []
    #     for i in range(1,n+1):
    #         if b and b[-1]==a[i]:
    #             continue
    #         b.append(a[i])
    #     # print(a)
    #     # res =max(cnt,res)
    #     print(len(b))


