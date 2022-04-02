#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

ll n, m;
const int N = 1e6+3;
ll a[N], b[N], d[N];
vll v[N], rev[N], g;
map <string, ll> ma;

void solve(){
        cin >> n;
        for(int i = 1; i <= n; i++){
            cin >> x;
            x = d[x];
            b[i] = x;
            a[x]++;
        }
        x = 0, z = 0;
        for(int i = 1; i <= n; i++){
            x = max(x, a[b[i]]);
            if(b[i] != 1 && a[b[i]] % 2 == 0) z += a[b[i]];
            if(b[i] != 1)a[b[i]] = 0;
        }
        y = x;
        a[1] += z;
        y = max(y, a[1]);
        a[1] = 0;
        g.clear();
        cin >> q;
        for(int i = 1; i <= q; i++){
            cin >> z;
            if(z == 0)cout << x;
            else cout << y;
            cout << endl;
        }
}

int main(){
    freopen("in.txt","r",stdin);
    // ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    // cin>>t;
    for(int i = 1; i <= 1000000; i++){
        if(d[i])continue;
        for(int j = 1; j * j * i <= 1000000; j++){
            d[j * j * i] = i;
        }
    }
    while(t-->0)
        solve();
    return 0;
}

ll gcd(ll a, ll b){
    while(b){
        a %= b;
        swap(a, b);
    }
    return a;
}
