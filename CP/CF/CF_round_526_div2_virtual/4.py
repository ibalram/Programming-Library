import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
# sys.setrecursionlimit(10**6)
import sys
sys.setrecursionlimit(3*10**5+5)
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
mod = int(1e9+7)

n = int(input())
w = [0]+ilist()
gr = defaultdict(list)
for i in range(n-1):
    x,y,c = imap()
    gr[x].append([y,c])
    gr[y].append([x,c])
@bootstrap
def dfs(s,par):
    mxls = []
    res = 0
    for i,c in gr[s]:
        if i==par: continue
        childmx, childres = yield dfs(i,s)
        res = max(childres,res)
        # mxls.append(max(childmx-c,0))
        cur = max(childmx-c,0)
        if len(mxls)<2: mxls.append(cur)
        else:
            mn = min(mxls)
            if mn<cur:
                mxls[mxls.index(mn)] = cur
    if not mxls:
        yield (w[s],w[s])
    yield (max(max(mxls),0)+w[s],max(sum(mxls)+w[s],res))
print(dfs(1,-1)[1])
