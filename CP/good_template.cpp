#include <bits/stdc++.h>
using namespace std;

//Utility functions
#define pb push_back
#define sz size()
#define fi first
#define se second
#define all(c) (c).begin(),(c).end()

//Constants
#define EPS 1e-6
#define INF 2e9

//Printing
#define coutRV(a,L,R) FE(i,L,R) cout<<a[i]<<" \n"[i==R] ;
#define coutV(a) coutRV(a,1,a.size()-1)

//For loops
#define FE(i,a,b)  for(int i=a; i<=b; i++)
#define FRE(i,b,a) for(int i=b; i>=a; i--)
#define FA(x,cont) for(auto& x : cont)

//For debug
void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

//Definitions
#define ll long long
#define ld long double
#define vi vector<int>
#define vll vector<ll>
#define vd vector<double>
#define vvi vector<vector<int> > //For UnGraph
#define vvpi vector<vector<pii> > //For DirGraph
#define vviwv(vecname, N, M, value) vector<vector<int> > vecname(N, vector<int> (M, value)) //For DP
#define vvlwv(vecname, N, M, value) vector<vector<ll> > vecname(N, vector<ll> (M, value)) //For DP
#define pii pair<int,int>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

//Input
#define cini(i) int i; cin>>i;
#define cini2(i,j) int i,j; cin>>i>>j;
#define cini3(i,j,k) int i,j,k; cin>>i>>j>>k;
#define cini4(i,j,k,l) int i,j,k,l; cin>>i>>j>>k>>l;
#define cinll(l) ll l; cin>>l;
#define cind(d) double d; cin>>d;
#define cins(s) string s; cin>>s; s = "#"+s;
#define cinv(a, n) vi a(n+1); FE(i,1,n) { cin>>a[i]; }
#define cinvd(a, n) vd a(n+1); FE(i,1,n) { cin>>a[i]; }
#define cinvll(a, n) vll a(n+1); FE(i,1,n) { cin>>a[i]; }

void solve()
{
    ll w, n;
    cin>>w>>n;
    vll x(w,0);

    FE(i,0,w-1)
        cin>>x[i];

    function<ll(ll)> cost = [&](ll st)
    {
        ll moves = 0;
        FE(i, 0, w-1)
        {
            if(st > x[i])
            {
                moves += min(st-x[i], x[i]+n-st);
            }
            else if(st < x[i])
            {
                moves += min(x[i]-st, n-x[i]+st);
            }
        }
        return moves;
    };

    ll l = 1, r = n;

    while(r-l>=3)
    {
        ll mid1 = l + (r-l)/3;
        ll mid2 = r - (r-l)/3;

        ll c1 = cost(mid1);
        ll c2 = cost(mid2);
        if( c1 < c2)
            r = mid2;
        else
            l = mid1;
    }
    if(l==r)
        cout<< cost(l)<<"\n";
    else if (l+1==r)
        cout<<min(cost(l), cost(r))<<"\n";
    else
        cout<<min(cost(l), min(cost(l+1), cost(l+2)))<<"\n";
    return;
}

int main()
{
    fastIO;
    cini(t);
    FE(i,1,t)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
