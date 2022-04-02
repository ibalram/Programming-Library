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

for _ in range(int(input())):
    n = int(input())
    inp = list(mapi())
    aans = 0
    for i in inp:
        aans^=i
    res = 0
    pre = 0
    cnt = 0
    def query(x,y):
        global cnt
        if x==2:
            print(aans,y)
            return -1*(y!=aans)
        cnt+=1
        if cnt>20:return -1
        tmp = 0
        for i in inp:
            tmp+=i^y
        return tmp
    # print(1,1<<20,flush=True)
    # sm = int(input())-n*(1<<20)
    pst = 0
    # sm = query(1,1<<19)-n*(1<<19)
    res2 = 0
    for i in range(20):
        # print(1,1<<i,flush=True)
        # x = int(input())
        x = query(1,1<<i)
        if i>=0:
            xx = ((pst-x)//(1<<i) +n)//2
            print(pst,x,x>>i)
            res2|=(1<<i) if xx%2 else 0
        pst = x
        if x==-1:print("fail");exit(0)
        # one = ((sm-x)//(1<<i) +n)//2
        # x^=(1<<i)
        # x&=(1<<i)
        # one = x//(1<<i)
        # res|=(1<<i) if one%2 else 0
    print(res2)
    # print(2,res, flush=True)
    # x = int(input())
    x = query(2,res)
    if x==-1:print("fail");exit(0)
    print("pass")
