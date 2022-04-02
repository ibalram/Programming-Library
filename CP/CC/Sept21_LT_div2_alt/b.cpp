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
      s+=(n%10)+'0';
      n/=10;
   }
    reverse(s.begin(), s.end());
    return s;
}

long long dp[20][2][83];
const long long k=3;

string s;

long long dp_solve(string & s,int index,bool smaller,int mod1){
    if(index==s.length()){
        if(mod1==0){
            return 1;
        }
        return 0;

    }
    if(dp[index][smaller][mod1]!=-1){
       return dp[index][smaller][mod1];
      }
    else{
        int limit=9;
        if(smaller){
            limit=s[index]-'0';
        }
        long long init_count=0;

        for(int i=0;i<=limit;i++){
            bool ns;
            if(i<s[index]-'0'){
                ns=0;
            }
            else{
                ns=smaller;
            }
            init_count+=dp_solve(s, index+1, ns,(mod1+i)%k);
        }
        dp[index][smaller][mod1]=init_count;
        return init_count;

    }

}


int solve(){
    long long a,b; //Find numbers between A and B whose sum of digits is divisible by K
    cin>>a>>b;
    string s=tostring(a-1);
    string s2=tostring(b);

    memset(dp,-1,sizeof(dp));
    long long a1=dp_solve(s,0,1,0); //Solving for a-1

    memset(dp,-1,sizeof(dp));
    long long a2=dp_solve(s2, 0, 1, 0); //Solving for b
    cout<<a2-a1<<endl;
    return 0;
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
