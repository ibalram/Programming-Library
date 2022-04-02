#include <bits/stdc++.h>
using namespace std;
#define ll long long

const ll MAX = 300005;

// Source: GeeksForGeeks

// Structure to store
// 4 values that are to be stored
// in the nodes
struct node {
    pair<ll,ll> prefix;
    pair<ll,ll> suffix;
    ll ans;
    ll length;
};

// array to store the segment tree
node tree[4 * MAX];

// function to build the tree

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

void build(vector<ll> &arr, ll low, ll high, ll index)
{
    // the leaf node
    if (low == high) {
        tree[index].prefix = {arr[low],1};
        tree[index].suffix = {arr[low],1};
        tree[index].ans = arr[low];
        tree[index].length = 1;
    }
    else {
        ll mid = (low + high) / 2;

        // left subtree
        build(arr, low, mid, 2 * index + 1);

        // right subtree
        build(arr, mid + 1, high, 2 * index + 2);

        // parent node's prefix sum will be equivalent
        // to maximum of left child's prefix sum or left
        // child sum + right child prefix sum.
        tree[index].prefix = tree[2 * index + 1].prefix;
        if (tree[2*index+1].length==tree[2*index+1].prefix.second && tree[2*index+1].prefix.first==tree[2*index+2].prefix.first){
            tree[index].prefix.second += tree[2 * index + 2].prefix.second;
        }


        // parent node's suffix sum will be equal to right
        // child suffix sum or right child sum + suffix
        // sum of left child
        tree[index].suffix = tree[2 * index + 2].suffix;
        if (tree[2*index+2].length==tree[2*index+2].suffix.second && tree[2*index+2].suffix.first==tree[2*index+1].suffix.first){
            tree[index].suffix.second += tree[2 * index + 1].suffix.second;
        }
        tree[index].ans = max(tree[2*index+1].ans,
                          max(tree[2*index+2].ans,
                          max(calc(tree[index].prefix), calc(tree[index].suffix))));
        if (tree[2*index+1].suffix.first==tree[2*index+2].prefix.first){
            tree[index].ans = max(tree[index].ans,
                calc(tree[2*index+1].suffix.first, tree[2*index+1].suffix.second + tree[2*index+2].prefix.second));
        }
        tree[index].length = tree[2 * index + 1].length + tree[2 * index + 2].length;
    }
}

// function to update the tree
void update(ll index, ll low, ll high,
            ll idx, ll value)
{
    // the node to be updated
    if (low == high) {
        tree[index].prefix = {value,1};
        tree[index].suffix = {value,1};
        tree[index].ans = value;
        tree[index].length = 1;
    }
    else {

        ll mid = (low + high) / 2;

        // if node to be updated is in left subtree
        if (idx <= mid)
            update(2 * index + 1, low, mid, idx, value);

        // if node to be updated is in right subtree
        else
            update(2 * index + 2, mid + 1, high, idx, value);

        // parent node's prefix sum will be equivalent
        // to maximum of left child's prefix sum or left
        // child sum + right child prefix sum.
        tree[index].prefix = tree[2 * index + 1].prefix;
        if (tree[2*index+1].length==tree[2*index+1].prefix.second && tree[2*index+1].prefix.first==tree[2*index+2].prefix.first){
            tree[index].prefix.second += tree[2 * index + 2].prefix.second;
        }

        // parent node's suffix sum will be equal to right
        // child suffix sum or right child sum + suffix
        // sum of left child
        tree[index].suffix = tree[2 * index + 2].suffix;
        if (tree[2*index+2].length==tree[2*index+2].suffix.second && tree[2*index+2].suffix.first==tree[2*index+1].suffix.first){
            tree[index].suffix.second += tree[2 * index + 1].suffix.second;
        }
        tree[index].ans = max(tree[2*index+1].ans,
                          max(tree[2*index+2].ans,
                          max(calc(tree[index].prefix), calc(tree[index].suffix))));
        if (tree[2*index+1].suffix.first==tree[2*index+2].prefix.first){
            tree[index].ans = max(tree[index].ans,
                calc(tree[2*index+1].suffix.first, tree[2*index+1].suffix.second + tree[2*index+2].prefix.second));
        }
        tree[index].length = tree[2 * index + 1].length + tree[2 * index + 2].length;
    }
}

// function to return answer to  every type-1 query
node query(ll index, ll low, ll high, ll l, ll r){
    // initially all the values are INT_MIN
    // cout<<low<<" "<<high<<endl;
    //     cout<<l<<" "<<r<<endl;
    node result;
    result.prefix = {0,0};
    result.suffix = {0,0};
    result.ans = 0;
    result.length = 0;

    // range does not lies in this subtree
    if (r < low || high < l){
        cout<<"YES"<<endl;
        return result;
    }

    // complete overlap of range
    if (l <= low && high <= r){
        // cout<<"hii"<<index<<tree[index].ans<<endl;
        return tree[index];
    }

    ll mid = (low + high) / 2;

    // right subtree
    if (l > mid)
        return query(2 * index + 2,mid + 1, high, l, r);

    // left subtree
    if (r <= mid)
        return query(2 * index + 1,low, mid, l, r);

    node left = query(2 * index + 1,low, mid, l, r);
    node right = query(2 * index + 2,mid + 1, high, l, r);

    // parent node's prefix sum will be equivalent
    // to maximum of left child's prefix sum or left
    // child sum + right child prefix sum.
    // cout<<"hii"<<endl;
    if (left.prefix.second==0){
        return right;
    }
    if (right.prefix.second==0){
        return left;
    }
    // print()
    result.prefix = {left.prefix.first,left.prefix.second};
    result.suffix = {left.suffix.first,left.suffix.second};;
    result.ans = left.ans;
    result.length = left.length;
    if (left.length==left.prefix.second && left.prefix.first==right.prefix.first){
        result.prefix.second += right.prefix.second;
    }

    // parent node's suffix sum will be equal to right
    // child suffix sum or right child sum + suffix
    // sum of left child
    result.suffix = right.suffix;
    if (right.length==right.suffix.second && right.suffix.first==left.suffix.first){
        result.suffix.second += left.suffix.second;
    }
    result.ans = max(left.ans,
                      max(right.ans,
                      max(calc(result.prefix), calc(result.suffix))));
    if (left.suffix.first==right.prefix.first){
        result.ans = max(result.ans,
            calc(left.suffix.first, left.suffix.second + right.prefix.second));
    }
    result.length = left.length + right.length;
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
    // for(ll i = 0; i<1; i++) {
    //     cout<<tree[i].ans<<endl;
    // }
    ll x,l,r;
    for(ll i = 0; i<q; i++){
        cin>>x>>l>>r;
        if (x==2){
            update(0,0,n-1, l-1, r);
        }
        else{
            node x = query(0,0,n-1,l-1,r-1);
            cout<<x.ans<<" ";
        }
    }
    cout<<"\n";
    // for(ll i = 0; i<1; i++) {
    //     cout<<tree[i].ans<<endl;
    // }
    return 0;
}

