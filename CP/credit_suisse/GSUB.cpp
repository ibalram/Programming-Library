// good problem
// segment tree
//GSUB codechef

#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
const int mxn = 2e5+2;

int a[mxn];
struct Node{
    int l,r,size;
}st[4*mxn];

Node build(int root, int l, int r){
    if(l==r){
        Node node ={a[l],a[l],1};
        st[root] = node;
        return st[root];
    }
    int mid = l+r>>1;
    Node ll = build(2*root+1, l, mid);
    Node rr = build(2*root+2, mid+1, r);
    if (ll.r==rr.l)
        ll.size--;
    return st[root] = {ll.l, rr.r, ll.size+rr.size};
}

Node update(int root, int l, int r, int idx){
    if (idx<l || idx>r) return st[root];
    if (l==r) {
        return st[root] = {a[l],a[l],1};
    }
    int mid = l+r>>1;
    Node ll,rr;
    if (idx<=mid){
        ll = update(2*root+1, l, mid, idx);
        rr = st[2*root+2];
    }
    else{
        rr = update(2*root+2, mid+1, r, idx);
        ll = st[2*root+1];
    }
    if (ll.r==rr.l){
        ll.size--;
    }
    return st[root] = {ll.l, rr.r, ll.size+rr.size};
}

/*int rec(int l, int r){
    if (l==r) return 1;
    int mid = l+r>>1;
    int res = rec(l,mid)+rec(mid+1,r);
    if (a[mid]==a[mid+1])
        res--;
    return res;
}*/
int main(){
    // freopen("in.txt", "r", stdin);
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0){
        int n,q;
        cin>>n>>q;
        for(int i=0; i<n; ++i) cin>>a[i];
        build(0, 0, n-1);
        int x,y;
        for (int i =0; i<q; ++i){
            cin>>x>>y;
            x--;
            a[x] = y;
            cout<<update(0,0,n-1,x).size<<endl;
            // cout<<rec(0,n-1)<<endl;
        }
    }
    return 0;
}


//
 // freopen("in.txt", "r", stdin);
