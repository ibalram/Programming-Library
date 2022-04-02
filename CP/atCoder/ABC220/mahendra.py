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

mxn = 1000002
spf = list(range(mxn))
def sieve():
    for i in range(4,mxn,2): spf[i]=2
    for i in range(3, int(mxn**.5)+1, 2):
        if spf[i]!=i: continue
        for j in range(i*i, mxn, i):
            if spf[j]==j: spf[j]=i
sieve()
def pFactor(x):
    ret = 1
    while x>1:
        tmp,cnt = spf[x],1
        x//=tmp
        while x%tmp==0: x,cnt = x//tmp, cnt+1
        ret*=cnt+1
    return ret

cache = [0]*(10**6+1)
cache[1] = 1
for i in range(2,1000001):
    x = (pFactor(i))
    # if x%2:x+=1
    cache[i] = cache[i-1]+(x*(x+1)//2)+x%2

for _ in range(int(input())):
    print(cache[int(input())])








# for _ in range(int(input())):
#     n,m,k = imap()
#     c = ilist()
#     t = ilist()
#     mp = defaultdict(list)
#     for i,j in zip(c,t):
#         mp[i].append(j)
#     a = []
#     for topic in mp.keys():
#         mp[topic].sort(reverse=True)
#         a.append([topic,mp[topic]])
#     a.sort(key = lambda x: x[1][::-1])
#     # print(a)
#     res = 0
#     for i in range(len(a)):
#         time = a[i][1][-1]
#         if k>=time:
#             a[i][1].pop()
#             k-=time
#             res+=1
#             while len(a[i][1])>=2 and k>=sum(a[i][1][-2:]) and (i<len(a)-1 and sum(a[i][1][-2:])<=a[i+1][1][-1] or i==len(a)-1):
#                 k-=sum(a[i][1][-2:])
#                 res+=1
#                 a[i][1].pop()
#                 a[i][1].pop()
#     for i in range(len(a)):
#         while len(a[i][1])>=2 and k>=sum(a[i][1][-2:]):
#             k-=sum(a[i][1][-2:])
#             res+=1
#             a[i][1].pop()
#             a[i][1].pop()
#     print(res)



    # heapify(a)
    # while k:
    #     time, freq = heappop(a)
    #     if
























# 2
# zgwabcdegqwdhiklmnopqadsrtuwevxzgwe
# xyzabcdefghijklmnopqrstuvw


# 3 1
# 3 3
# 14142 17320
# 3 2

#
# import os, sys, bisect
# from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
# if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
# #
# input = lambda: sys.stdin.readline().strip()
# imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
# #------------------------------------------------------------------
# #sys.setrecursionlimit(10**6)
# mod = 998244353





# # import bisect
# # def solve(s):
# #     a = [ord(i)-ord("a") for i in s]
# #     b = []
# #     for i in a:
# #         idx = bisect.bisect_left(b,i)
# #         if idx>=len(b):
# #             b.append(i)
# #         else:
# #             b[idx] = i
# #     return 26-len(b)

# # for i in range(int(input())):
# #     s = input()
# #     print(solve(s))






# # Cradle Point
# # ///////////////
# # # import requests
# # # import mysql.connector
# # # import pandas as pd
# # """
# # Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
# # """
# # """
# # Example 1:

# # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# # Output: [[1,6],[8,10],[15,18]]
# # Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# # Example 2:

# # Input: intervals = [[1,4],[4,5]]
# # Output: [[1,5]]
# # Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# # Constraints:

# # 1 <= intervals.length <= 104
# # intervals[i].length == 2
# # 0 <= starti <= endi <= 104
# # """
# # # print('Hello')


# # """

# # 2     4     6    7
# #    3     5
# # """

# # def solve(arr):
# #     n = len(arr)
# #     arr.sort()
# #     left = arr[0][0]
# #     i = 1
# #     right = arr[0][1]
# #     result = []
# #     for start, end in arr[1:]:
# #         if start>right:
# #             result.append([left, right])
# #             left = start
# #         right = max(right, end)
# #     result.append([left,right])
# #     # print(result)
# #     return result

# # print(solve([[1,3],[2,6],[8,10],[15,18]])==[[1,6],[8,10],[15,18]])
# # print(solve([[1,4],[4,5]])==[[1,5]])





