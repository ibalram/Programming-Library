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

t = int(input())
x = int(input())
from random import randint
for _ in range(1,t+1):
    res = 0
    w,e = imap()
    hist = []
    chc = "rsp"
    choice = randint(0,2)
    r,s,p = [0]*(60),[0]*(60),[0]*(60)
    res = ""
    wt = 0
    if chc[choice]=="r":
        if w>e:
            p[0]+=1
            res+="P"
        else:
            r[0]+=1
            res+="R"
    if chc[choice]=="s":
        if w>e:
            r[0]+=1
            res+="R"
        else:
            s[0]+=1
            res+="S"
    if chc[choice]=="p":
        if w>e:
            s[0]+=1
            res+="S"
        else:
            p[0]+=1
            res+="P"
    for i in range(1,60):
        x = s[i-1]/i  #r
        y = p[i-1]/i  #s
        z = r[i-1]/i  #p
        r[i]+=r[i-1]
        p[i]+=p[i-1]
        s[i]+=s[i-1]
        if x>=y and x>=z:
            if w>e:
                p[i]+=1
                res+="P"
            else:
                r[i]+=1
                res+="R"
        elif y>=x and y>=z:
            if w>e:
                r[i]+=1
                res+="R"
            else:
                s[i]+=1
                res+="S"
        else:
            if w>e:
                s[i]+=1
                res+="S"
            else:
                p[i]+=1
                res+="P"
    print("Case #{}: {}".format(_, res))
