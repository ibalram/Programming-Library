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


from math import factorial as fac

s1 = input().strip()
s2 = input().strip()
s = input().strip()

mark = defaultdict(lambda:-1)
rng = range(10)
rang = range(1,10)
def rec(i,j,k,carry):
    if i<0 and j<0 and k<0:
        return carry==0
    elif i<0 and j<0:
        if carry==0: return False
        if mark[s[0]]!=-1:
            return mark[s[0]]==carry
        else:
            mark[s[0]]=carry
            return True
    elif i<0 or j<0:
        if i<0:
            if mark[s2[j]]!=-1 and mark[s[k]]!=-1:
                x = mark[s2[j]]
                y = mark[s[k]]
                if y==0 and k==0 or x==0 and j==0:
                    return False
                nC = (x+carry)//10
                if y != (x+carry)%10:
                    return False
                return rec(i,j-1,k-1,nC)
            if mark[s2[j]]!=-1:
                x = mark[s2[j]]
                if j==0 and x==0: return False
                for l in rng:
                    if l==0 and k==0:continue
                    nC = (x+carry)//10
                    if (carry+x)%10==l:
                        mark[s[k]]=l
                        if rec(i,j-1,k-1,nC):return True
                        mark[s[k]]=-1
            if mark[s[k]]!=-1:
                y = mark[s[k]]
                if k==0 and y==0: return False
                for l in rng:
                    if l==0 and j==0:continue
                    nC = (l+carry)//10
                    if (carry+l)%10==y:
                        mark[s2[j]]=l
                        if rec(i,j-1,k-1,nC):return True
                        mark[s2[j]]=-1
            else:
                if k==0 and y==0: return False
                for l in rng:
                    if l==0 and j==0:continue
                    for m i in rng:
                        if m==0 and k==0:continue
                        nC = (l+carry)//10
                        if (carry+l)%10==m:
                            mark[s2[j]]=l
                            mark[s[k]]=m
                            if rec(i,j-1,k-1,nC):return True
                            mark[s2[j]]=-1
                            mark[s[k]]=-1
        else:
            if mark[s1[i]]!=-1 and mark[s[k]]!=-1:
                x = mark[s1[i]]
                y = mark[s[k]]
                if y==0 and k==0 or x==0 and i==0:
                    return False
                nC = (x+carry)//10
                if y != (x+carry)%10:
                    return False
                return rec(i-1,j,k-1,nC)
            if mark[s1[i]]!=-1:
                x = mark[s1[i]]
                if i==0 and x==0: return False
                for l in rng:
                    if l==0 and k==0:continue
                    nC = (x+carry)//10
                    if (carry+x)%10==l:
                        mark[s[k]]=l
                        if rec(i-1,j,k-1,nC):return True
                        mark[s[k]]=-1
            if mark[s[k]]!=-1:
                y = mark[s[k]]
                if k==0 and y==0: return False
                for l in rng:
                    if l==0 and i==0:continue
                    nC = (l+carry)//10
                    if (carry+l)%10==y:
                        mark[s1[i]]=l
                        if rec(i-1,j,k-1,nC):return True
                        mark[s1[i]]=-1
            else:
                if k==0 and y==0: return False
                for l in rng:
                    if l==0 and i==0:continue
                    for m i in rng:
                        if m==0 and k==0:continue
                        nC = (l+carry)//10
                        if (carry+l)%10==m:
                            mark[s2[j]]=l
                            mark[s[k]]=m
                            if rec(i-1,j,k-1,nC):return True
                            mark[s2[j]]=-1
                            mark[s[k]]=-1
    else:
        if mark[s2[j]]!=-1 and mark[s[k]]!=-1:
                x = mark[s2[j]]
                y = mark[s[k]]
                if y==0 and k==0 or x==0 and j==0:
                    return False
                nC = (x+carry)//10
                if y != (x+carry)%10:
                    return False
                return rec(i,j-1,k-1,nC)
            if mark[s2[j]]!=-1:
                x = mark[s2[j]]
                if j==0 and y==0: return False
                for l in rng:
                    if l==0 and k==0:continue
                    nC = (x+carry)//10
                    if (carry+x)%10==l:
                        mark[s[k]]=l
                        if rec(i,j-1,k-1,nC):return True
                        mark[s[k]]=-1
            if mark[s[k]]!=-1:
                y = mark[s[k]]
                if k==0 and y==0: return False
                for l in rng:
                    if l==0 and j==0:continue
                    nC = (l+carry)//10
                    if (carry+l)%10==y:
                        mark[s2[j]]=l
                        if rec(i,j-1,k-1,nC):return True
                        mark[s2[j]]=-1
            else:
                if k==0 and y==0: return False
                for l in rng:
                    if l==0 and j==0:continue
                    for m i in rng:
                        if m==0 and k==0:continue
                        nC = (l+carry)//10
                        if (carry+l)%10==m:
                            mark[s2[j]]=l
                            mark[s[k]]=m
                            if rec(i,j-1,k-1,nC):return True
                            mark[s2[j]]=-1
                            mark[s[k]]=-1

        return mark[s[0]]==carry+mark[s[]]
