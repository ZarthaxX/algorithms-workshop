#include <iostream>
#include <map>

using namespace std;

void solve()
{
    int n, k;
    cin >> n >> k;

    map<int, pair<int, int>> stations;
    for (int i = 0; i < n; i++)
    {
        int station;
        cin >> station;
        if (!stations.count(station))
        {
            stations[station] = {i, i};
        }
        else
        {
            stations[station].second = i;
        }
    }

    for (int i = 0; i < k; i++)
    {
        int a, b;
        cin >> a >> b;
        if (stations.count(a) && stations.count(b) && stations[a].first < stations[b].second)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
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