#include<bits/stdc++.h>
using namespace std;
int main(){
    auto x=1000000;
    auto lambda = [](auto x){ return 1LL*x*x;};
    cout<<lambda(x)<<" "<<"YES"<<endl;
    for (auto i =0; i<13;++i){
        // cout<<i<<endl;
    }
    return 0;
}
