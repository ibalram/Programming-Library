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

n = int(input())
sco = [0,n-1,0,n-1]
tco = [0,n-1,0,n-1]

def get():
    up = 0
    s = []
    for i in range(n):
        x = list(input().strip())
        if not up and x.count(".")!=n:
            up = 1
        if up:
            s.append(x)
    while len(s) and s[-1].count('.')==n:
        s.pop()
    m = len(s)
    left = 0
    right = n-1
    for i in range(n):
        count = sum(1 for j in range(m) if s[j][i]==".")
        if count!=m:
            left = i
            break
    for i in range(n-1,-1,-1):
        count = sum(1 for j in range(m) if s[j][i]==".")
        if count!=m:
            right = i
            break
    for i in range(m):
        s[i] = s[i][left:right+1]
    return s

s,t = get(),get()
if sorted([len(s),len(s[0])])!=sorted([len(t),len(t[0])]):
    print("No")
    exit()
def checkSame(s,t):
    if len(s)!=len(t): return 0
    if len(s[0])!=len(t[0]): return 0
    for i in range(len(s)):
        if s[i]!=t[i]:return 0
    return 1

if checkSame(s,t):
    print("Yes")
    exit()


def rotate(x):
    n =len(x)
    m = len(x[0])
    output = [[""]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            output[j][n-1-i] = x[i][j]
    return output

f = 0
for i in range(3):
    s = rotate(s)
    for j in range(4):
        if checkSame(s,t):
            f = 1
            break
        t = rotate(t)
    if f:
        break
print("Yes" if f else "No")
