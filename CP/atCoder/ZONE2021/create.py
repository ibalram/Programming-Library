
string = """import os, sys, bisect
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

"""
exec(string)

x = open('in.txt','w')
x.close()
x = open('out.txt','w')
x.close()

for i in range(1,6):
    x = open('{}.py'.format(i),'w')
    x.write(string)
    x.close()
