#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

bool cmp(int a, int b){
    if (a%2==0 and b%2==1){
        if (a%5==0 and b%5!=0)
    }
}
void solve(){
    int n;
    int arr[n];
    for(int i=0; i<n; ++i){
        cin>>arr[i];
    }
    sort(arr, arr+n, cmp);
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
