#include "bits/stdc++.h"
using namespace std;
#define ll long long

int dp[502][502][502];
int main(){
    // ios::sync_with_stdio(0),cin.tie(0);
    // freopen("in.txt", "r", stdin);
    int t = 1;
    cin >> t;
    while(t-->0){
                int n,x;
        cin >> n >> x;
        int a[n+1],mx=x;
        for(int i=1;i<=n;i++){
            cin >> a[i];
            mx=max(mx,a[i]);
        }
        // cout << n << '\n';
        int inf=2e9;
        // memset(dp,-1,sizeof dp);
        for(int i=0;i<=n;i++){
            for(int j=0;j<=mx;j++){
                for(int k=0;k<=mx;k++){
                    dp[i][j][k] = -1;
                }
            }
        }
         dp[0][0][x]=0;
         for(int i=0;i<n;i++){
            for(int j=0;j<=mx;j++){
                for(int k=0;k<=mx;k++){
                    if(dp[i][j][k]==-1)continue;
                    if(a[i+1]>k and k>=j){
                        if(dp[i+1][k][a[i+1]]==-1)dp[i+1][k][a[i+1]]=inf;
                        dp[i+1][k][a[i+1]]=min(dp[i+1][k][a[i+1]],dp[i][j][k]+1);
                    }
                    if(a[i+1]>=j){
                        if(dp[i+1][a[i+1]][k]==-1)dp[i+1][a[i+1]][k]=inf;
                        dp[i+1][a[i+1]][k]=min(dp[i+1][a[i+1]][k],dp[i][j][k]);
                    }
                }
            }
         }
        int ans=inf;
         for(int i=0;i<=mx;i++){
            for(int j=0;j<=mx;j++){
                if(dp[n][i][j]==-1)continue;
                ans=min(dp[n][i][j],ans);
        }
         }
         if(ans==inf)ans=-1;
         cout << ans << '\n';
    }
    return 0;
}
