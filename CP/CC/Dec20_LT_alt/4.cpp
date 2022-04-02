#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

int n,m,q;
int mat[202][202];
void printMset(auto mset){
    for (auto it: mset){
        cout<<it<<endl;
    }
}
void solve(){
    cin>>n>>m;
    vector<multiset<int, greater<int>>> mp(n+m, multiset<int, greater<int>>());
    for(int i = 0; i<n; ++i){
        for(int j=0; j<m; ++j){
            int k = m-j-1;
            cin>>mat[i][k];
            cout<<i<<" "<<k<<" "<<mat[i][k]<<endl;
            mp[i+k].insert(mat[i][k]);
            printMset(mp[i+k]);
        }
    }
    cin>>q;
    int x,y,z,k;
    for(int i = 0; i<q; ++i){
        cin>>x>>y>>z;
        x-=1;
        y = m-y;
        k = x+y;
        cout<<endl;
        mp[k].erase(mat[x][y]);
        printMset(mp[k]);
        mat[x][y] = z;
        mp[k].insert(z);
        printMset(mp[k]);
        cout<<k<<"-"<<mp[k].count(z)<<" "<<mp[k].size()<<endl;
        cout<<(mp[k].count(z)==mp[k].size()?"Yes":"No")<<"\n";
    }
}

int main(){
    freopen("in.txt","r",stdin);
    // ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}
