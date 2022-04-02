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

from collections import defaultdict, Counter
for _ in range(int(input())):
    s = input().strip()
    dub = 0
    ones = 0
    for value in Counter(s).values():
        dub+=value//2
        ones+=value%2
    if ones>=dub:
        print(dub)
        continue
    while ones<dub:
        ones+=2
        dub-=1
    print(min(dub,ones))
