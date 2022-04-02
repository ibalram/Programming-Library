#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

ll n;
ll w[300005];
vector<pair<int,ll>>gr[300005];

pair<ll, ll> dfs(int s, int par=-1){
    ll childmx, childres, res = 0;
    vector<ll> mxls;
    for (auto pr: gr[s]){
        if (pr.first==par) continue;
        auto child = dfs(pr.first,s);
        childmx = max(child.first-pr.second, 0LL);
        childres = child.second;
        res = max(res, childres);
        if (mxls.size()<2) mxls.push_back(childmx);
        else{
            ll mn = *min_element(mxls.begin(), mxls.end());
            if (mn<childmx)
                mxls[find(mxls.begin(), mxls.end(), mn)-mxls.begin()] = childmx;
        }
    }
    if (mxls.size()==0)
        return {w[s],w[s]};
    ll maxx = *max_element(mxls.begin(), mxls.end());
    ll summ = accumulate(mxls.begin(), mxls.end(), 0LL);
    return {max(maxx,0LL)+w[s],max(res,summ+w[s])};
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    cin>>n;
    ll x, y, c;
    for (int i = 1; i<=n; ++i) cin>>w[i];
    for (int i = 1; i<n; ++i){
        cin>>x>>y>>c;
        gr[x].push_back({y,c});
        gr[y].push_back({x,c});
    }
    auto res = dfs(1,-1);
    cout<<res.second<<endl;
    return 0;
}



/*
maxn = 1e5+5
res = [0]*(maxn)
a = [3,6,2,7,2,6]
for i in a:
    res[i]+=1
for i in range(1,maxn):
    for j in range(i,maxn,i):
        res[i]+=res[j]
    res[i] = res[i]*(res[i]-1)//2
for i in range(maxn,0,-1):
    for j in range(2*i, maxn, i):
        res[i]-=res[j]
for i in range(1,maxn):
    if res[i]==0:
        print(i)
        break
*/
