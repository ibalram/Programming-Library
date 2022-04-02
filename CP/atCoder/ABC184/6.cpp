// C++ program to solve knapsack problem using
// branch and bound

//TLE
#include <bits/stdc++.h>
using namespace std;

#define int long long
// #define double long double
// Structure for Item which store weight and corresponding
// value of Item
struct Item
{
    double weight;
    int value;
};
Item arr[45];

// Node structure to store information of decision
// tree
struct Node
{
    int level, profit, bound;
    float weight;
};


bool cmp(Item a, Item b)
{
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2;
}

int bound(Node u, int n, int W, Item arr[])
{
    if (u.weight >= W)
        return 0;

    int profit_bound = u.profit;

    int j = u.level + 1;
    int totweight = u.weight;


    while ((j < n) && (totweight + arr[j].weight <= W))
    {
        totweight    += arr[j].weight;
        profit_bound += arr[j].value;
        j++;
    }
    if (j < n)
        profit_bound += (W - totweight) * arr[j].value /
                                         arr[j].weight;

    return profit_bound;
}


int knapsack(int W, Item arr[], int n)
{
    sort(arr, arr + n, cmp);
    queue<Node> Q;
    Node u, v;
    u.level = -1;
    u.profit = u.weight = 0;
    Q.push(u);
    int maxProfit = 0;
    while (!Q.empty())
    {
        // Dequeue a node
        u = Q.front();
        Q.pop();
        if (u.level == -1)
            v.level = 0;
        if (u.level == n-1)
            continue;

        v.level = u.level + 1;

        v.weight = u.weight + arr[v.level].weight;
        v.profit = u.profit + arr[v.level].value;
        if (v.weight <= W && v.profit > maxProfit)
            maxProfit = v.profit;
        v.bound = bound(v, n, W, arr);
        if (v.bound > maxProfit)
            Q.push(v);
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, n, W, arr);
        if (v.bound > maxProfit)
            Q.push(v);
    }
    return maxProfit;
}

// driver program to test above function
int32_t main()
{
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
    int n= 0,W = 10;   // Weight of knapsack
    cin>>n>>W;
    for (int i =0; i<n; ++i){
        int x;
        cin>>x;
        arr[i] = Item({1.0*x,x});
    }
    cout << knapsack(W, arr, n);

    return 0;
}

