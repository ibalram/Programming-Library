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

# x = ilist()
# n = x[0]
# a = x[1:]
# def findMaxProfit(numOfPredictedDay, predictedSharePrices):
#     rightMax = predictedSharePrices[:]
#     for i in range(numOfPredictedDay-2,-1,-1):
#         rightMax[i] = max(rightMax[i], rightMax[i+1])
#     maxProfit = -1
#     for i in range(numOfPredictedDay-1):
#         maxProfit = max(maxProfit, rightMax[i+1]-predictedSharePrices[i])
#     return maxProfit
# print(findMaxProfit(n,a))

# def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
#     maxProfit = 0
#     for i in range(numOfPredictedTimes-1):
#         maxProfit += max(0, predictedSharePrices[i+1]-predictedSharePrices[i])
#     return maxProfit
# print(findMaxProfit(n,a))

# n,d = imap()
# a = ilist()
# b = [int(input()) for i in range(d)]

# def find_min_days(prices, profit):
#     import bisect
#     n = len(prices)
#     d = len(profit)
#     mp = {}
#     for i in range(n):
#         if prices[i] in mp:
#             mp[prices[i]].append(i)
#         else:
#             mp[prices[i]] = [i]
#     res = [[-1,n] for i in range(d)]
#     for j in range(d):
#         x = profit[j]
#         for i in range(n):
#             y = x+prices[i]
#             if y not in mp: continue
#             idx = bisect.bisect_right(mp[y], i)
#             if idx>=len(mp[y]): continue
#             endDay = mp[y][idx]+1
#             if res[j][1]>=endDay:
#                 res[j] = [i+1, endDay]
#         if res[j][0]==-1:
#             res[j] = "-1"
#         else:
#             res[j] = "{} {}".format(*res[j])
#     return ",".join(res)
# print(find_min_days(a,b))


n,m = imap()
p = list(map(float, input().split()))
x = list(map(float, input().split()))
y = list(map(float, input().split()))

def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):
    a = [x[i]*p[i]-y[i]*(1-p[i]) for i in range(noOfTradesAvailable)]
    q = [1.0-i for i in p]
    print(p)
    print(q)
    a.sort()
    res = 0
    for i in range(noOfTradesAvailable-1,max(-1,noOfTradesAvailable-maximumTradesAllowed-1) ,-1):
        print("DSF")
        res += max(0,a[i])
    return "{0:.2f}".format(res)

print(maximumExpectedMoney(n,m,p,x,y))
