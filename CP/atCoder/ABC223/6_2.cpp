#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const int mod = 1e8;
const int mxn = 2e5+2;

#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

const int N = 5e5 + 9;
int a[N];
struct ST {
  #define lc (n << 1)
  #define rc ((n << 1) | 1)
  long long t[4 * N], lazy[4 * N];
  ST() {
    memset(t, 0xff, sizeof t);
    memset(lazy, 0xff, sizeof lazy);
  }
  inline void push(int n, int b, int e) {
    if (lazy[n] == 0) return;
    t[n] = t[n] + lazy[n] * (e - b + 1);
    if (b != e) {
      lazy[lc] = min(lazy[lc] , lazy[n]);
      lazy[rc] = lazy[rc] , lazy[n];
    }
    lazy[n] = 0;
  }
  inline long long combine(long long a,long long b) {
    return min(a , b);
  }
  inline void pull(int n) {
    t[n] = t[lc] + t[rc];
  }
  void build(int n, int b, int e) {
    lazy[n] = 0;
    if (b == e) {
      t[n] = a[b];
      return;
    }
    int mid = (b + e) >> 1;
    build(lc, b, mid);
    build(rc, mid + 1, e);
    pull(n);
  }
  void upd(int n, int b, int e, int i, int j, long long v) {
    push(n, b, e);
    if (j < b || e < i) return;
    if (i <= b && e <= j) {
      lazy[n] = v; //set lazy
      push(n, b, e);
      return;
    }
    int mid = (b + e) >> 1;
    upd(lc, b, mid, i, j, v);
    upd(rc, mid + 1, e, i, j, v);
    pull(n);
  }
  long long query(int n, int b, int e, int i, int j) {
    push(n, b, e);
    if (i > e || b > j) return 0xff; //return null
    if (i <= b && e <= j) return t[n];
    int mid = (b + e) >> 1;
    return combine(query(lc, b, mid, i, j), query(rc, mid + 1, e, i, j));
  }
};
int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int n,m, t, x, y, mn,  left, right, cur;
    string s;
    cin>>n>>m>>s;
    // cur
    // vector<int> a(n,0);
    if (s[0]=='(')
        a[0] = 1;
    else a[0] = -1;
    for(int i = 1 ; i<n; ++i){
        a[i]=a[i-1];
        if (s[i]=='(')
            a[i]++;
        else a[i]--;
        // cout<<a[i]<<" ";
    }
    cout<<endl;
    ST tree = ST();
    cout<<tree.query(0,0)<<endl;
    for(int i = 0; i<m; ++i){
        cin>>t>>x>>y;
        x--;
        y--;
        if(t==1){ //update
            if (s[x]==s[y])continue;
            if (s[x]=='('){
                swap(s[x],s[y]);
                tree.update(x,n-1,-2);
                tree.update(y,n-1,+2);
            }
            else{
                swap(s[x],s[y]);
                tree.update(x,n-1,+2);
                tree.update(y,n-1,-2);
            }
        }else{
            mn = tree.query(x,y);
            if(x==0)
                left = 0;
            else
                left = tree.query(x-1,x-1);
            right = tree.query(y,y);
            cout<<left<<" "<<right<<" "<<mn;
            if (left==right && mn>=min(left,right)) cout<<"Yes"<<endl;
            else cout<<"No"<<endl;
        }
    }
    return 0;
    // int n,i,tree_size;
    // cin>>n;
    // int a[n];
    // tree_size=2*n;
    // int tree[tree_size];
    // for(i=0;i<n;i++)cin>>a[i];
    // buildTree(tree,a,0,n-1,0);
    // int n_ops;  // number of operations to be performed
    // cin>>n_ops;
    // while(n_ops--){
    //     int x,l,r;
    //     cin>>x>>l>>r;
    //     if(x==0)
    //     cout<<queryMin(tree,0,n-1,l-1,r-1,0)<<endl;
    //     else
    //     {
    //         int dif;
    //         cin>>dif;
    //         update(tree,0,n-1,l-1,r-1,dif,0);
    //     }
    // }
}
// void solve(){

// }

// int main(){
//     if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
//     else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
//     int t = 1;
//     // cin>>t;
//     while(t-->0) solve();
//     return 0;
// }
