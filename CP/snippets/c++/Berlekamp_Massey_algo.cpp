// Berlekamp-Massey Algorithm for solving Linear Recurrence

// in O(N^2)
// Optimization of naive DP
// Calculate for small n (distict points) using DP
// then just feed this sequence in BM algo, you are done.
// Better alternative to Matrix Exponent.

// Problem: Tree-Count
// by https://www.hackerearth.com/@bluedawnstar (Youngman Ro)
// https://www.hackerearth.com/challenges/competitive/april-circuits-21/algorithm/tree-count-16e5d14a/
// https://www.hackerearth.com/challenges/competitive/april-circuits-21/algorithm/tree-count-16e5d14a/submission/56770971/

// My submission: using langrange interpolation
// c++(AC): https://www.hackerearth.com/submission/56744691/
// python(TLE): https://www.hackerearth.com/submission/56744609/


// by Gennady:
// https://www.hackerearth.com/challenges/competitive/april-circuits-21/algorithm/tree-count-16e5d14a/submission/56741277/
#include <memory.h>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cstring>
#include <climits>
#include <cmath>
#include <complex>
#include <vector>
#include <string>
#include <memory>
#include <numeric>
#include <limits>
#include <functional>
#include <tuple>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#ifndef __GNUC__
#include <intrin.h>
#endif
#include <immintrin.h>

using namespace std;

#define PROFILE_START(i)    clock_t start##i = clock()
#define PROFILE_STOP(i)     fprintf(stderr, "elapsed time (" #i ") = %f\n", double(clock() - start##i) / CLOCKS_PER_SEC)

#ifndef M_PI
#define M_PI       3.14159265358979323846   // pi
#endif

typedef long long           ll;
typedef unsigned long long  ull;

const int MOD = 1'000'000'007;

int modPow(int x, int n) {
    if (n == 0)
        return 1;

    long long t = x % MOD;
    long long res = 1;
    for (; n > 0; n >>= 1) {
        if (n & 1)
            res = res * t % MOD;
        t = t * t % MOD;
    }
    return int(res);
}

inline int modInv(int x) {
    return modPow(x, MOD - 2);
}

template <int mod, int MaxN = (1 << 12)>
struct PolyFFTMod3 {
    static pair<double, double> w[MaxN];
    static bool initialized;

    static void init() {
        if (!initialized) {
            for (int i = 1; i < MaxN; i <<= 1) {
                for (int j = 0; j < i; j++) {
                    w[i + j].first = cos(M_PI * j / i);
                    w[i + j].second = sin(M_PI * j / i);
                }
            }
            initialized = true;
        }
    }

    static void fft(const pair<double, double>* in, pair<double, double>* out, int n, int k = 1) {
        if (n == 1) {
            *out = *in;
        } else {
            n >>= 1;
            fft(in, out, n, k << 1);
            fft(in + k, out + n, n, k << 1);
            for (int i = 0; i < n; i++) {
                pair<double, double> t(out[i + n].first * w[i + n].first - out[i + n].second * w[i + n].second,
                    out[i + n].second * w[i + n].first + out[i + n].first * w[i + n].second);

                out[i + n].first = out[i].first - t.first;
                out[i + n].second = out[i].second - t.second;
                out[i].first += t.first;
                out[i].second += t.second;
            }
        }
    }

    static void fftInv(const pair<double, double>* in, pair<double, double>* out, int n, int k = 1) {
        if (n == 1) {
            *out = *in;
        } else {
            n >>= 1;
            fftInv(in, out, n, k << 1);
            fftInv(in + k, out + n, n, k << 1);
            for (int i = 0; i < n; i++) {
                pair<double, double> t(out[i + n].first * w[i + n].first + out[i + n].second * w[i + n].second,
                    out[i + n].second * w[i + n].first - out[i + n].first * w[i + n].second);

                out[i + n].first = out[i].first - t.first;
                out[i + n].second = out[i].second - t.second;
                out[i].first += t.first;
                out[i].second += t.second;
            }
        }

        if (k == 1) {
            for (int i = 0; i < n; i++) {
                out[i].first /= n;
                out[i].second /= n;
            }
        }
    }

    //---

    static pair<double, double> A[MaxN], B[MaxN];
    static pair<double, double> C[MaxN], D[MaxN];

    static vector<int> multiplySlow(const vector<int>& a, const vector<int>& b) {
        vector<int> res(a.size() + b.size() - 1);
        for (int i = 0; i < int(a.size()); i++) {
            for (int j = 0; j < int(b.size()); j++) {
                res[i + j] = int((res[i + j] + 1ll * a[i] * b[j]) % mod);
            }
        }
        return res;
    }

    static vector<int> multiply(const vector<int>& left, const vector<int>& right) {
        int sizeL = int(left.size());
        int sizeR = int(right.size());
        int sizeDst = sizeL + sizeR - 1;

        if (min(sizeL, sizeR) <= 256)
            return multiplySlow(left, right);

        init();

        static const int shift = 15;
        static const int mask = (1 << shift) - 1;

        int size = 1;
        while (size < sizeDst)
            size <<= 1;
        int sizeMask = size - 1;

        for (int i = 0; i < size; i++) {
            if (i < sizeL) {
                A[i].first = left[i] & mask;
                A[i].second = left[i] >> shift;
            } else {
                A[i].first = 0;
                A[i].second = 0;
            }
            if (i < sizeR) {
                B[i].first = right[i] & mask;
                B[i].second = right[i] >> shift;
            } else {
                B[i].first = 0;
                B[i].second = 0;
            }
        }

        fft(A, C, size);
        fft(B, D, size);
        for (int i = 0; i < size; i++) {
            int j = (size - i) & sizeMask;
            pair<double, double> c0(C[i].first + C[j].first, C[i].second - C[j].second);
            pair<double, double> c1(C[i].first - C[j].first, C[i].second + C[j].second);
            pair<double, double> d0(D[i].first + D[j].first, D[i].second - D[j].second);
            pair<double, double> d1(D[i].first - D[j].first, D[i].second + D[j].second);
            //A[i] = c0 * d0 - point(0, 1) * c1 * d1;
            A[i].first = (c0.first * d0.first - c0.second * d0.second) + (c1.first * d1.second + c1.second * d1.first);
            A[i].second = (c0.first * d0.second + c0.second * d0.first) - (c1.first * d1.first - c1.second * d1.second);
            //B[i] = c0 * d1 + d0 * c1;
            B[i].first = (c0.first * d1.first - c0.second * d1.second) + (d0.first * c1.first - d0.second * c1.second);
            B[i].second = (c0.first * d1.second + c0.second * d1.first) + (d0.first * c1.second + d0.second * c1.first);
        }

        fft(A, C, size);
        fft(B, D, size);
        std::reverse(C + 1, C + size);
        std::reverse(D + 1, D + size);

        static const int SCALE2 = (1 << 2 * shift);
        static const int SCALE = (1 << shift);

        vector<int> res(sizeDst);

        int t = 4 * size;
        for (int i = 0; i < sizeDst; i++) {
            res[i] = int((llround(C[i].first / t) % mod
                + llround(D[i].second / t) % mod * SCALE
                + llround(C[i].second / t) % mod * SCALE2) % mod);
        }
        normalize(res);

        return res;
    }

    //--- extended operations (low order first)

    static void normalize(vector<int>& poly) {
        while (!poly.empty() && poly.back() == 0)
            poly.pop_back();
    }


    static int deg(const vector<int>& poly) {
        return int(poly.size()) - 1;
    }

    // get same polynomial mod x^k
    static vector<int> modXK(vector<int> poly, int k) {
        poly.resize(min(k, int(poly.size())));
        return poly;
    }

    // multiply by x^k
    static vector<int> mulXK(const vector<int>& poly, int k) {
        vector<int> res(k);
        res.insert(res.end(), begin(poly), end(poly));
        return res;
    }

    // return modXK(r).divXK(l)
    static vector<int> substr(const vector<int>& poly, int l, int r) {
        l = min(l, int(poly.size()));
        r = min(r, int(poly.size()));
        return vector<int>(begin(poly) + l, begin(poly) + r);
    }

    // reverses and leaves only n terms
    static vector<int> reverse(const vector<int>& poly, int n, bool rev = false) {
        vector<int> res(poly);
        if (rev) {   // if rev == true then tail goes to head
            res.resize(max(n, int(res.size())));
            std::reverse(res.begin(), res.end());
        } else {
            std::reverse(res.begin(), res.end());
            res.resize(max(n, int(res.size())));
        }
        return res;
    }


    static vector<int>& add(vector<int>& lhs, const vector<int>& rhs) {
        lhs.resize(max(lhs.size(), rhs.size()));
        for (size_t i = 0; i < rhs.size(); i++) {
            lhs[i] += rhs[i];
            if (lhs[i] >= mod)
                lhs[i] -= mod;
        }
        normalize(lhs);
        return lhs;
    }

    static vector<int> copyAndAdd(const vector<int>& lhs, const vector<int>& rhs) {
        vector<int> res(max(lhs.size(), rhs.size()));
        for (size_t i = 0; i < res.size(); i++) {
            res[i] = lhs[i] + rhs[i];
            if (res[i] >= mod)
                res[i] -= mod;
        }
        normalize(res);
        return res;
    }

    static vector<int>& subtract(vector<int>& lhs, const vector<int>& rhs) {
        lhs.resize(max(lhs.size(), rhs.size()));
        for (size_t i = 0; i < rhs.size(); i++) {
            lhs[i] -= rhs[i];
            if (lhs[i] < 0)
                lhs[i] += mod;
        }
        normalize(lhs);
        return lhs;
    }

    static vector<int> copyAndSubtract(const vector<int>& lhs, const vector<int>& rhs) {
        vector<int> res(lhs);
        res.resize(max(lhs.size(), rhs.size()));

        for (size_t i = 0; i < rhs.size(); i++) {
            res[i] -= rhs[i];
            if (res[i] < 0)
                res[i] += mod;
        }
        normalize(res);
        return res;
    }


    // when divisor or quotient is small
    // returns quotiend and remainder of a / b
    static pair<vector<int>, vector<int>> divmodSlow(vector<int> a, const vector<int>& b) {
        vector<int> res;
        while (a.size() >= b.size()) {
            res.push_back(a.back() / b.back());
            if (res.back() != 0) {
                for (int i = 0; i < int(b.size()); i++) {
                    a[a.size() - i - 1] = int((a[a.size() - i - 1] - 1ll * res.back() * b[b.size() - i - 1]) % mod);
                    if (a[a.size() - i - 1] < 0)
                        a[a.size() - i - 1] += mod;
                }
            }
            a.pop_back();
        }
        std::reverse(begin(res), end(res));
        return { res, a };
    }

    // returns quotiend and remainder of a / b
    static pair<vector<int>, vector<int>> divmod(const vector<int>& a, const vector<int>& b) {
        if (deg(a) < deg(b))
            return { vector<int>{0}, a };

        int d = deg(a) - deg(b);
        if (min(d, deg(b)) < 256) {
            return divmodSlow(a, b);
        }

        vector<int> D = reverse(modXK(multiply(reverse(a, d + 1), inverse(reverse(b, d + 1), d + 1)), d + 1), d + 1, true);
        return { D, copyAndSubtract(a, multiply(D, b)) };
    }

    //---

#if 1
    // get inverse series mod x^n
    static vector<int> inverse(const vector<int>& poly, int n) {
        //assert(!poly.empty());

        vector<int> res{ modInv(poly[0]) };
        int a = 1;
        while (a < n) {
            vector<int> C = substr(multiply(res, modXK(poly, 2 * a)), a, 2 * a);
            subtract(res, mulXK(modXK(multiply(res, C), a), a));
            a *= 2;
        }
        return modXK(res, n);
    }
#else
    // low order first
    static vector<int> inverse(const vector<int>& a, int n) {
        //assert(!a.empty());

        vector<int> b = { modInv(a[0]) };
        while (int(b.size()) < n) {
            vector<int> a_cut(a.begin(), a.begin() + min(a.size(), b.size() << 1));
            vector<int> x = multiply(square(b), a_cut);
            b.resize(b.size() << 1);
            for (int i = int(b.size()) >> 1; i < int(min(x.size(), b.size())); i++)
                b[i] = mod - x[i];
        }
        b.resize(n);
        return b;
    }
#endif

    static vector<int> inverse(const vector<int>& a) {
        return inverse(a, int(a.size()));
    }
};

template <int mod, int MaxN>
pair<double, double> PolyFFTMod3<mod, MaxN>::w[MaxN];

template <int mod, int MaxN>
bool PolyFFTMod3<mod, MaxN>::initialized = false;

template <int mod, int MaxN>
pair<double, double> PolyFFTMod3<mod, MaxN>::A[MaxN];

template <int mod, int MaxN>
pair<double, double> PolyFFTMod3<mod, MaxN>::B[MaxN];

template <int mod, int MaxN>
pair<double, double> PolyFFTMod3<mod, MaxN>::C[MaxN];

template <int mod, int MaxN>
pair<double, double> PolyFFTMod3<mod, MaxN>::D[MaxN];


template <typename T, int mod = 1'000'000'007>
struct LinearRecurrence {
    vector<T> X;    // initial values
    vector<T> C;    // coefficients of linear recurrence relation

    LinearRecurrence() {
    }

    explicit LinearRecurrence(const vector<T>& x) {
        build(x);
    }

    // Berlekamp-Massey, O(N*K + N*logMOD), N = the number of initial Xs
    // - N(the size of x) >= 2*K
    void build(const vector<T>& x) {
        int N = int(x.size());

        this->X = x;
        C = vector<T>(N);

        int size = 0, m = 0;
        vector<T> B(N);

        C[0] = B[0] = 1;
        T b = 1;
        for (int i = 0; i < N; i++) {
            ++m;

            T d = x[i];
            for (int j = 1; j <= size; j++) {
                d += T(1ll * C[j] * x[i - j] % mod);
                if (d >= mod)
                    d -= mod;
            }
            if (d == 0)
                continue;

            auto t = C;
            T coef = T(1ll * d * modInv(b) % mod);
            for (int j = m; j < N; j++) {
                C[j] -= T(1ll * coef * B[j - m] % mod);
                if (C[j] < 0)
                    C[j] += mod;
            }
            if (2 * size > i)
                continue;

            size = i + 1 - size;
            B = t;
            b = d;
            m = 0;
        }
        C.resize(size + 1);
        for (int i = 1; i <= size; i++) {
            if (C[i] > 0)
                C[i - 1] = mod - C[i];
            else
                C[i - 1] = C[i];
        }
        C.pop_back();
    }

#if 0
    // Kitamasa, O(K^2*logN)
    T getNth(long long n) {
        if (n < int(X.size()))
            return X[n];

        int m = int(C.size());
        if (m == 0)
            return T(0);

        vector<T> s(m), t(m);
        s[0] = 1;
        if (m != 1)
            t[1] = 1;
        else
            t[0] = C[0];

        for (; n; n >>= 1) {
            if (n & 1)
                s = mult(s, t);
            t = mult(t, t);
        }

        long long res = 0;
        for (int i = 0; i < m; i++)
            res += 1ll * s[i] * X[i] % mod;

        return T(res % mod);
    }
#else
    // Kitamasa, O(K*logK*logN)
    T getNth(long long n) {
        if (n < int(X.size()))
            return X[n];

        int m = int(C.size());
        if (m == 0)
            return T(0);

        vector<int> s{ 1 };     // result
        vector<int> t{ 0, 1 };  // xn = x^1, x^2, x^4, ...
        vector<int> f(C.size() + 1);
        f.back() = 1;
        for (int i = 0; i < m; i++)
            f[i] = MOD - C[m - i - 1];

        for (; n; n >>= 1) {
            if (n & 1) {
                s = move(PolyFFTMod3<MOD>::divmod(PolyFFTMod3<MOD>::multiply(s, t), f).second);
            }
            t = move(PolyFFTMod3<MOD>::divmod(PolyFFTMod3<MOD>::multiply(t, t), f).second);
        }

        long long res = 0;
        for (int i = 0; i < m; i++)
            res += 1ll * s[i] * X[i] % mod;

        return T(res % mod);
    }
#endif

    static T guessNthTerm(const vector<T>& x, long long n) {
        if (n < (long long)x.size())
            return x[n];

        LinearRecurrence<T, mod> rec(x);
        return rec.getNth(n);
    }

private:
    vector<T> mult(const vector<T>& v, const vector<T>& w) {
        int m = int(v.size());
        vector<T> t(2 * m);

        //TODO: optimize with FFT for big K
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < m; k++) {
                t[j + k] += T(1ll * v[j] * w[k] % mod);
                if (t[j + k] >= mod)
                    t[j + k] -= mod;
            }
        }
        for (int j = 2 * m - 1; j >= m; j--) {
            for (int k = 1; k <= m; k++) {
                t[j - k] += T(1ll * t[j] * C[k - 1] % mod);
                if (t[j - k] >= mod)
                    t[j - k] -= mod;
            }
        }
        t.resize(m);
        return t;
    }
};

const int MAXN = 1'000;

int gN, gX;
vector<int> gE[MAXN + 1];

ll dfsSlow(int u, int parent, int xx) {
    ll res = 0;
    for (int x = 1; x <= xx; x++) {
        ll t = 1;
        for (int v : gE[u]) {
            if (v == parent)
                continue;

            t = t * dfsSlow(v, u, x) % MOD;
        }
        res += t;
        if (res >= MOD)
            res -= MOD;
    }

    return res;
}

ll solveSlow() {
    return dfsSlow(0, -1, gX);
}


vector<int> gDP[MAXN + 1];
void dfs(int u, int parent, int XX) {
    vector<int> children;
    for (int v : gE[u]) {
        if (v == parent)
            continue;
        dfs(v, u, XX);
        children.push_back(v);
    }

    gDP[u] = vector<int>(XX + 1);
    for (int x = 1; x <= XX; x++) {
        ll t = 1;
        for (int v : children) {
            t = t * gDP[v][x] % MOD;
        }
        gDP[u][x] = int(t + gDP[u][x - 1]);
        if (gDP[u][x] >= MOD)
            gDP[u][x] -= MOD;
    }

    for (int v : children) {
        vector<int>().swap(gDP[v]);
    }
}

ll solve() {
    dfs(0, -1, gX);
    return gDP[0][gX];
}

ll solveFast() {
    int X = gN * 2 + 2;
    dfs(0, -1, min(X, gX));

    if (gX <= X)
        return gDP[0][gX];

    return LinearRecurrence<int, MOD>::guessNthTerm(gDP[0], gX);
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T-- > 0) {
        cin >> gN >> gX;

        int u, v;
        for (int i = 1; i < gN; i++) {
            cin >> u >> v;
            --u; --v;
            gE[u].push_back(v);
            gE[v].push_back(u);
        }

        //cout << solveSlow() << '\n';
        //cout << solve() << '\n';
        cout << solveFast() << '\n';

        if (T > 0) {
            for (int i = 0; i < gN; i++)
                gE[i].clear();
        }
    }

    return 0;
}
