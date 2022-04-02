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

vector<pair<int,ll>> gr[mxn];
int anc[mxn][20];
int level[mxn];
ll psum[mxn];

int n,q,r;

void dfs(int s,int par){
    for (int i=1; i<20; i++)
        anc[s][i] = anc[anc[s][i-1]][i-1];
    for(auto ent:gr[s]){
        int i = ent.X;
        ll w = ent.Y;
        if (i==par)continue;
        psum[i] = psum[s]+w;
        level[i] = level[s]+1;
        anc[i][0] = s;
        dfs(i,s);
    }
}

int lca(int u, int v){
    if (level[u]>level[v]) swap(u,v);
    for (int i=19; i>=0; i--){
        if (level[v] - (1<<i) >= level[u]) v = anc[v][i];
    }
    if (u==v)return u;
    for (int i=19; i>=0; i--){
        if (anc[u][i]!=anc[v][i]){
            u = anc[u][i];
            v = anc[v][i];
        }
    }
    return anc[u][0];
}

ll pathsum(int u, int v){
    int lc = lca(u,v);
    return psum[u]+psum[v]-2*psum[lc];
}


void solve(){
    cin>>n>>q>>r;
    for( int i =0 ; i<=n; ++i){
        for( int j = 0; j<=20; ++j)
            anc[i][j] = -1;
        gr[i].clear();
        psum[i] = 0;
    }
    int u,v;
    ll w;
    for (int i =0 ; i<n-1; ++i){
        cin>>u>>v>>w;
        gr[u].push_back({v,w});
        gr[v].push_back({u,w});
    }
    level[r] = 0;
    dfs(r,-1);
    for(int i = 0; i<q; ++i){
        cin>>u>>v;
        cout<<pathsum(u,v)<<endl;
    }
}

int main(){
    // freopen("in.txt", "r", stdin);
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}
