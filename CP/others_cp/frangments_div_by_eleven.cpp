#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;




// int DivisibilityByEleven(int num){
//     int res = 0;
//     string s = to_string(num);
//     int n = s.size();
//     for (int i = 0; i<n; ++i){
//         int sm = 0;
//         int sign = 1;
//         for (int j = i; j<n; ++j){
//             sm+=sign*(s[j]-'0');
//             sign = -sign;
//             res+=sm%11==0;
//         }
//     }
//     return res;
// }



int DivisibilityByEleven(int num){
    int res = 0;
    int x = num;
    int n = 0;
    while(x>0){
        x/=10;
        n++;
    }
    int i = n;
    int s[n*sizeof(int)];
    while(num>0){
        i--;
        s[i] = num%10;
        num/=10;
    }
    for (int i = 0; i<n; ++i){
        int sm = 0;
        int sign = 1;
        for (int j = i; j<n; ++j){
            sm+=sign*(s[j]);
            sign = -sign;
            res+=sm%11==0;
        }
    }
    return res;
}



void solve(){
    cout<<DivisibilityByEleven(55)<<endl;
    cout<<DivisibilityByEleven(1215598)<<endl;
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int t = 1;
    // cin>>t;
    while(t-->0) solve();
    return 0;
}
