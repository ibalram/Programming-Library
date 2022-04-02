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
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    mx = max(a)
    b = [i for i in range(n) if a[i]==mx]
    res = 0
    for i in b:
        if i+1>=k:
            res+=n-i
    print(res)
    # nxt = [n]*(n+1)
    # st = []
    # for i,v in enumerate(a):
    #     while st and a[st[-1]]<v:
    #         nxt[st.pop()] = i
    #     st.append(i)
    # while st: st.pop()
    # prv = [-1]*(n+1)
    # for i in range(n-1,-1,-1):
    #     v = a[i]
    #     while st and a[st[-1]]<v:
    #         prv[st.pop()] = i
    #     st.append(i)
    # while st: st.pop()
    # res = 0
    # i = 0
    # while i<n:
    #     back = prv[i]
    #     front = nxt[i]
    #     if i-back>=k:
    #         print(i,back)
    #         res+=front-i-1+ (i-back-k)
    #     i+=1
    # print(res)
