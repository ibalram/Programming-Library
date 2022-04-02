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


print(2*3*5*7*11*13*17)#*19)
from heapq import heappop, heappush, heapify
for _ in range(int(input())):
    k,x = map(int,input().split())
    primes = []
    for i in range(2, int(x**.5)+1):
        if x%i==0:
            primes.append(i)
            while x%i==0:
                x//=i
    if x>2:
        primes.append(x)
    res = 0
    primes.sort()
    if len(primes)>k:
        x = len(primes)-k
        # res = sum(primes[x:])
        # heap = primes[x:]
        # heapify(heap)
        # extra = primes[:x]
        # extra.sort(reverse = True)
        # for i in extra:
        #     # print(heap)
        #     tm = heappop(heap)
        #     heappush(heap,tm*i)
        # heap.sort()
        # # print(heap)
        # res = sum(heap)
        pst = float("inf")
        seq = []
        cn =0
        def rec(ls, other):
            global pst, seq,cn
            # print(ls,other)
            if len(ls)==0:
                sm = sum(other)
                if sm<pst:
                    seq = other[:]
                    pst = sm
                cn+=1
                return sm
            res = float("inf")
            for i in range(len(ls)):
                if len(other)<k:
                    res = min(res, rec(ls[:i]+ls[i+1:], other+[ls[i]]))
                    continue
                for j in range(len(other)):
                    res = min(res, rec(ls[:i]+ls[i+1:], other[:j]+[other[j]*ls[i]]+other[j+1:]))
            return res
        res = rec(primes, [])
        print(seq,cn)
        # x = len(primes)-k
        # print(primes)
        # res = sum(primes[x:])
        # prod = 1
        # for i in primes[:x]:
        #     prod*=i
        # print(prod,primes[:x],)
        # res +=prod
    else:
        # if len(primes)>=2:
        #     primes.append(primes[0]+primes[1])
        #     primes.sort()
        #     primes = primes[2:]
        x = k-len(primes)
        # print(primes, x)
        res = sum(primes)+x
    print(res)

# import math
# print(math.factorial(8))

# print(11*19)

# 2 3 5 7 9
# 30 7
# 14 15
# 10 21
