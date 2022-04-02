#include <bits/stdc++.h>
using namespace std;
#define pb push_back
typedef long long int ll;
#define pll pair<ll, ll>
#define mll map <ll, ll>
#define vl vector <ll>
#define vll vector <pll>
#define mod 1000000007
#define rep(i, a, b) for(ll i = a; i < b; i++)
#define fast_io ios_base::sync_with_stdio(false);  cin.tie(NULL);
#define all(v) v.begin(), v.end()
#define dall(v) v.begin(), v.end(), greater<ll>()

int func(vl v){
    int i = 1;
    int tem1 = 0;
    if(v[1] > v[0] && v[1] > v[2])
        tem1++;
    if(v[2] < v[1] && v[2] < v[3])
        tem1++;
    if(v[0] > v[1] && v[2] > v[1])
        tem1++;
    if(v[2] > v[1] && v[2] > v[3])
        tem1++;
    return tem1;
}

int func2(vl v){
    int tem1 = 0;
    if(v[v.size()-2] > v[v.size()-1] && v[v.size() - 2] > v[v.size() - 3])
        tem1++;
    if(v[v.size()-3] > v[v.size()-2] && v[v.size() - 3] > v[v.size() - 4])
        tem1++;
    if(v[v.size()-2] < v[v.size()-1] && v[v.size() - 2] < v[v.size() - 3])
        tem1++;
    if(v[v.size()-3] > v[v.size()-2] && v[v.size() - 3] < v[v.size() - 4])
        tem1++;
    return tem1;
}


int main(){
    freopen("in.txt","r",stdin);
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

            int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        int arr[n];
        for(int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        int mark[n], ans = 0;
        memset(mark, 0, sizeof(mark));
        for(int i = 1; i < n - 1; i++) {
            if((arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) || (arr[i] < arr[i - 1] && arr[i] < arr[i + 1])) {
                ++ans;
                mark[i] = 1;
            }
        }
        int ans1 = ans, ans2 = ans;
        if(ans == 0 || ans == 1) {
            cout << "0\n";
        } else {
            for(int i = 1; i < n - 2; i++) {
                ans = ans2;
                if(mark[i] == 1) {
                    int temp = arr[i];
                    arr[i] = arr[i - 1];
                    int count = 1;
                    if(mark[i + 1] == 1)
                        count++;

                    if(i - 2 >= 0){
                        if(arr[i - 1] == 0) {
                            if((arr[i - 1] < arr[i] && arr[i - 1] < arr[i - 2]) || ( arr[i - 1] > arr[i] && arr[i - 1] > arr[i - 2])) {
                                --count;
                            }
                        }
                        if(arr[i - 1] == 1) {
                            if((arr[i - 1] < arr[i] && arr[i - 1] < arr[i - 2]) || ( arr[i - 1] > arr[i] && arr[i - 1] > arr[i - 2])) {
                            } else {
                                ++count;
                            }
                        }

                    }
                    ans1 = min(ans1, ans - count);
                    }
            }
            cout << ans1 << " \n";
        }

    }
    return 0;
}
// #include<bits/stdc++.h>
// using namespace std;
// typedef long long ll;
// #define endl "\n"

// int main() {
//     freopen("in.txt","r",stdin);
//     ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

//     int t=0;
//     cin>>t;
//     while(t--){
//         int n;
//         cin>>n;
//         int a[n]={0};
//         for(int i=0;i<n;i++)
//             cin>>a[i];
//         ll cnthl = 0, cntvl = 0;
//         vector<ll> v;
//         if (a[0] > a[1])
//             v.push_back(2);
//         else{
//             v.push_back(1);
//         }

//         for (int i=1; i< n - 1; ++i)
//         {
//             if (a[i - 1] > a[i] && a[i + 1] > a[i])
//             {
//                 cntvl++;
//                 v.push_back(1);
//             }
//             else if (a[i - 1] < a[i] && a[i + 1] < a[i])
//             {
//                 cnthl++;
//                 v.push_back(2);
//             }
//         }

//         if (a[n - 1] > a[n - 2])
//             v.push_back(2);
//         else
//             v.push_back(1);
//         bool flag = 0;
//         ll z = cnthl;
//         for (int i=0; i< v.size(); ++i)
//         {
//             if (v[i] == v[i + 2] && v[i] == v[i + 4] && v[i + 1] == v[i + 3] && v[i] != v[i + 1])
//             {
//                 if (v[i] == 1)
//                 {
//                     cnthl -= 2;
//                     cntvl -= 1;
//                 }
//                 else
//                 {
//                     cnthl -= 1;
//                     cntvl -= 2;
//                 }
//                 break;
//             }
//         }

//         if (cnthl != z)
//             flag = 1;
//         if (!flag)
//         {
//             for (int i=0; i< v.size(); ++i)
//             {
//                 if (v[i] == v[i + 2] && v[i] != v[i + 1])
//                 {
//                     if (v[i] == 1){
//                         cnthl--;
//                     }
//                     else
//                         cntvl--;
//                     break;
//                 }
//             }
//         }
//          cout <<  cnthl + cntvl << endl;
//     }
//     return 0;
// }
