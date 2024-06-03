def solve():
    _,c = map(int, input().split(' '))
    planetsOrbit = list(map(int, input().split(' ')))

    planetsByOrbit = dict()
    for orbit in planetsOrbit:
        if orbit not in planetsByOrbit:
                planetsByOrbit[orbit] = 0

        planetsByOrbit[orbit]+=1
        
    totalCost = 0
    for _, planets in planetsByOrbit.items():
        totalCost += min(planets, c)
            
    print(totalCost)
    
testCases = int(input())

for i in range(testCases):
    solve()
