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


n  = 5

ln =2*n+1
val = "#abcdefghijklmnopqrstuvwxyz"
y = n
pst =[]
mat = []
rem = 2*(n-1)
for i in range(1,n+1):
    x = (len(pst)+1)//2
    res = pst[:x]+[val[y]]+pst[-x:]
    pst = res
    res = "-"*rem + "-".join(res) + "-"*rem
    y-=1
    rem-=2
    mat.append(res)
mat += mat[:n-1][::-1]
for i in mat:
    print(i)

