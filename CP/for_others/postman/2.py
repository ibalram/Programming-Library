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

def maxPerksItems(cartridges, dollers, recycleReward, perksCost):
    l = 0
    r = cartridges
    def check(perks):
        sold = cartridges-perks
        return sold*recycleReward +dollers>=perksCost*perks
    res = 0
    while r-l>=0:
        mid = l+r>>1
        if check(mid):
            res = mid
            l = mid+1
        else:
            r = mid-1
    return res


x = []
for i in range(4):
    x.append(int(input()))
print(maxPerksItems(*x))
