#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;


void solve(){
    int n;
    string s,x;
    cin>>n;
    cin>>s;
    cin>>x;

    int dp[n+5][11];
    memset(dp,-1,sizeof(dp));
    function<int(int,int)> rec = [&](int idx, int num){
        if (idx==n-1){
            int nw = num*10;
            if (x[idx]=='A')
                return (nw%7!=0 | (nw+s[idx]-'0')%7!=0);
            else
                return (nw%7==0 | (nw+s[idx]-'0')%7==0);
        }
        int res = 0;
        if (dp[idx][num]!=-1) return dp[idx][num];
        for (auto nxt:{0,s[idx]-'0'}){
            if (x[idx+1]!=x[idx])
                res|=1^rec(idx+1, (num*10+nxt)%7);
            else
                res|=rec(idx+1, (num*10+nxt)%7);
        }
        dp[idx][num] = int(res);
        return dp[idx][num];
    };
    int chk = rec(0,0);
    if (x[0]=='A')
        cout<<(chk?"Aoki":"Takahashi")<<endl;
    else
        cout<<(chk==0?"Aoki":"Takahashi")<<endl;

}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
