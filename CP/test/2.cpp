#include<bits/stdc++.h>
using namespace std;
const int mxn = 1e5+2;

vector<int> graph[mxn];
int n, res[mxn];
char a[mxn];

vector<int> dfs(int s, int par){
    vector<int> vec(26,0);
    for(auto i: graph[s]){
        if (i!=par){
            vector<int> child = dfs(i,s);
            for(int i=0; i<26; ++i)
                vec[i]+=child[i];
        }
    }
    vec[a[s-1]-'a']++;
    res[s-1]=vec[a[s-1]-'a'];
    return vec;
}
void solve(){
    cin>>n;
    for(int i=0; i<n; ++i) {
        cin>>a[i];
        graph[i].clear();
    }
    graph[n].clear();
    int u,v;
    for(int i=0; i<n-1; ++i){
        cin>>u>>v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dfs(1,-1);
    for (int i = 0; i<n; ++i){
        cout<<res[i]<<" ";
    }
    cout<<"\n";
}

int main(){
    int t = 1;
    cin>>t;
    while(t-->0)
        solve();
    return 0;
}
