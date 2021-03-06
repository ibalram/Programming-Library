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

k = int(input())

def calc(n):
    if k==1:return n*(n+1)//2
    if k==2: return n*(n+1)*(2*n+1)//6
    if k==3:return (n*(n+1)//2)**2
    if k==4: return n*(n+1)*(2*n+1)*(3*n**2+3*n-1)//30

for _ in range(int(input())):
    n = int(input())
    a = [i**k for i in range(1,n+1)]
    # f = 0
    # sm = calc(n)
    # # if sm%2!=0:
    # #     f =1
    # # if f:
    # #     print(-1)
    # #     continue
    # sm//=2
    # def bs(x,i):
    #     l = 0
    #     r = i
    #     res = -1
    #     while r-l>=0:
    #         mid = l+r>>1
    #         if a[mid]<=x:
    #             res = mid
    #             l = mid+1
    #         else:
    #             r = mid-1
    #     return res
    # i = n-1
    # A = 0
    # B = 0
    # res = [0]*(n)
    # while i>=0:
    #     if A>=B:
    #         res[i] = 1
    #         B+=a[i]
    #     else:
    #         A+=a[i]
    #     i-=1
    res = [0]*n
    mn = float("inf")
    for i in range(1<<(n),-1,-1):
        sm = 0
        cur = [0]*n
        # print("yes")
        for j in range(n):
            if (i>>j)&1:
                sm+=a[j]
                cur[j] = 1
            else:
                sm-=a[j]
                cur[j] = 0
        sm = abs(sm)
        if sm<=mn:
            mn = sm
            res = cur[:]
    print(abs(sum(a[i] if res[i] else -a[i] for i in range(n))), end=" ")
    print("".join(map(str,res)))














"""
2
20
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
################33
1 0
3 01
4 001
2 0001
3 01001
1 101001
0 1101001
0 01101001
1 011000101
1 0100100101
0 10111000101
0 000000001101
1 0001000010011
1 11010000001011
0 110010000000111       0 1101001 10010110 1001011001101001
0 1010110000000111
1 10000000001000111
1 100100000000100111
0 1100000000000001111
0 00001100000000001111




#############33
####################
################





3
20
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

##########################
1 0
7 01
18 001
28 0001
25 00001
7 010001
26 1110001
4 11001001
5 100101001
1 1000000101
12 00001101001
0 110100011001
1 0000010000011
1 01011001101001
0 110000101000011
0 1001011001101001
1 11101001000001101
1 101100101010100101
0 0011001001011000011
0 10100000001000000111



###############3
#############33
############33
############33

4
24
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

###################33
1 0
15 01
64 001
158 0001
271 00001
317 000001
126 0000001
34 11010001
253 111110001
13 0101001001
92 00000101001
30 110010101001
47 0010110101001
31 11111110000101
2 100001110101001
0 1111000111110001
1 11010111100000011
13 111111001011110001
0 0111101101001000011
0 11110101001000100011
9 000000000100100100011
1 1010110000100000001011
0 11110111011001000010011
0 111101100001001000001011

"""
