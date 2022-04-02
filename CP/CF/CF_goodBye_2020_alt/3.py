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

import os, sys
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    a = list(input().strip())
    n = len(a)
    # i = 0
    # while i<n-2:
    #     subs = a[i:i+3]
    #     if a[i]==a[i+1]==a[i+2]:
    #         a[i+1]="*"
    #         a[i+2] = "#"
    #         i = i+2
    #     elif a[i]==a[i+1]:
    #         a[i+1] = "#"
    #         i = i+1
    #     elif a[i+1]==a[i+2] or a[i]==a[i+2]:
    #         a[i+2] = "#"
    #         i = i+2
    #     else:
    #         i+=1
    op =["*", "#", "-", "$"]
    def get(chk):
        for i in op:
            if i not in chk:
                return i
    for i in range(n-2):
        subs = a[i:i+3]
        if a[i]==a[i+1]==a[i+2]:
            a[i+1]=get([a[i]])
            a[i+2] = get([a[i],a[i+1]])
        elif a[i]==a[i+1]:
            a[i+1] = get([a[i], a[i+2]])
        elif a[i+1]==a[i+2] or a[i]==a[i+2]:
            a[i+2] = get(set(a[i:i+2]))
    if n<3:
        print((len(set(a))!=n)*1)
        continue
    print(a.count("*")+a.count("#")+a.count("-")+a.count("$"))






