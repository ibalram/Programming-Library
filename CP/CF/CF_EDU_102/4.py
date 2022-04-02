import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)


import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int,input().split())
    s = "#"+input().strip()
    pf = [0]*(n+2)
    mnpf = [0]*(n+2)
    mxpf = [0]*(n+2)
    mnsff = [0]*(n+2)
    mxsff = [0]*(n+2)
    for i in range(1,n+1):
        pf[i] = pf[i-1]+(s[i]=="+")
        pf[i]-=(s[i]=="-")
        mnpf[i] = min(pf[i],mnpf[i-1])
        mxpf[i] = max(pf[i], mxpf[i-1])
    cur = 0
    lstmn = 0
    lstmx = 0
    for i in range(n-1,0,-1):
        cur-=(s[i+1]=="+")
        cur+=(s[i+1]=="-")
        lstmn = min(cur,lstmn)
        lstmx = max(cur,lstmx)
        mnsff[i] = lstmn-cur
        mxsff[i] = lstmx-cur
    for qe in range(m):
        l,r = map(int,input().split())
        low = high = 0
        if l==1 and r==n:
            print(1)
            continue
        if l==1:
            print(mxsff[r]-mnsff[r]+1)
            continue
        if r==n:
            print(mxpf[l-1]-mnpf[l-1]+1)
            continue
        high = max(mxpf[l-1], pf[l-1] + mxsff[r])
        low = min(mnpf[l-1], pf[l-1] + mnsff[r])
        print(high-low+1)
"""
#include <bits/stdc++.h>
using namespace std;
void solution() {
  int n, m;
  cin >> n >> m;
  string s;
  cin >> s;
  s = '~' + s;
  vector<int> pref(n + 2), suf(n + 2), min_pref(n + 2, n + 1), max_pref(n + 2), min_suf(n + 2, n + 1), max_suf(n + 2);
  for (int i = 1; i <= n; i ++) {
    int delta = (s[i] == '-' ? -1: 1);
    pref[i] = pref[i - 1] + delta;
    min_pref[i] = min(pref[i], min_pref[i - 1]);
    max_pref[i] = max(pref[i], max_pref[i - 1]);
  }
  for (int i = n; i >= 1; i --) {
    min_suf[i] = min(min_suf[i + 1], pref[i]);
    max_suf[i] = max(max_suf[i + 1], pref[i]);
  }
  while (m --) {
    int l, r;
    cin >> l >> r;
    int low = 0, high = 0;
    if (l > 1) low = min(low, min_pref[l - 1]);
    if (l > 1) high = max(high, max_pref[l - 1]);
    if (r < n) low = min(low, pref[l - 1] - pref[r] + min_suf[r + 1]);
    if (r < n) high = max(high, pref[l - 1] - pref[r] + max_suf[r + 1]);
    cout << high - low + 1 << '\n';
  }
}
main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int tests;
  cin >> tests;
  for (int i = 1; i <= tests; i ++) solution();
}

"""
