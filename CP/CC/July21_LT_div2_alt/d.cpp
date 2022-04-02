#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;
const ll INF = (1<<63) -1;


ll t[4*mxn];
lazy[4*mxn];
int n;
void push(int v) {
    t[v*2] += lazy[v];
    lazy[v*2] += lazy[v];
    t[v*2+1] += lazy[v];
    lazy[v*2+1] += lazy[v];
    lazy[v] = 0;
}

void update(int v, int tl, int tr, int l, int r, int addend) {
    if (l > r)
        return;
    if (l == tl && tr == r) {
        t[v] = min(INF, t[v]+addend);
        // lazy[v] += addend;
        lazy[v] = min(INF, lazy[v]+addend);
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), addend);
        update(v*2+1, tm+1, tr, min(l, tm+1), r, addend);
        t[v] = min(t[v*2], t[v*2+1]);
    }
}

int query(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return INF;
    if (l <= tl && tr <= r)
        return t[v];
    push(v);
    int tm = (tl + tr) / 2;
    return min(query(v*2, tl, tm, l, min(r, tm)),
               query(v*2+1, tm+1, tr, min(l, tm+1), r));
}

void solve(){
    int n = 0;
    int q;
    cin>>q;
    ll p,x, res;
    // memset(t, 0xffff, sizeof(t));
    while(q-->0){
        cin>>p;
        if(p==1){
            cin>>x;
            n++;
            update(1, 1, maxn, n+1, n+1, x);
        }else if(p==2){
            cin>>x;
            update(1, 1, maxn, 1, n, x);
        }
        else{
            res = query(1, 1,maxn, 1, n);
            update(1, 1, maxn, n, n, INF);
        }
    }

}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
