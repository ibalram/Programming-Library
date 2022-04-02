#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;


ll dp[301][301][301];
int n;
int a[301], b[301], X,Y;
ll rec(int i, int A, int B){
    if (i>=n){
        if (A>=X && B>=Y) return 0;
        return mod;
    }
    if (dp[i][A][B]!=-1){
        return  dp[i][A][B];
    }
    dp[i][A][B] = min(1L+rec(i+1,min(X, A+a[i]), min(Y,B+b[i])), rec(i+1,A,B));
    return dp[i][A][B];
}

void solve(){
    cin>>n>>X>>Y;
    for(int i = 0; i<n; ++i){
        cin>>a[i]>>b[i];
    }
    for(int i = 0; i<=n; ++i){
        for(int j = 0; j<=300; ++j)
            for(int k = 0; k<=300; ++k)
                dp[i][j][k] = -1;
    }
    ll res = rec(0,0,0);
    if (res<mod){
        cout<<res<<"\n";
    }
    else{
        cout<<-1<<"\n";
    }


}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else

    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
