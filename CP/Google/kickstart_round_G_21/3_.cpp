#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const int mod = 1e7;
const int mxn = 2e5+2;

int n,k,b[5001],sm,res, parSum;
map<int,vector<int>>> a;
void solve(int test){
    cin>>n>>k;
    for(int i = 0; i<n; ++i)cin>>b[i];
    a.clear();
    res = mod;
    parSum = 0;
    for(int i = 0; i<n; ++i){
        parSum+=b[i];
        sm = parSum;
        for(int j = 0; j<=i; ++j){
            if (sm==k) res = min(res,i-j+1);
            // for(int l = 0; l<j; ++l){
            //     if (a[l].find(k-sm)!=a[l].end())
            //         res = min(res, i-j+1+a[l][k-sm]);
            // }
            if (a[i].find(sm)!=a[i].end())
                a[i][sm] = min(a[i][sm], i-j+1);
            else
                a[i][sm] = i-j+1;
            sm-=b[j];
        }
    }
    if (res==mod)res = -1;
    cout<<"Case #"<<test<<": "<<res<<endl;
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    cin>>t;
    for(int i = 1; i<=t; ++i)solve(i);
    return 0;
}
