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

# n = int(input())

# a = list(map(int,input().split()))

# pf = [0]+a[:]
# for i in range(1,n+1):
#     pf[i]+=pf[i-1]

# res = 0
# for i in range(0,n,2):
#     mn = float("inf")
#     cnt = 0
#     for j in range(i,n):
#         if j&1:
#             x = max(0,mn+1-max(cnt-a[j],0))
#             res+=min(x,a[j]-max(cnt,a[j]))
#             print(i,j,max(0,mn+1-max(cnt-a[j],0)), a[j])
#             cnt-=a[j]
#             if cnt<0:
#                 break
#         else:
#             cnt+=a[j]
#         mn = min(mn, cnt)
# print(res)







# """
# 4th round at Agoda
# # Problem: Find the n’th term in Look-and-say (Or Count and Say) Sequence. The look-and-say sequence is the sequence of below integers:

# # 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, …

# # The first term is "1"

# # Second term is "11", generated by reading first term as "One 1" (There is one 1 in previous term)

# # Third term is "21", generated by reading second term as "Two 1"

# # Fourth term is "1211", generated by reading third term as "One 2 One 1" and so on ...

# # Input: n = 3
# # Output: 21

# # Input: n = 5
# # Output: 111221

# """
# 13112221 => 1 1, 1 3, 2 1, 3 2, 1 1

# """

# # import sys
# # sys.setrecursion


# def recurse(n):
#     if n==1: return "1"
#     prevSequence= recurse(n-1)
#     m = len(prevSequence)

#     currentSequence = []
#     count = 1
#     for i in range(1, m):
#         if prevSequence[i]==prevSequence[i-1]:
#             count+=1
#         else:
#             currentSequence.append(str(count)+str(prevSequence[i-1]))
#             count = 1
#     currentSequence.append(str(count)+str(prevSequence[m-1]))
#     return "".join(currentSequence)

# def tailRecurse(n, idx, prevSequence):
#     if n==idx:
#         return prevSequence
#     m = len(prevSequence)
#     currentSequence = []
#     count = 1
#     for i in range(1, m):
#         if prevSequence[i]==prevSequence[i-1]:
#             count+=1
#         else:
#             currentSequence.append(str(count)+str(prevSequence[i-1]))
#             count = 1
#     currentSequence.append(str(count)+str(prevSequence[m-1]))
#     currentResult = "".join(currentSequence)
#     return tailRecurse(n,idx+1, currentResult)

# def solve(n):
#     if n==0: return ""
#     # return recurse(n)
#     return tailRecurse(n,1,"1")

# print(solve(5)=="111221")
# print(solve(8)=="1113213211")
# print(solve(0)=="")
# print(solve(1000))

# # n = 3
# # 2 1

# # n = 2
# # 1 1

# # 2 4 4 1 2 2 2


# """








# def SearchingChallange(str):
#     a = str.strip().split()
#     mx = 0
#     res = -1
#     for i in a:
#         mp = Counter(i)
#         cnt = 0
#         for k,v in mp.items():
#             cnt+=v>1
#         if cnt>mx:
#             mx = cnt
#             res = i
#     return res



# print(SearchingChallange("Hello apple pie"))
# print(SearchingChallange("No Words"))
# print(SearchingChallange("Today, is the greatest day ever!"))



def ArrayChallange(arr):
    childCount = {}
    nums = set()
    parent = {}
    for i in arr:
        u,v = map(int,i[1:-1].split(","))
        childCount[v] = childCount.get(v,0)+1
        if childCount[v]>2 or parent.get(u,v)!=v:
            return False
        parent[u] = v
        nums.add(u)
        nums.add(v)
    if sum(1 for i in nums iff i not in parent)>1:
        return False
    return True

print(ArrayChallange(["(1,2)", "(2,4)", "(5,7)", "(7,2)","(9,5)"]))
print(ArrayChallange(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))


# print(SearchingChallange("Hello apple pie"))
# print(SearchingChallange("No Words"))
# print(SearchingChallange("Today, is the greatest day ever!"))
