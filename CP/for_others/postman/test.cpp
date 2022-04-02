#include<bits/stdc++.h>
#include <cstring>
#define mod 1000000007
#define mp make_pair
#define pb push_back
#define fi first
#define ss second
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define ll long long int
#define inf 1000000000
#define endl '\n'
using namespace std;

void decode(string s,string key)
{
    int n=s.length();
   // cout<<n<<" ";
    int m=key.length();
   // cout<<m<<endl;
    string t=key;
    n=n/m;
   // cout<<n<<endl;
    char mat[n+1][m+1];
    int cnt=0;
    for(int i=1;i<=m;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if((int)s[cnt]==32)
            mat[j][i]='0';
            else
            mat[j][i]=s[cnt];
            cnt++;
        }
    }

    sort(key.begin(),key.end());
    cnt=0;
    for(int i=1;i<=m;i++)
    mat[0][i]=key[cnt++];

    key=t;

    char matrix[n+1][m+1];
    cnt=1;
    for(int i=0;i<m;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(key[i]==mat[0][j])
            {
                for(int k=1;k<=n;k++)
                {
                    matrix[k][cnt]=mat[k][j];
                }
                cnt++;
            }
        }
    }
    vector<string>v;
    cnt=0;
    string a;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(matrix[i][j]=='0' || matrix[i][j]=='_')
            {
                v.push_back(a);
                a.clear();
                continue;
            }
            a.push_back(matrix[i][j]);
        }
    }
    map<string,int>mp;
    mp["Khardung"]=1;
    mp["Lachulung"]=1;
    mp["Gyong"]=1;
    mp["Sasser"]=1;
    mp["Zoji"]=1;
    mp["Sia"]=1;
    mp["Indira"]=1;
    mp["Rezang"]=1;
    mp["Tanglang"]=1;
    mp["Pensi"]=1;
    mp["Marsimik"]=1;
    int flag=0;
     for(int i=0;i<v.size();i++)
    {
        if(v[i]=="not" || v[i]=="Not")
        {
            flag=1;
        }
    }
    for(int i=0;i<v.size();i++)
    {
        if(mp.find(v[i])!=mp.end())
        {
            mp[v[i]]=0;
        }
    }
    vector<string>res;
    if(flag==1)
    {
         map<string,int>::iterator it;
        for(it=mp.begin();it!=mp.end();it++)
        {
           if(it->second==1)
           {
               res.push_back(it->first);
           }
        }

    }
    else{
         map<string,int>::iterator it;
        for(it=mp.begin();it!=mp.end();it++)
        {
           if(it->second==0)
           {
               res.push_back(it->first);
           }
        }
    }

    for(int i=0;i<res.size();i++)
    {
        cout<<res[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    freopen("in.txt", "r", stdin);
    string s;
    getline(cin,s);
    ///cout<<s;
    string key;
    getline(cin,key);
    ///cout<<key;
    decode(s,key);

    return 0;
}
