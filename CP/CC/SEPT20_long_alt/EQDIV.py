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

k = int(input())

def calc(n):
    if k==1:return n*(n+1)//2
    if k==2: return n*(n+1)*(2*n+1)//6
    if k==3:return (n*(n+1)//2)**2
    if k==4: return n*(n+1)*(2*n+1)*(3*n**2+3*n-1)//30

for _ in range(int(input())):
    n = int(input())
    a = [i**k for i in range(1,n+1)]
    f = 0
    sm = calc(n)
    # if sm%2!=0:
    #     f =1
    # if f:
    #     print(-1)
    #     continue
    sm//=2
    def bs(x,i):
        l = 0
        r = i
        res = -1
        while r-l>=0:
            mid = l+r>>1
            if a[mid]<=x:
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res
    mx = n-1
    res = [0]*(n)
    while sm:
        i = bs(sm,mx)
        # print(i,sm)
        if i==-1:
            break
        res[i] = 1
        mx = i-1
        sm-=a[i]
        # print(sm,i)
    if f:
        print(-1)
    else:
        print(abs(sum(a[i] if res[i] else -a[i] for i in range(n))))
        print("".join(map(str,res)))

