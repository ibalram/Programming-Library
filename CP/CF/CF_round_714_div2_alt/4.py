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

n,k,x = imap()
s = list(input().strip())
# cnt = 0
# emer = []
# while s and s[-1]=='a':
#     emer.append(s.pop())

# n = len(s)
# i = n-1
# while i>=0 and cnt<x:
#     if s[i]=="b":
#         cnt+=1
#     i-=1

# ns = s[:i+1]
# bs = s[i+1:]
# rem = k-x
# def takeA(num,idx):
#     res = ''
#     for i in range(idx,n):
#         if s[i]=='b':
#             res+=s[i]
#         elif s[i]=='a' and num:
#             res+=s[i]
#             num-=1
#     return res

# if ns.count('a')>=rem:
#     res = "a"*rem +"b"*x
# elif s.count('a')>=rem:
#     rem = ns.count('a')
#     res = "a"*(rem)+takeA(k-rem-x, i+1)
#     print(ns,"yez")
# else:
#     takeb = k-s.count('a')-len(emer)-len(bs)
#     # az = s.count('a')
#     # bz = k-az-x
#     while i>=0 and takeb:
#         if s[i]=='b':
#             takeb-=1
#         i-=1
#     bs = s[i+1:]
#     res = "a"*(k-len(bs))+bs
# print(res)




# CPP program for the above approach

# Function to find lexicographically
# smallest subsequence of size K
def smallestSubsequence(S, K, X):
    # Length of string
    N = len(S)
    # Stores the minimum subsequence
    answer = []
    sf = [1 if i=='b' else 0 for i in S]
    for i in range(n-2,-1,-1):
        sf[i]+=sf[i+1]
    # Traverse the string S
    cntr = 0
    for i in range(N):
        # If the stack is empty
        if (len(answer) == 0):
            cntr+=S[i]=='b'
            answer.append(S[i])
        else:
            # Iterate till the current character is less than the the character at the top of stack
            while answer and S[i]<answer[-1] and (len(answer) - 1 + N - i >= K) and cntr+sf[i]>=X+1:
                cntr-=answer.pop()=='b'
            # If stack size is < K
            if len(answer) < K:
                answer.append(S[i])
                cntr+=S[i]=='b'
            if S[i]=='b' and cntr+sf[i]==X:
                answer.append(S[i])
                cntr+=1
            print(cntr,sf[i])
    # Stores the resultant string
    # ret = []
    ret = answer[:]
    indd = list(range(len(ret)))
    indd.sort(key=lambda x:[-ord(ret[x]),x])
    indd = indd[:K]
    indd.sort()
    ret = [ret[i] for i in indd]
    ret = ''.join(ret)
    print(ret)

print(smallestSubsequence(s,k,x))
