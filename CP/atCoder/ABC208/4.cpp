#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

const ll INF = 999999999999999;

void solve(){
    int n, m;
    int i,j,k;
    cin>>n>>m;
    ll dist[n+1][n+1];
    for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                dist[i][j]=INF;
    int a,b,c;
    for (int i =0; i<m; ++i){
        cin>>a>>b>>c;
        dist[a][b] = c;
    }
    ll res = 0;
    for (k = 1; k <= n; k++) {
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                if (i==j){
                    continue;
                }
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                if (dist[i][j]<INF){
                    res+=dist[i][j];
                }
            }
        }
    }
    cout<<res<<"\n";
}

int main(){
 if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
 else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
 int t = 1;
 // cin>>t;
 while(t-->0) solve();
 return 0;
}
