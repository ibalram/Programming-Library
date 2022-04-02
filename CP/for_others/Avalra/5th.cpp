#include<bits/stdc++.h>
using namespace std;
#define int long long int
#define fast_io ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

string solve(string s){
    string month, date, year, time;
        stringstream ss(s);
        ss >> month >> date >> year >> time;
        int mn;
        if (month == "January") mn = 1;
        if (month == "February") mn = 2;
        if (month == "March")   mn = 3;
        if (month == "April") mn = 4;
        if (month == "May") mn = 5;
        if (month == "June") mn = 6;
        if (month == "July")    mn = 7;
        if (month == "August") mn = 8;
        if (month == "September")   mn = 9;
        if (month == "October") mn = 10;
        if (month == "November")    mn = 11;
        if (month == "December") mn = 12;

        date.pop_back();
        int dt = stoi(date);

        int yr = stoi(year);
        int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (yr % 400 == 0 || (yr % 100 != 0 && yr % 4 == 0))
            days[1]++;

        int tot = 0;
        for (int i : days)
            tot += i;

        tot *= 24;
        tot *= 60;

        int ele = 0;

        for (int i = 0; i < mn - 1; i++)
            ele += (days[i] * 24 * 60);
        ele += (dt - 1) * 24 * 60;
        ele += ((int)(time[0] - '0') * 10 + (time[1] - '0')) * 60;
        ele += ((int)(time[3] - '0') * 10 + (time[4] - '0'));
        ele *= 100;
        setprecision(11);
        long double ans = (long double)(ele) / tot;

        std::stringstream stream;
        stream << fixed << setprecision(11) << ans;
        return stream.str();
}
int32_t main() {
    fast_io
    freopen("in.txt", "r", stdin);
    int t = 1;
    while (t--) {
        string s;
        getline(cin, s);
        cout << solve(s);
    }
    return 0;
}


// January 31, 1900 00:47
