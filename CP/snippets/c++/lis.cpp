#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const ll mod = 1e9+7;
const int mxn = 2e5+2;


// time: O(nlogn)
// space: O(n)
int strictlyIncreLIS(int n, int a[]){
    vector<int> v;
    for (int i = 0; i < n; i++) {
        auto it = lower_bound(v.begin(), v.end(), a[i]);
        if (it != v.end()) *it = a[i];
        else v.push_back(a[i]);
    }
    return v.size();
}

int nonDecreLIS(int n, int a[]){
    vector<int> v;
    for (int i = 0; i < n; i++) {
        auto it = upper_bound(v.begin(), v.end(), a[i]);
        if (it != v.end()) *it = a[i];
        else v.push_back(a[i]);
    }
    return v.size();
}


void solve(){
}

int main(){
    freopen("in.txt", "r", stdin);
    // ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
