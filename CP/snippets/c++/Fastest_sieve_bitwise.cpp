// --------------------------------------------
// https://codeforces.com/blog/entry/75852
// ---------------------------------------------



// I know sieve up to 10^8
// You can use std::bitset::_Find_next(bit) to find next prime.


#pragma GCC optimize("Ofast")
#pragma GCC target("avx")
#include <bits/stdc++.h>
const int NMAX = (int)1e8;
std::bitset<NMAX> bits;
int main() {
    bits.set();
    bits[0] = bits[1] = 0;
    for (int i = 2; i * i <= NMAX; i++) {
        if (bits[i]) {
            for (int j = i * i; j <= NMAX; j += i) bits[j] = 0;
        }
    }
    //iterate over primes
    int64_t sum(0);
    int cnt(0);
    for (int p = bits._Find_first(); p < bits.size(); p = bits._Find_next(p)) {
        sum += p;
        cnt++;
    }
    assert(bits.count() == cnt);
    std::cout << "sum = " << sum << std::endl;
    std::cout << "cnt = " << cnt << std::endl;
    return 0;
}









// By pazengod
// not fastest but fastest clean short code

// Sieve using bitset
// Had some fun codegolfing it and making it skip even numbers.
// The skipping makes it be able to do 1e9 in 4.4 s on CF.
// https://ideone.com/zZGO5q

#include <bits/stdc++.h>
using namespace std;

const int NMAX = (int)1e8;
int main() {
    bitset<NMAX / 2> bits;
    bits.set();
    auto sum = 2LL;
    int cnt = 1;
    for (int i = 3; i / 2 < bits.size(); i = 2 * bits._Find_next(i / 2) + 1) {
        sum += i;
        ++cnt;
        for (auto j = (int64_t) i * i / 2; j < bits.size(); j += i)
            bits[j] = 0;
    }
    cout << "sum = " << sum << endl;
    cout << "cnt = " << cnt << endl;
    return 0;
}





//
// Fastest sieve
// by pazengod
// segmented sieve
// The fastest sieve I know of (a segmented sieve)
// takes around 1.6 s on CF for 1e9.
// https://ideone.com/FFIlTC

#include <bits/stdc++.h>
using namespace std;

const int MAXPR = (int)1e8;
void calcPrimes() {
    auto sum = 2LL;
    int cnt = 1;

    const int S = round(sqrt(MAXPR));
    vector<char> sieve(S + 1, true);
    vector<array<int, 2>> cp;
    for (int i = 3; i < S; i += 2) {
        if (!sieve[i])
            continue;
        cp.push_back({i, (i * i - 1) / 2});
        for (int j = i * i; j <= S; j += 2 * i)
            sieve[j] = false;
    }
    vector<char> block(S);
    int high = (MAXPR - 1) / 2;
    for (int low = 0; low <= high; low += S) {
        fill(block.begin(), block.end(), true);
        for (auto &i : cp) {
            int p = i[0], idx = i[1];
            for (; idx < S; idx += p)
                block[idx] = false;
            i[1] = idx - S;
        }
        if (low == 0)
            block[0] = false;
        for (int i = 0; i < S && low + i <= high; i++)
            if (block[i])
                ++cnt, sum += (low + i) * 2 + 1;
    };

    cout << "sum = " << sum << endl;
    cout << "cnt = " << cnt << endl;
}

int main() {
    calcPrimes();
    return 0;
}






//
// https://codeforces.com/blog/entry/75852?#comment-600818
// Block sieving up to 10^9 works 2.7s on CF.
// https://ideone.com/pNiP1M

#pragma GCC optimize("Ofast")
#pragma GCC target("avx")
#include <bits/stdc++.h>
using pii = std::pair<int, int>;
const int NMAX = (int)1e9;
const int SNMAX = (int)sqrt(NMAX) + 1;
std::bitset<NMAX + 1> bits;
int main() {
    bits[0] = bits[1] = 1;
    std::vector<pii> smallPrimes;
    for (int i = 2; i <= SNMAX; ++i) {
        if (!bits[i]) {
            smallPrimes.push_back({i, i * i});
            for (int j = i * i; j <= SNMAX; j += i) {
                bits[j] = 1;
            }
        }
    }
    const int blockSize = 1 << 18;
    for (int from = 0; from <= NMAX; from += blockSize) {
        int to = std::min(from + blockSize - 1, NMAX);
        for (pii& p : smallPrimes) {
            for (; p.second <= to; p.second += p.first) bits[p.second] = 1;
        }
    }
    bits.flip();
    //iterate over primes
    int64_t sum(0);
    int cnt(0);
    for (int p = bits._Find_first(); p < bits.size(); p = bits._Find_next(p)) {
        sum += p;
        cnt++;
    }
    assert(bits.count() == cnt);
    std::cout << "sum = " << sum << std::endl;
    std::cout << "cnt = " << cnt << std::endl;
    return 0;
}
