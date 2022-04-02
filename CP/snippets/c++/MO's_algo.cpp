// Mo's algorithm
// number of xor pairs in range query
//
// https://codeforces.com/contest/617/problem/E
// my submission:   https://codeforces.com/contest/617/submission/114194439

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;


int cnt[1<<20];
ll res[mxn], a[mxn], ans;
int n, m, k, block;
vector<array<int,3>> queries;
void update(int x, int add=1){
    if (add==1){
        ans += cnt[a[x]^k];
        cnt[a[x]]++;
    }
    else{
        cnt[a[x]]--;
        ans -= cnt[a[x]^k];
    }
}
int l=0, r=-1;

// [L,R]
ll solveQuery(int L, int R){
    while(l > L) update(--l);
    while(r < R) update(++r);
    while(l < L) update(l++,-1);
    while(r > R) update(r--, -1);
    return ans;
}

bool cmp(array<int,3>x, array<int,3> y){
    if (x[0]/block != y[0]/block)
        return x[0]<y[0];
    return x[1]<y[1];
}

void solve(){
    cin>>n>>m>>k;
    a[0] = 0;
    for(int i=1;i<=n;++i)cin>>a[i], a[i]^=a[i-1];
    int u,v;
    for(int i=0; i<m; ++i){
        cin>>u>>v;
        queries.push_back({--u,v,i});
    }

    block = sqrt(n);
    sort(queries.begin(), queries.end(), cmp);
    for(auto query: queries){
        res[query[2]] = solveQuery(query[0], query[1]);
    }
    for(int i=0; i<m; ++i){
        cout<<res[i]<<"\n";
    }

}

int main(){
    // if(FILE*f=fopen(string("in.txt").c_str(),"r"))fclose(f),freopen("in.txt","r",stdin);
    // else
        ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
