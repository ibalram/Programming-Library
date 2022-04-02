#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

#include <iostream>
#include <climits>
using namespace std;
int lazy[1000]={0};
void buildTree(int *tree,int *a,int start,int end,int node){
    if(start==end)tree[node]=a[start];
    else if(start<end){
        int mid=(start+end)/2,left=2*node+1,right=left+1;
        buildTree(tree,a,start,mid,left);
        buildTree(tree,a,mid+1,end,right);
        tree[node]=min(tree[left],tree[right]);
    }
}
void update(int *tree,int start,int end,int l,int r,int dif,int node){
    if(lazy[node]!=0){
        // there are pending updates
        tree[node]+=lazy[node];
        if(start!=end){
            lazy[2*node+1]+=lazy[node];
            lazy[2*node+2]+=lazy[node];
        }
        lazy[node]=0;
    }
    if(start> r or end<l)return;
    else if(start>=l and end<=r){
        tree[node]+=dif;    // make the update for the current range and keep them pending for the child nodes
        if(start!=end){
            lazy[2*node+1]+=dif;
            lazy[2*node+2]+=dif;
        }
        return;
    }
    int mid=(start+end)/2;
    update(tree,start,mid,l,r,dif,2*node+1);
    update(tree,mid+1,end,l,r,dif,2*node+2);
    tree[node]=min(tree[2*node+1],tree[2*node+2]);
}
int queryMin(int *tree,int start,int end,int l,int r,int node){
    if(lazy[node]!=0){
        // if there are updates pending, apply them before making the queries
        tree[node]+=lazy[node];
        if(start!=end){
            lazy[2*node+1]=lazy[node];
            lazy[2*node+2]=lazy[node];
        }
        lazy[node]=0;
    }
    if(start>r or end<l)return INT_MAX-1;
    else if(start>=l and end<=r)return tree[node];
    else{
        int mid=(start+end)/2,left=2*node+1,right=left+1;
        return min(queryMin(tree,start,mid,l,r,left),queryMin(tree,mid+1,end,l,r,right));
    }
}
int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int n,i,tree_size;
    cin>>n;
    int a[n];
    tree_size=2*n;
    int tree[tree_size];
    for(i=0;i<n;i++)cin>>a[i];
    buildTree(tree,a,0,n-1,0);
    int n_ops;  // number of operations to be performed
    cin>>n_ops;
    while(n_ops--){
        int x,l,r;
        cin>>x>>l>>r;
        if(x==0)
        cout<<queryMin(tree,0,n-1,l-1,r-1,0)<<endl;
        else
        {
            int dif;
            cin>>dif;
            update(tree,0,n-1,l-1,r-1,dif,0);
        }
    }
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
