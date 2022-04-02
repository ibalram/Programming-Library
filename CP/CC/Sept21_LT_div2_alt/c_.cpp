// source:  https://www.hackerrank.com/topics/digit-dp

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"

string tostring(long long n)
{
   string s;
   while(n!=0)
  {
      s+=(n%2)+'0';
      n/=2;
   }
    // reverse(s.begin(), s.end());
    return s;
}

int dp[64][2][2];
// const long long k=3;

string bits;

int m;
int DP(string &bits, int i, int turn, int changed){
    if (i>=m)
        return 1;
    if (dp[i][turn][changed]!=-1)
        return dp[i][turn][changed];
    if (bits[i]=='1'){
        if (changed==0){
            dp[i][turn][changed] = 1^DP(bits, i, turn^1, changed^1);
            return dp[i][turn][changed];
        }
    }
    int res = (1^DP(bits, i+1,turn^1, 0));
    if (i+1<m and bits[i+1]=='0'){
        res |= DP(bits, i+1, turn, 0);
    }dp[i][turn][changed] = res;
    return dp[i][turn][changed];
}
long long a;
void solve(){
    //Find numbers between A and B whose sum of digits is divisible by K
    cin>>a;
    string bits=tostring(a);
    m = bits.size();

    memset(dp,-1,sizeof(dp));
    int ans=DP(bits, 0,0,0); //Solving for a-1
    string res = "Bob";
    if (ans==1){
        res = "Alice";
    }
    cout<<res<<endl;
}

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    else
        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t = 1;
    cin>>t;
    while(t-->0) solve();
    return 0;
}
