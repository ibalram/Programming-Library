"""
# n = 7
# arr = [100, 180, 260, 310, 40, 535, 695]
# output = [5, 7, 655]

# [100, 180, 260, 310, 40, 535, 695]
#             buy  50  -220  275
# 695-100 = 595
# 695-180 = 515
# 695-260 = 435
# 695-310 =
# 695-40 = 655 -> max

"""

INF = float("inf")
def solve(arr):
    if len(arr)<2:
        return [-1,-1,-INF]
    n = len(arr)
    maximumOnRight = [-1]*n
    for i in range(n-2,-1,-1):
        maximumOnRight[i] = maximumOnRight[i+1]
        if maximumOnRight[i]==-1:
            maximumOnRight[i] = i+1
        elif arr[maximumOnRight[i]]<arr[i+1]:
            maximumOnRight[i] = i+1
    buyDay, sellDay, maxProfit = -1,-1,-INF
    # print(maximumOnRight)
    for i in range(n-1):
        if arr[maximumOnRight[i]] - arr[i]> maxProfit:
            maxProfit = arr[maximumOnRight[i]] - arr[i]
            buyDay = i
            sellDay = maximumOnRight[i]
    # print(maxProfit)
    return [buyDay+1, sellDay+1, maxProfit]

# Time Complexity = O(n)
# Aux. Space Complexity = O(n)
# print(solve([100, 180, 260, 310, 40, 535, 695]) == [5, 7, 655])
# print(solve([500, 400, 300, 250, 100]) == [3, 4, -50])




"""
Book -> (
id: Number
book_name: Char

)

Author->(
id: Number
Name:
Books:

)


Book -> many author
Author -> many books

select * from Book where author="Balram";



From Sandeep to Everyone:  03:32 PM
// Consider two services A and B, A making a certain API call to B. We need to deploy a new version of B with the updated API response body. New version of Service A needs to be deployed as well so it can consume the new response. How do we deploy both the services? Is this a breaking change, how can it be handled?
From Sandeep to Everyone:  03:39 PM
// Given is the list of stock prices for a company on consecutive days. Find the max profit one can make by buying on a day and selling on some later day. Return buy day, sell day, max proift. Buy/sell operation happens exactly once.
// 7, [100, 180, 260, 310, 40, 535, 695]
// [5, 7, 655]
From Me to Everyone:  03:40 PM
n = 7[100, 180, 260, 310, 40, 535, 695]
// [5, 7, 655]
From Sandeep to Everyone:  03:45 PM
brb
From Me to Everyone:  03:47 PM
Hi
Am I audible
?
From Sandeep to Everyone:  04:07 PM
Book, Author
get all books written by an author



"""
