import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)

mod = int(1e9+7)

for _test in range(int(input())):
    res = 0
    n,c = imap()
    intervels = []
    a = []
    for i in range(n):
        intervels.append(ilist())
        x,y = intervels[i]
        a.append((x,-1))
        a.append((y,1))
    a = Counter(a)
    a = list(sorted(a.items()))
    m = len(a)
    bal = 0
    lst = -1
    kes = defaultdict(int)
    vv = defaultdict(list)
    for (v,sgn),cnt in a:
        if lst!=-1:
            vv[bal].append([lst+1,v-1])
        kes[v] = max(kes[v],bal)
        if sgn==-1:
            bal+=cnt
        else:
            bal-=cnt
        kes[v] = max(kes[v],bal)
        lst = v
    cnt = 0
    res = 0
    st = set()
    xx = sorted(vv.keys(), reverse = True)
    yy = sorted(kes.keys(), reverse = True)
    i = 0
    j = 0
    while i<len(xx) and j<len(yy):
        if c<=0:
            break
        if xx[i]>=yy[j]:
            res+= xx[i]
            for _x in vv[xx[i]]:
                s,e = _x
                c-=e-s+1
            i+=1
        else:
            res+= yy[i]
            c-=1
            j+=1
    # i = 1
    # lst = a[0][0]
    # cnt = 1
    # strip = defaultdict(list)
    # while i<2*n:
    #     cntr = 0
    #     while i<2*n and a[i][0]==a[i-1][0] and a[i][1]==-1:
    #         i+=1
    #         cntr+=1
    #         cnt+=1
    #     strip[cnt].append([a[i-1][0],a[i][0]])
    #     lst = a[i]


    print('Case #{}:'.format(_test+1), res)
