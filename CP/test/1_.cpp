#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m,k;
    cin>>n>>m>>k;
    vector<int> a(n,0);
    unordered_set<int> b;
    for(int i=0; i<n;++i)cin>>a[i];
    int x;
    for(int i=0; i<m;++i){
        cin>>x;
        b.insert(x);
    }
    map<int,int> mp;
    int l=0,r=0;
    int res = 1<<30;
    while (l<n and r<n){
        if (b.count(a[r])){
            mp[a[r]]+=1;
        }
        while(l<n and (!b.count(a[l]) or mp.size()>k or mp.size()==k and mp[a[l]]>1)){
            if (b.count(a[l])){
                mp[a[l]]+=1;
                if(mp[a[l]]==0){
                    mp.erase(a[l]);
                }
            }
            l++;
        }
        if(mp.size()==k){
            res = min(res, r-l+1);
        }
        r++;
    }
    cout<<(res<(1<<30)?res:-1)<<"\n";
    return 0;
}
