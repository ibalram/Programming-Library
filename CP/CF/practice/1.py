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


from itertools import permutations
from math import gcd
tick = 1/12 *10**-10
for _ in range(1,int(input())+1):
    res = 0
    a,b,c = map(int, input().split())
    h,m,s,n = 0,0,0,0
    ls = [a,b,c]
    def calc(ns,s,m,h):
        sa = (s*10**9+ns)
        ma = (m*60*10**9+sa)
        ha = h*3600*10**9+ma
        return 720*sa,12*ma,ha
    res = []
    lcm = lambda x,y:x*y//gcd(x,y)
    cal = lambda x,y,z:(x//720,y//12-x//720,z-(y//12-x//720))
    for i,j,k in permutations(range(0,3)):
        tot = min(ls[i]//(10000), ls[j]//(720*10000), ls[k]//(720*10000))
        a = ls[i]-tot*(10000)-720*10000
        b = ls[j]-tot*(10000)-720*10000
        c = ls[k]-tot*(10000)-720*10000
        f = 0
        for ii in range(36720):
            a+=10000
            b+=10000
            c+=720*10000
            s,m,h = cal(a,b,c)
            ns = s%(10**9)
            s//=10**9
            m//=10**9*60
            h//=10**9*3600
            if calc(ns,s,m,h)==(a,b,c):
                res = [ns,s,m,h]
                f = 1
                break
            # print(ns,s,m,h)
        if f:
            break

    # for i,j,k in permutations(range(0,3)):
    #     try:
    #         lc = 1
    #         lc = lcm(lc,720*10**9-ls[i]%(720*10**9))
    #         lc = lcm(lc,720*60*10**9-(60*ls[j]-ls[i])%(720*60*10**9))
    #         lc = lcm(lc,720*3600*10**9- (720*ls[k]-60*ls[j]-ls[i])%(720*3600*10**9))
    #     except:
    #         continue
    #     ls[i]+=lc
    #     ls[j]+=lc
    #     ls[k]+=lc
    #     rot = 0
    #     if ls[i]%720:
    #         rot+=ls[i]%720
    #         ls[i]-=rot
    #         ls[j]-=rot
    #         ls[k]-=rot
    #     if ls[j]%12:
    #         val = lcm(ls[j]%12,rot)
    #         rot+=val
    #         ls[i]-=val
    #         ls[j]-=val
    #         ls[k]-=val
    #     s,m,h = cal(ls[i],ls[j],ls[k])
    #     # ns = s%(10**9)
    #     if s%10**9:
    #         val = lcm((s%10**9)*720,rot)
    #         rot+=val
    #         ls[i]-=val
    #         ls[j]-=val
    #         ls[k]-=val
    #     s,m,h = cal(ls[i],ls[j],ls[k])
    #     if m%(60*10**9):
    #         val = lcm((s%(60*10**9)*720,rot))
    #         rot+=val
    #         ls[i]-=val
    #         ls[j]-=val
    #         ls[k]-=val
    #     s,m,h = cal(ls[i],ls[j],ls[k])
    #     s//=10**9
    #     m//=10**9*60
    #     h//=10**9*3600
    #     s,m,h = cal(ls[i],ls[j],ls[k])
    #     ns = s%(10**9)
    #     s//=10**9
    #     m//=10**9*60
    #     h//=10**9*3600
    #     if calc(ns,s,m,h)==(ls[i],ls[j],ls[k]):
    #         res = [ns,s,m,h]
    #         break
    #     print(ns,s,m,h)
    #     print(ls)
    #     print(calc(ns,s,m,h))
    # ls.sort(key = lambda x:(x%720, x%12))
    # hd = ls[0]%720
    # md = ls[1]%720
    # sd = ls[2]%720
    # print(hd,md,sd)
    print("Case #{}:".format(_), *res[::-1])
