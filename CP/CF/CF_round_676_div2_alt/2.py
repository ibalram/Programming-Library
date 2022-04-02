from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------


from collections import deque, defaultdict
for _ in range(int(input())):
    n = int(input())
    mat = [[]]
    for i in range(n):
        a = [0]+list(input().strip())
        mat.append(a)
    one = [mat[1][2], mat[2][1]]
    two = [mat[n][n-1], mat[n-1][n]]
    if len(set(one+two))==1:
        print(2)
        print(n,n-1)
        print(n-1,n)
    elif len(set(one))==1 and len(set(two))==1 and set(one)!=set(two):
        print(0)
    else:
        if one[0]==one[1]:
            if one[0]==two[0]:
                print(1)
                print(n,n-1)
            else:
                print(1)
                print(n-1,n)
        elif two[0]==two[1]:
            if two[0] == one[0]:
                print(1)
                print(1,2)
            else:
                print(1)
                print(2,1)
        else:
            print(2)
            if one[0]=="1":
                print(2,1)
            else:
                print(1,2)
            if two[0]=="0":
                print(n-1,n)
            else:
                print(n,n-1)
    # dx = [1,-1,0,0]
    # dy = [0,0,-1,1]
    # def bfs(sign):
    #     q = deque()
    #     q.append([0,0])
    #     vis = {(0,0):1}
    #     while q :
    #         x,y = q.popleft()
    #         if x==n-1 and y==n-1:
    #             return True
    #         for i in range(4):
    #             xx = x+dx[i]
    #             yy = y+dy[i]
    #             if 0<=xx<n and 0<=yy<n and (xx,yy) not in vis and mat[xx][yy] in [sign,"F"]:
    #                 q.append([xx,yy])
    #                 vis[(xx,yy)] = 1
    #     return False
    # # print(mat)
    # one = bfs("1")
    # zero = bfs("0")
    # # print(one,zero)
    # if not one and not zero:
    #     print(0)
    #     continue
    # if one and zero:
    #     res = [[1,2],[n,n-1]]
    #     print(len(res))
    #     for i in res:
    #         print(*i)
    #     continue
    # ones = []
    # zeros = []
    # if mat[0][1]!=mat[1][0]:
    #     ones += [[1,2],[2,1]]
    # if mat[-1][-2]!=mat[-2][-1]:
    #     zeros += [[n-1,n],[n,n-1]]
    # res = []
    # if one:
    #     if ones:
    #         for i,j in ones:
    #             if mat[i-1][j-1]=="1":
    #                 res.append([i,j])
    #     else:
    #         for i,j in zeros:
    #             if mat[i-1][j-1]=="1":
    #                 res.append([i,j])
    #     print(len(res))
    #     for i in res:
    #         print(*i)
    # else:
    #     if ones and zeros:

    #     if ones:
    #         for i,j in ones:
    #             if mat[i-1][j-1]=="0":
    #                 res.append([i,j])
    #     else:
    #         for i,j in zeros:
    #             if mat[i-1][j-1]=="0":
    #                 res.append([i,j])
    #     print(len(res))
    #     for i in res:
    #         print(*i)




