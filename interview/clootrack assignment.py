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



def solve(tweets):
    result = []
    mapp = dict()
    for user_name, tweet in tweets:
        mapp[user_name] = mapp.get(user_name, 0) + 1
    max_count = max(mapp.values())
    for user_name in sorted(mapp.keys()):
        if mapp[user_name] == max_count:
            result.append((user_name, max_count))
    return result


tests = int(input())
for _ in range(tests):
    n = int(input())
    tweets = []
    for i in range(n):
        tweets.append(input().split())
    result = solve(tweets)
    for user_name, count in result:
        print(user_name, count)

