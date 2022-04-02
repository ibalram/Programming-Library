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
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**5+10)
from types import GeneratorType
#use:- put @bootstrap overrecursive function
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack: return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack: break
                    call = stack[-1].send(call)
            return call
    return wrapped_function

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    g = defaultdict(list)
    for i in range(n-1):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)
    cntr ={}
    sz = [1]*(n+1)
    @bootstrap
    def dfs(s,par):
        cur = a[s-1]
        for i in g[s]:
            if i==par: continue
            cur^=(yield dfs(i,s))
            sz[s]+=sz[i]
        if s>1 and sz[s]<=2 and cur not in cntr:
            cntr[cur] = s
        yield cur
    tot = dfs(1,-1)
    # print(tot, val)
    res = "NO"
    if tot==0:
        res = "YES"
    elif tot in cntr and k>2:
        res = "YES"
    print(res)
    # print("YES" if tot==0 or cntr[tot]>1 and k>2 else "NO")
