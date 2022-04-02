import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)










import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify
def solve(N, Arr):
    heap = []
    for v,x,y in Arr:
        heap.append((x*x+y*y,-v,x,y))
    heapify(heap)
    while len(heap)>1:
        a = heappop(heap)
        b = heappop(heap)
        x = a[2]-b[2]
        y = a[3]-b[3]
        heappush(heap, (x*x+y*y, a[0]+b[0], x,y))
    return heap[0][2:]

T = int(input())
for _ in range(T):
    N = int(input())
    Arr = [list(map(int, input().split())) for i in range(N)]

    out_ = solve(N, Arr)
    print(' '.join(map(str, out_)))









# for _ in range(int(input())):
#     n = int(input())
#     a = ilist()
#     print(*solve(n,a))

n = 4
a = [[9,1,0], [4,9,0], [12,0,1],[15,4,0]]
print(solve(n,a))
