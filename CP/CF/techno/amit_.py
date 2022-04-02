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



def solution2(S):
    n = len(S)
    orda = lambda x: ord(x)-ord("a")
    ordA = lambda x: ord(x)-ord("A")
    res = float("inf")
    for i in range(n):
        for j in range(i,n):
            seg = S[i:j+1]
            mpa = [0]*26
            mpA = [0]*26
            for k in seg:
                if k.isupper():
                    mpA[ordA(k)]=1
                else:
                    mpa[orda(k)]=1
            if all(mpa[i]==mpA[i] for i in range(26)):
                if res>len(seg):
                    res = len(seg)
    return res if res!=float("inf") else -1


# print(solution2("CATattac"))
# print(solution2("azABaabza"))
# print(solution2("TacoCat"))
# print(solution2("AcZCbaBz"))


def solution(A,K):
    n = len(A)
    even =[]
    odd = []
    if K>n: return -1

    for i in A:
        if i%2: odd.append(i)
        else: even.append(i)
    even.sort()
    odd.sort()
    res = 0
    while K>0:
        if K%2:
            if even:
                res+=even.pop()
            else:
                return -1
            K-=1
        elif len(even)>1 and len(odd)>1:
            ev = sum(even[-2:])
            od = sum(odd[-2:])
            if ev<=od:
                res+=odd.pop()+odd.pop()
            else:
                res+=even.pop()+even.pop()
            K-=2
        elif len(even)>1:
            res+=even.pop()+even.pop()
            K-=2
        elif len(odd)>1:
            res+=odd.pop()+odd.pop()
            K-=2
    return res




print(solution([4,9,8,2,6],3))
print(solution([5,6,3,4,2],5))
print(solution([7,7,7,7,7],1))
print(solution([10000],2))
print(solution([2,3,3,5,5],3))
