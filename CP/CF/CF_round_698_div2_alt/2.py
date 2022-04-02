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

for _ in range(int(input())):
    from collections import Counter
    q,d = map(int,input().split())
    a = list(map(int,input().split()))
    for i in a:
        num = i
        # f = 0
        # while num:
        #     x = d
        #     while x%10!=num%10:
        #         x+=d
        #         if x>num:
        #             break
        #     if x%10==num%10 and x<=num:
        #         f = 1
        #         break
        #     num//=10
        # print(x)
        # cnt = 0
        # while num:
        #     x = num%10 - d
        #     if x>=0:
        #         cnt+=1
        #     if x%d==0:
        #         cnt+=1
        #     num//=10
        # print("YES" if cnt>=2 else "NO")
        f = 0
        res = "NO"
        while num>0:
            tm = num
            while tm>0:
                r = tm%10
                if r==d:
                    f = 1
                    break
                tm//=10
            if f==1:
                print("YES")
                break
            num-=d
        if f==0:
            print("NO")
