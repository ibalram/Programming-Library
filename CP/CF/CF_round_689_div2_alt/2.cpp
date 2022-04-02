#include"bits/stdc++.h"
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 502;

int n, m;
int mat[mxn][mxn];

void solve(){
    cin>>n>>m;
    char x;
    for(int i =0; i<n; ++i)
        for (int j =0; j<m; ++j){
            cin>>x;
            mat[i][j] = (x=='*'?1:0);
        }
    for(int k=0; k<n;++k){
        for(int i =0; i<n; ++i){
            for (int j =0; j<m; ++j){
                int f = 1;
                if(mat[i][j]>0){
                    for (int l=0;l<=mat[i][j];++l){
                        int xx = l,yy = mat[i][j]-l;
                        if (mat[i-xx][j-yy]<=0 or mat[i-xx][i+yy]<=0){
                            f = 0;break;
                        }
                    }
                }
                if (f){
                    mat[i][j]+=1;
                }
            }
        }
    }

}

int main(){
    freopen("in.txt","r",stdin);
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}
