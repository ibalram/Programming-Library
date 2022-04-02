
# O(2^(n+m))
# O(n*m)
def lcsRecursiveBruteForce(a,b):
    n = len(a)
    m = len(b)
    def rec(i,j):
        if i>=n or j>=m:
            return 0
        return max(rec(i+1,j),rec(i,j+1), a[i]==b[j] and (1+rec(i+1,j+1)))
    return rec(0,0)

# O(n*m)
# O(n*m)
def lcsRecursiveMemoize(a,b):
    n = len(a)
    m = len(b)
    dp = [[-1]*(m+1) for i in range(n+1)]
    def rec(i,j):
        if i>=n or j>=m:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j] = max(rec(i+1,j),rec(i,j+1), a[i]==b[j] and (1+rec(i+1,j+1)))
        return dp[i][j]
    return rec(0,0)

# O(n*m)
# O(n*m)
def lcsRecursiveLRUCache(a,b):
    n = len(a)
    m = len(b)
    from functools import lru_cache
    @lru_cache(None)
    def rec(i,j):
        if i>=n or j>=m:
            return 0
        return max(rec(i+1,j),rec(i,j+1), a[i]==b[j] and (1+rec(i+1,j+1)))
    return rec(0,0)


# O(n*m)
# O(n*m)
def lcsBottomUpDP(a,b):
    n = len(a)
    m = len(b)
    dp = [[0]*(m+1) for i in range(n+1)]
    mx = 0
    idx = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][m]


# O(n*m)
# O(m)
def lcsBottomUpSpaceOptimizedDP(a,b):
    n = len(a)
    m = len(b)
    dp = [[0]*(m+1) for i in range(2)]
    mx = 0
    idx = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i%2][j] = 1+dp[(i-1)%2][j-1]
            else:
                dp[i%2][j] = max(dp[i%2][j-1], dp[(i-1)%2][j])
    return dp[n%2][m]


print(lcsBottomUpSpaceOptimizedDP("2365432", "1345"))
