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

k = int(input())
s = list(map(int,list(input()[:-1])))
t = list(map(int,list(input()[:-1])))
den = (9*k-8)*(9*k-9)
num = 0

def calc(a):
    b = [i for i in range(10)]
    for i in a:
        b[i]*=10
    return sum(b)
cnt = [k]*10
for i in range(1,10):
    cnt[i]-=s.count(i)+t.count(i)
for i in range(1,10):
    for j in range(1,10):
        if calc(s+[i])>calc(t+[j]):
            num+=cnt[i]*(cnt[j]-(i==j))
print(num/den)
