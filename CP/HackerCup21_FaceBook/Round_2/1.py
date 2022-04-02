import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("runway_validation_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    res = 0
    n,m = imap()
    s = ilist()
    b = s[:]
    # s.sort()
    for i in range(m):
        s[i] = [s[i],i]
    orig = [x[:] for x in s]
    p = []
    for i in range(n):
        p.append(ilist())
        p[i].sort()
    res = 0
    changed = [0]*m
    # print(*orig)
    ans = n*m
    inters = set(p[0])
    for i in range(n):
        l = 0
        r = 0
        if i>=1:
            inters &= set(p[i])
        ans -= len(set(b if i==0 else p[i-1])&set(p[i]))
        # ans+=sum(1 for k in Counter(p[i]).values() if k==1)
        marks = [1]*m
        markp = [1]*m
        s = [x[:] for x in orig]
        s.sort()
        while l<m and r<m:
            if s[l][0]==p[i][r]:
                marks[l] = 0
                markp[r] = 0
                l+=1
                r+=1
            elif s[l][0]<p[i][r]:
                l+=1
            else:
                r+=1
        idx1 = []
        idx2 = []
        for k in range(m):
            if marks[k]:
                idx1.append(s[k][1])
            if markp[k]:
                idx2.append(p[i][k])
        # print(idx1)
        # print(idx2)
        cnt = 0
        for k in range(len(idx1)):
            # print(idx1[k], len(changed))
            if not changed[idx1[k]]:
                changed[idx1[k]] = 1
            else:
                cnt+=1
            # cnt+=1
            orig[idx1[k]][0] = idx2[k]
        res+=cnt
        # print(cnt)
        # print(*orig)
        # print(*changed)
    # ans = n*m-m
    ans-=m
    for k in range(n-2,n):
        cntr = Counter(p[k])
        for i in list(inters):
            if cntr[i]>1:
                # inters.remove(i)
                # pass
                # ans+=1
                res-=1
    # cntr = Counter(b)
    # for i in list(inters):
    #     if cntr[i]>1:
    #         inters.remove(i)
    # ans+=(m-len(inters)
    # print(inters)
    # print(ans)


    print("Case #{}: {}".format(_+1, res))

