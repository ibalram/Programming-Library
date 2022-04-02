#include <bits/stdc++.h>
using namespace std;
const int mx = 1e5+5;
// const int mx2 = 1e6+5;
const long long mod = 1e9+7;

int n,q, v,w,T,N,M,sz,mx2;
// int a[mx];
// vector<int> g[mx];

pair<int,int> coord(int x){
    return {x/M,x%M};
}
int index(int x, int y){
    return x*M+y;
}

vector<int> ones;
int bfs(int st){
    queue<int> q;
    q.push(st);
    while(!q.empty()){
        int s = q.front();
        q.pop();

    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d %d",&n, &T);
    set<pair<int,int>> coords;
    for( int i=0; i<n; ++i){
        scanf("%d %d",&v, &w);
        N = 0,M=0;
        N = max(N,v);
        M = max(M,w);
        coords.insert({v-1,w-1});
    }
    unordered_set<int> marked;
    sz = N*M;
    assert(sz<=20);
    for(auto x: coords) marked.insert(index(x.first,x.second));
    mx2 = 1<<sz;
    int bits[sz];
    int res = INT_MAX;
    int count = 0;
    for (int i=1; i<mx2; ++i){
        ones.clear();
        int f = 0;
        int st = -1;
        for (int j=1; j<sz; ++j){
            bits[j] = i>>j&1;
            if(bits[j] && ! marked.find(j)){
                f = 1;
                break;
            }
            if (bits[j] ){
                ones.push_back(j);
                if(st==-1)st = j;
            }
        }
        if (f) continue;
        int sm = __builtin_popcount(i);
        if(sm<n) continue;
        for(auto x: ones){
            if (!bfs(x)){
                f = 1;
                break;
            }
        }
        if (!f){
            if
        }




    }
    return 0;
}
