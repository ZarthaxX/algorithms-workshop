def solve():
    n,k = map(int, input().split(' '))
    players = list(map(int, input().split(' ')))
    
    currentWinner = players[0]
    streak = 0
    for i in range(1, n):
        nextPlayer = players[i]
        if nextPlayer > currentWinner:
            currentWinner = nextPlayer
            streak = 1
        else:
            streak+=1
        
        if streak == k:
            break

    print(currentWinner)
    
solve()