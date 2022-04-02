import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6+10)
mod = int(1e9+7)

from math import ceil, log2;

def getMid(s, e) :
    return s + (e - s) // 2;
def getXorUtil(st, ss, se, qs, qe, si) :
    if (qs <= ss and qe >= se) :
        return st[si]
    if (se < qs or ss > qe) :
        return 0
    mid = getMid(ss, se);

    return getXorUtil(st, ss, mid, qs, qe, 2 * si + 1) ^ \
           getXorUtil(st, mid + 1, se, qs, qe, 2 * si + 2);

def updateValueUtil(st, ss, se, i,
                    prev_val, new_val, si) :

    if (i < ss or i > se) :
        return;

    st[si] = (st[si] ^ prev_val) ^ new_val;
    if (se != ss) :
        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i, prev_val,
                            new_val, 2 * si + 1);
        updateValueUtil(st, mid + 1, se, i,
            prev_val, new_val, 2 * si + 2);

def updateValue(arr, st, n, i, new_val) :
    new_val = arr[i]^new_val
    if (i < 0 or i > n - 1) :
        return;
    temp = arr[i];
    arr[i] = new_val;
    updateValueUtil(st, 0, n - 1, i, temp, new_val, 0);

def getXor(st, n, qs, qe) :
    if (qs < 0 or qe > n - 1 or qs > qe) :
        return 0;
    return getXorUtil(st, 0, n - 1, qs, qe, 0);


def constructSTUtil(arr, ss, se, st, si) :
    if (ss == se) :
        st[si] = arr[ss];
        return arr[ss]
    mid = getMid(ss, se);
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1)^constructSTUtil(arr, mid + 1, se, st, si * 2 + 2);
    return st[si];

def constructST(arr, n):
    x = (int)(ceil(log2(n)))
    max_size = 2 * (int)(2**x) - 1
    st = [0] * (max_size)
    constructSTUtil(arr, 0, n - 1, st, 0);
    return st

n,q = imap()
a = ilist()
st = constructST(a, n);
for i in range(q):
    t,x,y = imap()
    x-=1
    if t==1:
        updateValue(a, st, n, x, y)
    else:
        y-=1
        print(getXor(st, n, x, y))
