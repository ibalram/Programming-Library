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


#####################3333


# AbcDE
# AD
# 1sdEGgGb
# SEGGB

'''
convert string a to string b by changing some(0 or more) small
chars to uppercase and removing others
'''


a = input().strip()
b = input().strip()

# f = 1
# j = 0
# for i in b:
#     while j<len(a) and i in [a[j],a[j].upper()]:
#         j+=1
#     if j==len(a):
#         f = 0
#         break
# for i in range(j,len(a)):
#     if a[j].upper():
#         f = 0
#         break

from functools import lru_cache
@lru_cache
def rec(i,j):
    if i>=len(a) and j>=len(b):
        return 0
    if i>=len(a) or j>=len(b):
        if i>=len(b): return -float("inf")
        cnt = sum(1 if a[k].isupper() else 0 for k in range(j,len(a)))
        if cnt: return 0
        return -float("inf")
    res = max(rec(i,j+1), rec(i+1,j))
    if b[j] in (a[i],a[i].upper()):
        res= max(res, 1+rec(i+1,j+1))
    return res
print((rec(0,0)==len(b))*1)

