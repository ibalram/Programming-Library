#include <bits/stdc++.h>
using namespace std;
#define ll long long

const ll mxn = 300005;

struct node {
    pair<ll,ll> pref;
    pair<ll,ll> suff;
    ll ans;
    ll size;
};
node tree[4 * mxn];

ll calc(ll a, ll n){
    ll nth = a-n+1;
    if (nth>=0){
        return n*1L*(a+nth)/2;
    }
    return 1L*a*(a+1)/2;
}

ll calc(pair<ll,ll> pr){
    return calc(pr.first, pr.second);
}

void build(vector<ll> &arr, ll low, ll high, ll index){
    if (low == high) {
        tree[index].pref = {arr[low],1};
        tree[index].suff = {arr[low],1};
        tree[index].ans = arr[low];
        tree[index].size = 1;
    }
    else {
        ll mid = (low + high) / 2;
        build(arr, low, mid, 2 * index + 1);
        build(arr, mid + 1, high, 2 * index + 2);
        tree[index].pref = tree[2 * index + 1].pref;
        if (tree[2*index+1].size==tree[2*index+1].pref.second && tree[2*index+1].pref.first==tree[2*index+2].pref.first){
            tree[index].pref.second += tree[2 * index + 2].pref.second;
        }
        tree[index].suff = tree[2 * index + 2].suff;
        if (tree[2*index+2].size==tree[2*index+2].suff.second && tree[2*index+2].suff.first==tree[2*index+1].suff.first){
            tree[index].suff.second += tree[2 * index + 1].suff.second;
        }
        tree[index].ans = max(tree[2*index+1].ans, max(tree[2*index+2].ans, max(calc(tree[index].pref), calc(tree[index].suff))));
        if (tree[2*index+1].suff.first==tree[2*index+2].pref.first){
            tree[index].ans = max(tree[index].ans, calc(tree[2*index+1].suff.first, tree[2*index+1].suff.second + tree[2*index+2].pref.second));
        }
        tree[index].size = tree[2 * index + 1].size + tree[2 * index + 2].size;
    }
}


void update(ll index, ll low, ll high,ll idx, ll value){
    if (low == high) {
        tree[index].pref = {value,1};
        tree[index].suff = {value,1};
        tree[index].ans = value;
        tree[index].size = 1;
    }
    else {

        ll mid = (low + high) / 2;
        if (idx <= mid)
            update(2 * index + 1, low, mid, idx, value);
        else
            update(2 * index + 2, mid + 1, high, idx, value);
        tree[index].pref = tree[2 * index + 1].pref;
        if (tree[2*index+1].size==tree[2*index+1].pref.second && tree[2*index+1].pref.first==tree[2*index+2].pref.first){
            tree[index].pref.second += tree[2 * index + 2].pref.second;
        }
        tree[index].suff = tree[2 * index + 2].suff;
        if (tree[2*index+2].size==tree[2*index+2].suff.second && tree[2*index+2].suff.first==tree[2*index+1].suff.first){
            tree[index].suff.second += tree[2 * index + 1].suff.second;
        }
        tree[index].ans = max(tree[2*index+1].ans,
                          max(tree[2*index+2].ans,
                          max(calc(tree[index].pref), calc(tree[index].suff))));
        if (tree[2*index+1].suff.first==tree[2*index+2].pref.first){
            tree[index].ans = max(tree[index].ans,
                calc(tree[2*index+1].suff.first, tree[2*index+1].suff.second + tree[2*index+2].pref.second));
        }
        tree[index].size = tree[2 * index + 1].size + tree[2 * index + 2].size;
    }
}
node query(ll index, ll low, ll high, ll l, ll r){
    node result;
    result.pref = {0,0};
    result.suff = {0,0};
    result.ans = 0;
    result.size = 0;
    if (r < low || high < l){
        return result;
    }
    if (l <= low && high <= r){
        return tree[index];
    }

    ll mid = (low + high) / 2;
    if (l > mid) return query(2 * index + 2,mid + 1, high, l, r);
    if (r <= mid) return query(2 * index + 1,low, mid, l, r);

    node left = query(2 * index + 1,low, mid, l, r);
    node right = query(2 * index + 2,mid + 1, high, l, r);
    if (left.pref.second==0) return right;
    if (right.pref.second==0) return left;
    result.pref = {left.pref.first,left.pref.second};
    result.suff = {left.suff.first,left.suff.second};;
    result.ans = left.ans;
    result.size = left.size;
    if (left.size==left.pref.second && left.pref.first==right.pref.first){
        result.pref.second += right.pref.second;
    }
    result.suff = right.suff;
    if (right.size==right.suff.second && right.suff.first==left.suff.first){
        result.suff.second += left.suff.second;
    }
    result.ans = max(left.ans,max(right.ans,max(calc(result.pref), calc(result.suff))));
    if (left.suff.first==right.pref.first){
        result.ans = max(result.ans, calc(left.suff.first, left.suff.second + right.pref.second));
    }
    result.size = left.size + right.size;
    return result;
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    ll n, q;
    cin>>n>>q;
    vector<ll> a(n,0);
    for(ll i = 0; i<n; i++) {
        cin>>a[i];
    }
    build(a, 0, n-1, 0);
    ll x,l,r;
    for(ll i = 0; i<q; i++){
        cin>>x>>l>>r;
        if (x==1){
            cout<<query(0,0,n-1,l-1,r-1).ans<<" ";
        }
        else{
            update(0,0,n-1, l-1, r);
        }
    }
    cout<<"\n";
    return 0;
}

