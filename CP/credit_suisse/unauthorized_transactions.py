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

def organizingContainers(container):
    n = len(container)
    row = []
    col = []
    for i in range(n):
        rowSum = sum(container[i])
        colSum = sum(container[j][i] for j in range(n))
        if rowSum!=colSum:
            return "Impossible"
    return "Possible"

if __name__ == "__main__":
    q = int(input().strip())
    answer=""
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        if(answer == ""):
             answer = str(result)
        else:
            answer = answer +  "," +str(result)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line
