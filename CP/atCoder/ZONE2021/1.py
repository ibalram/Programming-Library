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

s = input().strip()

q = deque()
front = 0
for i in s:
    if i=="R":
        front^=1
    else:
        if front :
            q.appendleft(i)
        else:
            q.append(i)
ls = list(q)
if front:
    ls = ls[::-1]
# print(ls)
res = []
cnt = 1
st = []
for i in ls:
    if st and st[-1]==i:
        st.pop()
    else:
        st.append(i)
# for i in range(1,len(ls)):
#     if ls[i]!=ls[i-1]:
#         if cnt&1:
#             res.append(ls[i-1])
#         cnt = 1
#     else:
#         cnt+=1
# if cnt&1:
#     res.append(ls[-1])
print("".join(st))
