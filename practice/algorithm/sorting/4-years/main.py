def solve():
    n = int(input())
    events = dict()
    for i in range(n):
        s, e = map(int, input().split(' '))
        if s not in events:
            events[s] = 0
        events[s]+=1
        if e not in events:
            events[e] = 0
        events[e]-=1

    currentLives = 0
    maxLives = 0
    maxYear = 0
    for year, lives in sorted(events.items()):
        currentLives += lives
        if currentLives > maxLives:
            maxLives = currentLives
            maxYear = year
    
    print(maxYear, maxLives)
solve()
