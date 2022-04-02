import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("weak_typing_chapter_1_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    res = 0
    n = int(input())
    s = input().strip()
    distinct = []
    s = s.replace("F","")
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            distinct.append(s[i-1])
    if s:
        distinct.append(s[-1])
    # print(s)
    res = max(0,len(distinct)-1)

    print("Case #{}: {}".format(_+1, res))

