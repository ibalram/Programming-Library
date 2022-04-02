# https://leetcode.com/problems/powx-n/

"""
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104"""


"""
The naive idea of solution is to use n-time multiplication of x.
x^n = x*x*x*.....n-times
now we can see that x^20 = x^10*x^10 and x^21 = (x^10*x^10)*x.
so pow(x,n) = pow(x, n/2)*pow(x,n/2) if n is even otherwise
pow(x,n) = pow(x, n/2)*pow(x,n/2)*x
if we anayze this depth of this recursive function then it is atmost log2(n)
so Time: O(logn)
   Space: O(logn) if recursive but can be reduced to O(1) by using iterative approach

there are some edge cases that must be handled separetly:
x^0 = 1
0^n = 0


Time complexity: O(logn)
Space complexity: O(1)
`

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = n<0
        if x==0:
            return 0
        if n==0:
            return 1
        n = abs(n)
        res = 1
        while n>0:
            if n&1:
                res*=x
            x = x*x
            n>>=1
        if sign: res = 1/res
        return res




