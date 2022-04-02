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

inline bool exists (const std::string& name) {
    if (FILE *file = fopen(name.c_str(), "r")) {
        fclose(file);
        return true;
    }
    return false;
}

void solve(){
    int n = 0;
    // cin>>n;
    // cout<<n<<endl;
    cout<<(long long)pow(2,62)<<" "<<pow(2,62)<<" "<<(int64_t)pow(2,62)<<endl;
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
