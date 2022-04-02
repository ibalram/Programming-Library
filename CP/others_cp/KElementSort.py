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




def KElementSort(arr, k):
    a = []
    n = len(arr)
    for i in range(0,n-k+1, k):
        a.append(arr[i:i+k])
    a.sort(key = lambda x: int("".join(map(str, x))))
    res = []
    for i in a:
        res+=i
    return res




print(KElementSort([1,7,2,9,1,3,1,5,3], 3))
print(KElementSort([1,32,5,4,1,2], 2))
