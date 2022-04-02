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

class IntervalTree
{
    int* tree;
    int* lazy;
    int n;

    void build_tree(const vector<int>& v, int node, int a, int b)
    {
        if (a > b) return;

        if (a == b) { tree[node] = v[a]; return; }

        build_tree(v, node * 2, a, (a + b) / 2);
        build_tree(v, node * 2 + 1, 1 + (a + b) / 2, b);
        tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
    }

    void update_lazy(int node, int a, int b)
    {
        tree[node] += lazy[node];

        if (a != b)
        {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }

        lazy[node] = 0;
    }

    void update_tree(int node, int a, int b, int i, int j, int value)
    {
        if (lazy[node] != 0) update_lazy(node,a,b);

        if (a > b || a > j || b < i) return;

        if (a >= i && b <= j)
        {
            tree[node] += value;
            if (a != b)
            {
                lazy[node * 2] += value;
                lazy[node * 2 + 1] += value;
            }
            return;
        }

        update_tree(node * 2, a, (a + b) / 2, i, j, value);
        update_tree(1 + node * 2, 1 + (a + b) / 2, b, i, j, value);

        tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
    }

    int query_tree(int node, int a, int b, int i, int j)
    {
        if (a > b || a > j || b < i) return mod;

        if (lazy[node] != 0) update_lazy(node,a,b);

        if (a >= i && b <= j) return tree[node];

        int q1 = query_tree(node * 2, a, (a + b) / 2, i, j);
        int q2 = query_tree(1 + node * 2, 1 + (a + b) / 2, b, i, j);

        return min(q1, q2);
    }

public:
    IntervalTree(const vector<int>& v)
    {
        n = v.size();
        int s = 2*pow(2, ceil(log2(v.size())));
        tree = new int[s];
        lazy = new int[s];
        memset(lazy, 0, sizeof lazy);
        for(int i =0; i<s; ++i){
            tree[i] = mod;
        }
        build_tree(v, 1, 0, n - 1);
        int ht = 0;
        for(int i = 0; i<s; ++i){
            cout<<tree[i]<<" ";
            if (i+1==(1<<ht)){
                cout<<endl;
                ht++;
            }
        }
        cout<<endl;
    }

    void update(int idx1, int idx2, int add){
        update_tree(1, 0, n - 1, idx1, idx2, add);
    }

    int query(int idx1, int idx2){
        cout<<tree[idx2]<<endl;
        return query_tree(1, 0, n - 1, idx1, idx2);
    }
};
int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int n,m, t, x, y, mn,  left, right;
    string s;
    cin>>n>>m>>s;
    vector<int> a(n,0);
    if (s[0]=='(')
        a[0]++;
    else a[0]--;
    for(int i = 1 ; i<n; ++i){
        a[i]+=a[i-1];
        if (s[i]=='(')
            a[i]++;
        else a[i]--;
        cout<<a[i]<<" ";
    }
    cout<<endl;
    IntervalTree tree = IntervalTree(a);
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
