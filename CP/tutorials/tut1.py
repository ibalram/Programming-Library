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

# #pattern 1
# # *
# # * *
# # * * *
# for i in range(1,n+1):
#     print("* "*(i))


# #pattern 2
# #     *
# #   * *
# # * * *
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*(i))


# #pattern 3
# #   *
# #  * *
# # * * *
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*(i))


#pattern 3
#   *
#  * *
# * *
#  * *
#   *
for i in range(1,n+1):
    print("*"*(n-i)+"  "*(i))
for i in range(n-1,0,-1):
    print("*"*(n-i)+"  "*(i))
