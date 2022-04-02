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




mod = int(10**9+21)
from math import cos,acos, asin, atan, radians, fmod
def power(x, y, p) :
    res = 1     # Initialize result
    # Update x if it is more
    # than or equal to p
    # x = fmod(x ,p)
    x = x%p
    if (x == 0) :
        return 0
    # return x**y if y else
    while (y > 0) :
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            # res = fmod(res * x ,p)
            res = res*x%p
        # y must be even now
        y = y >> 1      # y = y/2
        # x = fmod(x * x ,p)
        x = x*x%p
    return res
def Multiply (p, q, M):
    # Multiplication of two complex numbers is
    # (a + ib)(c + id) = (ac - bd) + i(ad + bc)
    # x = fmod(fmod(p[0] * q[0] , M)-fmod(p[1] * q[1] , M) + M , M)
    # y = fmod(fmod(p[0] * q[1] , M)+fmod(p[1] * q[0] , M) ,M)
    # x = fmod(p[0] * q[0]-p[1] * q[1]*3, M)
    # y = fmod(p[0] * q[1]+p[1] * q[0], M)
    x = (p[0] * q[0]-p[1] * q[1]*3)%M
    y = (p[0] * q[1]+p[1] * q[0])%M
    # Return the multiplied value
    return [x, y]
# Function to calculate the
# complex modular exponentiation
def compPow(complex, k, M):
    # Here, res is initialised to (1 + i0)
    res = [1, 0]
    while (k > 0):
        # If k is odd
        if (k & 1):
            # Multiply 'complex' with 'res'
            res = Multiply(res, complex, M)
        # Make complex as complex*complex
        complex = Multiply(complex, complex, M)
        # Make k as k/2
        k = k >> 1
    # Return the required answer
    return res[0]

a = 7**.5
theta = atan(cos(radians(30)))
# theta = acos(2/a)
sqrt3 = 3**.5
# print(acos(2/a))
def apow(x,y):
    # if x&1:
    #     return round(power(a,x, mod)*a*cos(y*theta))
    return round(power(a,x, mod)*cos(y*theta))
def trigo(n):
    n+=1
    if n==0:return 0
    res = round(a**(n+1)*cos((n-1)*theta))-round(a**n*cos(n*theta))-1#round(a*cos(theta))+1
    # res*=2
    # res/=a*a-2*a*cos(theta)+1
    res//=2
    n-=1
    # res+=(3*n*(4**(n+1))-4*(4**n-1))//9
    res+=(3*n*power(4, n+1, mod)-4*(power(4,n,mod)-1))*power(9,mod-2,mod)
    # res = fmod(power(a,n+1,mod)*cos((n-1)*theta),mod)-fmod(power(a,n,mod)*cos(n*theta), mod)- fmod(a*cos(theta), mod)+1+mod
    # # res*=2
    # res*=power(2,mod-2,mod)
    # res = fmod(res, mod)
    # n-=1
    # res+=((3*n%mod*(power(4,n+1,mod))%mod-4*(power(4,n,mod)-1)%mod)*power(9,mod-2,mod)%mod+mod)%mod
    # return fmod(res,mod)
    return res%mod

# for i in range(20,21):
#     print(i, 7**10,a**(i)*cos((i)*theta))
#     re = abs( (a**(i)*cos((i)*theta)))
#     print(re/(7**10))

# x = [2,1]
# from decimal import *
# getcontext().prec = 100

# for i in range(15,23):
#     print(compPow(x,i,mod), (a**i)*cos(Decimal(i*theta)))#fmod((a**i)*cos(i*theta)+mod,mod))

def trigo3(n):
    n+=1
    if n==0:return 0
    res = (a**(n+1))*cos((n-1)*theta)-(a**n)*cos(n*theta)-1#round(a*cos(theta))+1
    # res*=2
    # res/=a*a-2*a*cos(theta)+1
    res//=2
    # res = round(res)
    n-=1
    # res+=(3*n*(4**(n+1))-4*(4**n-1))//9
    res+=(3*n*(4**(n+1))-4*(4**n-1))//9

    # res = fmod(power(a,n+1,mod)*cos((n-1)*theta),mod)-fmod(power(a,n,mod)*cos(n*theta), mod)- fmod(a*cos(theta), mod)+1+mod
    # # res*=2
    # res*=power(2,mod-2,mod)
    # res = fmod(res, mod)
    # n-=1
    # res+=((3*n%mod*(power(4,n+1,mod))%mod-4*(power(4,n,mod)-1)%mod)*power(9,mod-2,mod)%mod+mod)%mod
    # return fmod(res,mod)
    return round(res)%mod

def trigo2(n):
    n+=1
    if n==0:return 0
    # res =round(a**(n+1)*cos((n-1)*theta))-round(a**n*cos(n*theta))-round(a*cos(theta))+1
    # res = apow(n+1, n-1)-apow(n, n)-apow(1,1)+1
    res = (7*compPow([2,1], n-1,mod)%mod-compPow([2,1], n,mod)-1+mod)%mod
    res*=power(2, mod-2,mod)
    res%=mod
    # res/=2
    n-=1
    res+=(3*n*power(4, n+1, mod)-4*(power(4,n,mod)-1))*power(9,mod-2,mod)
    # if n==1:
    #     res+=1
    return res%mod


for _ in range(int(input())):
    p,q = map(int,input().split())
    # print((trigo3(q)-trigo3(p-1)+mod)%mod)
    print((trigo2(q)-trigo2(p-1)+mod)%mod)

# print(sum(a))






"""
mod = int(1e9+21)
from math import acos, fmod
def power(x, y, p) :
    res = 1
    x = x%p
    if (x == 0) :
        return 0
    while (y > 0) :
        if ((y & 1) == 1) :
            res = res*x%p
        y = y >> 1
        x = x*x%p
    return res
def Multiply (p, q, M):
    x = (p[0] * q[0]-p[1] * q[1]*3)%M
    y = (p[0] * q[1]+p[1] * q[0])%M
    return [x, y]
def compPow(complex, k, M):
    res = [1, 0]
    while (k > 0):
        if (k & 1):
            res = Multiply(res, complex, M)
        complex = Multiply(complex, complex, M)
        k = k >> 1
    return res[0]

a = 7**.5
theta = acos(2/a)
sqrt3 = 3**.5

def trigo3(n):
    n+=1
    if n==0:return 0
    res = (a**(n+1))*cos((n-1)*theta)-(a**n)*cos(n*theta)-1
    res//=2
    n-=1
    res+=(3*n*(4**(n+1))-4*(4**n-1))//9
    return round(res)%mod

def trigo2(n):
    n+=1
    if n==0:return 0
    res = (7*compPow([2,1], n-1,mod)%mod-compPow([2,1], n,mod)-1+mod)%mod
    res*=power(2, mod-2,mod)
    res%=mod
    n-=1
    res+=(3*n*power(4, n+1, mod)-4*(power(4,n,mod)-1))*power(9,mod-2,mod)
    return res%mod



for _ in range(int(input())):
    p,q = map(int,input().split())
    print((trigo2(q)-trigo2(p-1)+mod)%mod)
"""
