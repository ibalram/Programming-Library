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
# mod = int(1e9+7)

#1
# while True:
#     try:
#         x = input().strip()
#         if len(x):
#             print("NO", flush=True)
#         else:
#             break
#     except:
#         break




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

#2
x = str(int(input()))
while len(x)>1:
    res = 0
    for i in str(x):
        res+=int(i)
    x = str(res)
print(x)



import sys
sys.setrecursionlimit(10**5+10)
from types import GeneratorType
#use:- put @bootstrap overrecursive function
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack: return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack: break
                    call = stack[-1].send(call)
            return call
    return wrapped_function
