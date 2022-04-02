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

def variantsCount(n,s0,k,b,m,a):
    res =0
    cnt = 0
    s = [0]*n
    s[0] = s0
    if s[0]*s[0]<=a:
        cnt+=1
        res+=1
    for i in range(1,n):
        s[i] = (k*s[i-1]+b)%m +1+s[i-1]
        if s[i]*s[i]<=a:
            res+=1
            res+=2*cnt
            # print(i,cnt,s[i])
            cnt+=1
        else:
            while cnt>=0 and s[cnt]*s[i]>a:
                cnt-=1
            res+=2*(cnt+1)
            # print(i,cnt,s[i])
    # print(*s)
    return res

x = []
for i in range(6):
    x.append(int(input()))
print(variantsCount(*x))
