// https://codeforces.com/problemset/problem/1669/F
#include <iostream>
#include <map>
#include <vector>

using namespace std;

void solve()
{
    int candyCount;
    cin >> candyCount;

    vector<int> candies(candyCount, 0);
    for (int i = 0; i < candyCount; i++)
    {
        cin >> candies[i];
    }

    int a = 0;
    int b = candyCount - 1;
    long long aWeight = 0, bWeight = 0;
    long long bestCandyCount = 0;
    while (a <= b)
    {
        if (aWeight < bWeight)
        {
            aWeight += candies[a];
            a++;
        }
        else
        {
            bWeight += candies[b];
            b--;
        }

        if (aWeight == bWeight)
        {
            bestCandyCount = a + (candyCount - 1 - b);
        }
    }

    cout << bestCandyCount << endl;
}

int main()
{
    int testCases;
    cin >> testCases;

    for (int i = 0; i < testCases; i++)
    {
        solve();
    }

    return 0;
}