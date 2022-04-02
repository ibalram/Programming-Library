import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("consistency_chapter_1_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

vowel = "AEIOU"

for _ in range(int(input())):
    s = input().strip()
    res = len(s)
    mp = Counter(s)
    v = sum(1 for i in s if i in vowel)
    c = len(s)-v
    mxV = 0
    V = -1
    mxC = 0
    C = -1
    for i in mp:
        if i in vowel:
            if mxV<mp[i]:
                mxV = mp[i]
                V = i
        else:
            if mxC<mp[i]:
                mxC = mp[i]
                C = i
    res = float("inf")
    res = 2*(v-mxV)+c
    res = min(res, 2*(c-mxC)+v )

    print("Case #{}: {}".format(_+1, res))

