// https://codeforces.com/problemset/problem/1744/C
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

void solve()
{
    //   n,m,k = map(int, input().split(' '))
    // a = list( map(int, input().split(' ')))
    // b = list( map(int, input().split(' ')))
    
    int n,m,k;
    cin>>n>>m>>k;
    vector<int> a(n, 0),b(m,0);
    for(int &e : a){
        cin >> e;
    }
    for(int &e : b){
        cin >> e;
    }

    map<int,int> bset,aset;
    for(int e : b){
        if(bset.find(e) == bset.end())
            bset[e] = 0;
        bset[e] += 1;
    }
 
    for(int e : a){
        if(aset.find(e) == aset.end())
            aset[e] = 0;
        if(bset.find(e) == bset.end())
            bset[e] = 0;
    }
    
    int matchings = 0;
    for(int i = 0; i < m;i++){
        int e = a[i];
        aset[e] += 1;

        if(aset[e] <= bset[e])
            matchings++;
    }

    int valids = 0;
    if(matchings >= k)
        valids++;

    for(int i = m; i < n;i++){
        int last = a[i-m];
        int next = a[i];
        if(aset[last] <= bset[last])
            matchings--;
        aset[last]--;
        if(aset[next] < bset[next])
            matchings++;
        aset[next]++;

        if(matchings >= k)
            valids++;
    }

    cout<<valids<<endl;
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