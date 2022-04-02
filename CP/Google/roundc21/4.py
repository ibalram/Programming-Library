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

t = int(input())
# x = int(input())
from random import randint

def solve(a,b,op):
    try:
        xx = int(front)
        xy = int(back)
        if op=="*":
            return a*b
        if op=="+":
            return a+b
        return str(a)+"#"+str(b)
    except ValueError:
        if op=="*" and 0 in (a,b):return 0
        elif op=="*" and a==1: return b
        elif op=="*" and b==1: return a
        a = str(a)
        b = str(b)
        return a+op+b if a<=b else b+op+a


for _ in range(1,t+1):
    n = int(input())
    classes = set()
    sortd = []
    for __ in range(n):
        s = input().strip()
        stack = []
        i = 0
        while i<len(s):
            if s[i] in "(":
                # stack.append(s[i])
                i+=1
                continue
            if s[i].isdigit():
                x = ""
                while i<len(s) and s[i].isdigit():
                    x+=s[i]
                    i+=1
                # if stack:
                #     op = stack.pop()
                #     # print(op,int(x),s)
                #     back = stack.pop()
                stack.append(int(x))
                # stack.append(int(s[i]))
            elif s[i] in ")":
                front = stack.pop()
                op = stack.pop()
                back = stack.pop()
                stack.append(solve(front,back,op))
                i+=1
            else:
                stack.append(s[i])
                i+=1
        sortd.append(stack)

    print("Case #{}: {}".format(_, sortd))
