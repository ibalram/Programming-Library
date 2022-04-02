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


orda = lambda x: ord(x)-ord("a")
def ans(s,k):
    ln = len(s)
    cnt = 0
    for i in range(ln):
        cnt += ((orda(s[i]))*pow(k, ln-i-1,mod))
        cnt%=mod
    return cnt


for _ in range(1,int(input())+1):
    res = 0
    n,k = imap()
    s = input().strip()
    l = (n+1)//2
    a = s[:l]
    res = ans(a,k)
    temp = a[:-1]
    lst = a[-1]
    x = (a+a[::-1] if n%2==0 else temp+lst+temp[::-1])
    # print(x)
    if x<s:
        res+=1
    print("Case #{}: {}".format(_, res%mod))
