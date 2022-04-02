// tribbonacci
// zs

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define X first
#define Y second
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;
ll n, k;
ll dp[500001][51];

// ll rec(ll i, ll k){
//     if (i==n) return 1;
//     ll &res = dp[i][k];
//     if (res!=-1)return dp[i][k];
//     res =0;
//     if(i+1<=n) res = (res+rec(i+1,k)%mod)%mod;
//     if (i+2<=n) res = (res+rec(i+2,k)%mod)%mod;
//     if (i+3<=n && k) res = (res+rec(i+3,k-1)%mod)%mod;
//     return res;
// }
void solve(){
    cin>>n>>k;
    for(int i=0; i<=n; i++){
        for(int j = 0; j<=k; j++){
            dp[i][j]=0;
        }
    }
    // cout<<rec(0,k)<<endl;
    for(int j =0; j<=k; j++) dp[0][j]=1;
    for(int i =1; i<=n; i++){
        for( int j =0; j<=k; j++){
            if (i>=1)
                dp[i][j] = (dp[i][j]+dp[i-1][j])%mod;
            if (i>=2)
                dp[i][j] = (dp[i][j]+dp[i-2][j])%mod;
            if (i>=3 and j>=1)
                dp[i][j] = (dp[i][j]+dp[i-3][j-1])%mod;
            // cout<<dp[i][j]<<" ";
        }
        // cout<<endl;
    }
    cout<<dp[n][k]<<endl;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}



// mod = int(1e9+7)
// for _ in range(int(input())):
//     n,k = map(int,input().split())
//     dp = [[-1]*(k+1) for i in range(n+1)]
//     @bootstrap
//     def rec(i,k):
//         if i==n:
//             yield 1
//         res = 0
//         if dp[i][k]!=-1:
//             yield dp[i][k]
//         if i+1<=n:
//             res += yield rec(i+1,k)
//             res%=mod
//         if i+2<=n:
//             res+= yield rec(i+2,k)
//             res%=mod
//         if i+3<=n and k:
//             res+=yield rec(i+3,k-1)
//             res%=mod
//         dp[i][k] = res
//         yield res
//     print(rec(0,k))


/*
6
7 3
4 2
3 3
7 1
2 3
500000 50


44
7
4
41
2
934580754
*/
