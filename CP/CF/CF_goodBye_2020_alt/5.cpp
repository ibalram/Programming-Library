#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

int n;
ll a[500001];
int w[61];
void solve(){
    memset(w,0,sizeof(w));
    cin>>n;
    for(int i=0;i<n;i++){
        scanf("%lld",&a[i]);
        for(int j=0;j<=60;j++){
            if((a[i]>>j)&1ll)
                w[j]++;
        }
    }
    ll res=0;
    for(int i=0;i<n;i++){
        ll x=0,y=0;
        for(int j=0;j<=60;j++){
            ll tmp=(1ll<<j)%mod;
            if((a[i]>>j)&1ll){
                x=(x+tmp*n)%mod;
                y=(y+tmp*w[j])%mod;
            }
            else
                x=(x+tmp*w[j])%mod;
        }
        res=(res+x*y)%mod;
    }
    printf("%lld\n", res);
}

int main(){
    // freopen("in.txt","r",stdin);
    // ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}
