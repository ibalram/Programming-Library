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


def solve2(n,k):
    def check(k):
        digits = list(map(int,list(str(k))))
        m = len(digits)
        @lru_cache(None)
        def rec(idx, rem, flag):
            res = 0
            mx = digits[idx] if flag else 9
            if idx == m-1:
                for i in range(mx+1):
                    res+=(i%5==rem)
                return res
            for i in range(mx+1):
                mod = i%5
                cntrPart = (5+rem-mod)%5
                res += rec(idx+1, cntrPart, flag and i==mx)
            return res
        res = 0
        for i in range(digits[0]+1):
            mod = i%5
            cntrPart = (5-mod)%5
            res += rec(1, cntrPart, i==digits[0])
        return res
    l = n
    r = 10**12
    res = -1
    lst = 0
    while r-l>=0:
        mid = l+r>>1
        ans = check(mid)
        if ans==k:
            print(ans,mid)
            return mid
        if ans<=k:
            res = mid
            l = mid+1
        else:
            r = mid-1
    return res





def solve(n,k):
    mod = int(1e9+7)
    @lru_cache(None)
    def rec(s,index,smaller,mod1):
        if(index==len(s)):
            if(mod1==0): return 1
            return 0
        else:
            limit=9
            if(smaller): limit=int(s[index])
            initCount=0
            for i in range(limit+1):
                ns = 0
                if i>=int(s[index]):
                    ns=smaller
                initCount+=rec(s, index+1, ns,(mod1+i)%k)%mod
                initCount%=mod
            return initCount
    return rec(str(n),0,1,0)%mod


n = int(input())
k = int(input())
print(solve(n,k))



"""string tostring(long long n)
{
   string s;
   while(n!=0)
  {
      s+=(n%10)+'0';
      n/=10;
   }
    reverse(s.begin(), s.end());
    return s;
}

long long dp[12][2][83]; //dp[index][smaller][remainder]

//For integers, the sum of digits can't be greater than 82

long long k;

string s;

long long dp_solve(string & s,int index,bool smaller,int mod1)
{
 if(index==s.length())
 {
        if(mod1==0)
        {
            return 1;

         }
     return 0;

 }
  if(dp[index][smaller][mod1]!=-1)
      {
       return dp[index][smaller][mod1];

      }
    else
    {
        int limit=9;

        if(smaller)
        {
            limit=s[index]-'0';
        }
        long long init_count=0;

        for(int i=0;i<=limit;i++)
        {
            bool ns;
            if(i<s[index]-'0')
            {
                ns=0;
            }
            else
            {
                ns=smaller;
            }

            init_count+=dp_solve(s, index+1, ns,(mod1+i)%k);

        }


        dp[index][smaller][mod1]=init_count;
        return init_count;

    }

}
"""
