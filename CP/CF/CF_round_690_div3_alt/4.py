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

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pf = [a[0]]
    for i in range(1,n):
        pf.append(pf[i-1]+a[i])
    pf.append(0)
    sm = sum(a)
    f = n-1
    for i in range(n,0,-1):
        if sm%i: continue
        # print("---")
        chk = sm//i
        init = 1
        cnt = 0
        anss = 0
        for j in range(n):
            if pf[j]==init*chk:
                # print("YES0",j,cnt,init)
                init+=1
                anss += cnt
                cnt = 0
            else:
                cnt+=1
        # print(init,"nnn")
        if init-1==i: f = min(f, anss)
    print(f)
    # res = 0
    # while len(a)>1:
    #     if len(set(a))==1: break
    #     idx = a.index(min(a))
    #     if idx==0:
    #         a[idx+1]+=a[idx]
    #     elif idx==len(a)-1:
    #         a[idx-1]+=a[idx]
    #     else:
    #         mn = idx-1
    #         if a[idx+1]<a[mn]:
    #             mn = idx+1
    #         a[mn]+=a[idx]
    #     a.pop(idx)
    #     res+=1
    # print(res)
