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

from collections import defaultdict

def power(x,y):
    res = 1
    while y>0:
        if y%2:
            res = res*x%mod
        x = x*x%mod
        y>>=1
    return res
fact = [1]*(200005)
ifact = [1]*(200005)
for i in range(1,200005):
    fact[i] = fact[i-1]*i%mod
    ifact[i] = ifact[i-1]*power(i,mod-2)%mod
for _ in range(int(input())):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    from bisect import bisect_right
    l = 0
    res = 0
    while l<n:
        idx = bisect_right(a, a[l]+k)
        cnt = idx-l-1
        if cnt>=m-1: res = (res + fact[cnt]*ifact[cnt-m+1]%mod*ifact[m-1]%mod)%mod
        l+=1
    print(res)
    # mp = defaultdict(int)
    # for i in a:
    #     mp[i]+=1
    # res = 0
    # for i in mp.keys():
    #     x = mp[i]
    #     res+= x*(x-1)*(x-2)//6
    # ls = list(mp.keys())
    # for i in ls:
    #     res+=mp[i]*mp[i-1]*mp[i+1]
    #     res+=(mp[i-1]+mp[i-2])*mp[i]*(mp[i]-1)//2
    #     res+=(mp[i+1]+mp[i+2])*mp[i]*(mp[i]-1)//2
    # print(res)

