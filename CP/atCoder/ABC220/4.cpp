#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 998244353L;
const int mxn = 2e5+2;

// def rec(i,sm, k):
//     if i>=n:
//         return sm==k
//     if dp[i][sm]!=-1:
//         return dp[i][sm]
//     dp[i][sm] = (rec(i+1,(sm+a[i])%10, k)%mod+rec(i+1,(sm*a[i])%10, k)%mod)%mod
//     return dp[i][sm]
// for i in range(10):
//     dp = [[-1]*10 for i in range(n+1)]
//     ans[i] = rec(1,a[0],i)
// print(*ans, sep="\n")

ll dp[100005][11];
int n;
ll a[100005];

ll rec(int i, int sm, int k){
    if (i>=n)
        return (sm==k)*1L;
    if (dp[i][sm]!=-1)
        return dp[i][sm];
    dp[i][sm] = (rec(i+1, (sm+a[i])%10, k)%mod+rec(i+1,(sm*a[i])%10, k)%mod)%mod;
    return dp[i][sm];
}
void solve(){
    cin>>n;
    for (int i = 0; i<=n; i++){
        if (i<n)cin>>a[i];
        for (int j = 0; j<=10; j++){
            dp[i][j] = -1;
        }
    }
    for(int j = 0; j<10; ++j){
        cout<<rec(1,a[0],j)<<"\n";
        for (int _i = 0; _i<=n; _i++){
            for (int _j = 0; _j<=10; _j++){
                dp[_i][_j] = -1;
            }
        }
    }

}

int main(){
    // if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    // else
        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
