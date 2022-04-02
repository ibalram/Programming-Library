#include<bits/stdc++.h>
#include<io.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define X first
#define Y second
#define endl "\n"
const ll mod = 1e9+7;
const int mxn = 2e5+2;

void solve(){

}

long getNumber(SinglyLinkedListNode* binary){
    long res = 0;
    while (binary!=null){
        res = res*2+binary.data;
        binary = binary->next;
    }
    return res;
}

int main(){
    if (access("in.txt", F_OK) != -1) freopen("in.txt", "r", stdin);
    else {ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);}

    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}
