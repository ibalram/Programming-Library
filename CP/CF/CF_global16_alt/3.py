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

for _ in range(int(input())):
    n = int(input())
    s = [list(input().strip()) for i in range(2)]
    a = []
    for j in range(n):
        cnt = 0
        for i in range(2):
            cnt+=s[i][j]=="1"
            cnt-=s[i][j]=="0"
        a.append(cnt)
    st = []
    for i in range(n):
        if a[i]==-2:
            if st and st[-1]==2:
                st.pop()
                st.append(0)
            else:
                st.append(a[i])
        elif a[i]==2:
            if st and st[-1]==-2:
                st.pop()
                st.append(0)
            else:
                st.append(a[i])
        else:
            st.append(0)
    res = 2*st.count(0) + st.count(-2)
    print(res)

    # print(min(2,a.count("0")))
