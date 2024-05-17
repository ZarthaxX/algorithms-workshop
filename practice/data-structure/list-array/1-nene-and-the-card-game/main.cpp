#pragma GCC optimize("Ofast")
#pragma GCC optimize("inline")
#pragma GCC optimize("omit-frame-pointer")
#pragma GCC optimize("unroll-loops")
#pragma comment(linker, "/stack:200000000")

#include <bitset>
#include <stdio.h>
#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stdint.h>
#include <string>
#include <cstring>
#include <math.h>
#include <set>
#include <limits>
#include <chrono>
#include <numeric>

#define pause system("pause")
#define endl "\n"
#define DBG(x) cerr << #x << " = " << (x) << "\n"
#define forn(i, n) for (int i = 0; i < n; i++)
#define forr(i, n) for (int i = n; i >= 0; i--)
#define fori(i, a, n) for (int i = a; i < n; i++)
#define forall(c, i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define clr(a, b) memset(a, b, sizeof a)
#define all(x) x.begin(), x.end()
#define present(c, x) ((c).find(x) != (c).end())
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define ppb(x) pop_back(x)
#define ppf(x) pop_front(x)
#define lwb(x) lower_bound(x)
#define upb(x) upper_bound(x)
#define sz(x) ((int)x.size())
#define umap unordered_map
#define ff first
#define ss second
#define count_ones(x) __builtin_popcountll(x)
#define first_one(x) __builtin_ffs(x)
#define leading0(x) __builtin_clz(x)
#define mp make_pair
using namespace std;
using namespace std::chrono;

typedef unsigned long long ULL;
typedef long long LL;
typedef long long int LLI;
typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef pair<LL, LL> PLL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<float> VF;
typedef vector<bool> VB;
typedef vector<string> VS;
typedef vector<char> VC;
typedef vector<LL> VLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
typedef vector<VPII> GRAPH;
typedef vector<VLL> ADY_MATRIX;

const double EPS = 1E-9;
const double PI = 3.1415926535897932384626433832795;
/*********************************************************************************************************************/

template <class T>
void debug(vector<T> vec)
{
	for (int i = 0; i < vec.size(); i++)
		cerr << vec[i] << " ";
	cerr << endl;
}
template <class T>
void debug(vector<vector<T>> vec)
{
	for (int i = 0; i < vec.size(); i++)
	{
		for (int ii = 0; ii < vec[i].size(); ii++)
			cerr << vec[i][ii] << " ";
		cerr << endl;
	}
}

constexpr int directions[8][2] = {{-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}};

#define ONLINE_JUDGE 1
#define IO_SPEEDUP

void solve()
{
	LL a,b,c;cin>>a>>b>>c;
	a--;b--;c--;

	LL l = 0;
	LL r = 10e8;

	while(l<r){

		LL m = (l+r)/2;
LL prevBullets = m-1;
		if(!(a >= prevBullets && b >= prevBullets && c >= prevBullets)){
			m = r;
			continue;
		}
		
		LL lives = (a+b+c-3*prevBullets-6*m);

		if(lives>0){
			m = l+1;
		}else if (lives < 0){
			m = r;
		} else {
			cout<<"YES"<<endl;
			return;
		}
	}

	cout<<"NO"<<endl;
}

int main()
{
#ifdef IO_SPEEDUP
	ios::sync_with_stdio(false);
	cin.tie(NULL);
#endif

	int testcases = 1;
	cin >> testcases;
	while (testcases-- != 0)
	{
		solve();
		// if(testcases != 0)cout << "---------- END OF TEST " << testcases << " -------------" << endl;
	}
}