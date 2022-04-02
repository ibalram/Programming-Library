#include <bits/stdc++.h>
using namespace std;

const int MAX = 100005;


// Source: GeeksForGeeks

// Structure to store
// 4 values that are to be stored
// in the nodes
struct node {
    long long prefixsums, suffixsums, sum, resultsum, length;
};

// array to store the segment tree
node tree[4 * MAX];

// function to build the tree
void build(vector<int> &arr, int low, int high, int index)
{
    // the leaf node
    if (low == high) {
        tree[index].prefixsums = arr[low];
        tree[index].suffixsums = arr[low];
        tree[index].sum = arr[low];
        tree[index].resultsum = arr[low];
        tree[index].length = 1;
    }
    else {
        int mid = (low + high) / 2;

        // left subtree
        build(arr, low, mid, 2 * index + 1);

        // right subtree
        build(arr, mid + 1, high, 2 * index + 2);

        // parent node's sum is the summation
        // of left and right child
        tree[index].sum = tree[2 * index + 1].sum + tree[2 * index + 2].sum;

        // parent node's prefix sum will be equivalent
        // to maximum of left child's prefix sum or left
        // child sum + right child prefix sum.
        tree[index].prefixsums = tree[2 * index + 1].prefixsums +
                    tree[2 * index + 1].sum * tree[2 * index + 2].length +
                    tree[2 * index + 2].prefixsums;

        // parent node's suffix sum will be equal to right
        // child suffix sum or right child sum + suffix
        // sum of left child
        tree[index].suffixsums = tree[2 * index + 2].suffixsums +
                    tree[2 * index + 2].sum * tree[2 * index + 1].length +
                    tree[2 * index + 1].suffixsums;

        // maxum will be the maximum of prefix, suffix of
        // parent or maximum of left child or right child
        // and summation of left child's suffix and right
        // child's prefix.
        tree[index].resultsum =
                    tree[2 * index + 1].resultsum + tree[2 * index + 2].resultsum+
                    tree[2 * index + 1].length * tree[2 * index + 2].prefixsums +
                    tree[2 * index + 2].length * tree[2 * index + 1].suffixsums;
        tree[index].length = tree[2 * index + 1].length + tree[2 * index + 2].length;
    }
}

// function to update the tree
void update(int index, int low, int high,
            int idx, int value)
{
    // the node to be updated
    if (low == high) {
        tree[index].prefixsums = value;
        tree[index].suffixsums = value;
        tree[index].sum = value;
        tree[index].resultsum = value;
        tree[index].length = 1;
    }
    else {

        int mid = (low + high) / 2;

        // if node to be updated is in left subtree
        if (idx <= mid)
            update(2 * index + 1, low, mid, idx, value);

        // if node to be updated is in right subtree
        else
            update(2 * index + 2, mid + 1, high, idx, value);

        // parent node's sum is the summation of left
        // and right child
        tree[index].sum = tree[2 * index + 1].sum + tree[2 * index + 2].sum;

        // parent node's prefix sum will be equivalent
        // to maximum of left child's prefix sum or left
        // child sum + right child prefix sum.
        tree[index].prefixsums = tree[2 * index + 1].prefixsums +
                    tree[2 * index + 1].sum * tree[2 * index + 2].length +
                    tree[2 * index + 2].prefixsums;

        // parent node's suffix sum will be equal to right
        // child suffix sum or right child sum + suffix
        // sum of left child
        tree[index].suffixsums = tree[2 * index + 2].suffixsums +
                    tree[2 * index + 2].sum * tree[2 * index + 1].length +
                    tree[2 * index + 1].suffixsums;

        // maxum will be the maximum of prefix, suffix of
        // parent or maximum of left child or right child
        // and summation of left child's suffix and right
        // child's prefix.
        tree[index].resultsum =
                    tree[2 * index + 1].resultsum + tree[2 * index + 2].resultsum+
                    tree[2 * index + 1].length * tree[2 * index + 2].prefixsums +
                    tree[2 * index + 2].length * tree[2 * index + 1].suffixsums;
        tree[index].length = tree[2 * index + 1].length + tree[2 * index + 2].length;
    }
}

// function to return answer to  every type-1 query
node query(int index, int low, int high, int l, int r){
    // initially all the values are INT_MIN
    node result;
    result.prefixsums = 0;
    result.suffixsums = 0;
    result.sum = 0;
    result.resultsum = 0;
    result.length = 0;

    // range does not lies in this subtree
    if (r < low || high < l)
        return result;

    // complete overlap of range
    if (l <= low && high <= r)
        return tree[index];

    int mid = (low + high) / 2;

    // right subtree
    if (l > mid)
        return query(2 * index + 2,mid + 1, high, l, r);

    // left subtree
    if (r <= mid)
        return query(2 * index + 1,low, mid, l, r);

    node left = query(2 * index + 1,low, mid, l, r);
    node right = query(2 * index + 2,mid + 1, high, l, r);

    // finding the maximum and returning it
    // result.sum = left.sum + right.sum;
    // result.prefixsum = max(left.prefixsum, left.sum +right.prefixsum);

    // result.suffixsum = max(right.suffixsum,right.sum + left.suffixsum);
    // result.maxsum = max(result.prefixsum,
    //                 max(result.suffixsum,
    //                 max(left.maxsum,
    //                 max(right.maxsum,left.suffixsum + right.prefixsum))));
    result.sum = left.sum + right.sum;

    // parent node's prefix sum will be equivalent
    // to maximum of left child's prefix sum or left
    // child sum + right child prefix sum.
    result.prefixsums = left.prefixsums +
                left.sum * right.length +
                right.prefixsums;

    // parent node's suffix sum will be equal to right
    // child suffix sum or right child sum + suffix
    // sum of left child
    result.suffixsums = right.suffixsums +
                right.sum * left.length +
                left.suffixsums;

    // maxum will be the maximum of prefix, suffix of
    // parent or maximum of left child or right child
    // and summation of left child's suffix and right
    // child's prefix.
    result.resultsum =
                left.resultsum + right.resultsum+
                left.length * right.prefixsums +
                right.length * left.suffixsums;
    result.length = left.length + right.length;
    return result;
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    int t = 0;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n,0);
        for(int i = 0; i<n; i++) {
            cin>>a[i];
        }
        build(a, 0, n-1, 0);
        int q, x,l,r;
        cin>>q;
        for(int i = 0; i<q; i++){
            cin>>x>>l>>r;
            if (x==1){
                update(0,0,n-1, l-1, r);
            }
            else{
                node ans = query(0,0,n-1,l-1,r-1);
                cout<<ans.resultsum<<"\n";
            }
        }


    }

    return 0;
}

