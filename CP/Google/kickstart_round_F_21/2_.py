import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------- fast io --------------------


# input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)

mod = int(1e9+7)

for _test in range(int(input())):
    res = 0
    d,n,k = imap()
    # mp = [0]*(d+1)
    # for i in range(n):
    #     h[i],s[i],e[i] = imap()
    #     mp[s[i]-1]+=h[i]
    #     mp[e[i]]-=h[i]
    # print(mp)
    # for i in range(1,d+1):
    #     mp[i]+=mp[i-1]
    # res = max(mp)
    # print(mp)
    st = set()
    queries = []
    for i in range(n):
        h,s,e = imap()
        st.add(s)
        st.add(e)
        queries.append((h,s,e))
    a = list(sorted(st))
    rev = defaultdict(int)
    for i in range(len(a)):
        rev[a[i]] = i
    mp = [[] for i in range(len(a)+1)]
    st = None
    a = None
    for h,x,y in queries:
        s,e = rev[x],rev[y]
        for j in range(s,e+1):
            heappush(mp[j], h)
            if len(mp[j])>k:
                heappop(mp[j])
    # print()
    res = 0
    for i in mp:
        res = max(res, sum(i))
    print('Case #{}:'.format(_test+1), res)
