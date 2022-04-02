#include<bits/stdc++.h>
#define endl "\n"
using namespace std;
int n,m,k;
int dp[71][71][71][71], mat[71][71];

int rec(int i, int j, int count, int rem){
    if (i>=n) return rem==0 ? 0 : INT_MIN;
    if (j>=m) return rec(i+1,0,0,rem);
    int &res = dp[i][j][count][rem];
    if(res!=-1) return res;
    res = max(rec(i+1,0,0,rem), rec(i,j+1,count, rem));
    if(count<m/2){
        res = max(res, mat[i][j]+rec(i,j+1, count+1, (rem+mat[i][j])%k));
    }
    return res;
}

void solve(){
    cin>>n>>m>>k;
    for(int i =0; i<n; ++i)
        for(int j =0; j<m; ++j)
            cin>>mat[i][j];
    memset(dp,-1,sizeof(dp));
    cout<<rec(0,0,0,0)<<endl;
}

int main(){
    // freopen("in.txt", "r", stdin);
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
