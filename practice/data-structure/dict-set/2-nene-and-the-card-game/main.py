t = int(input())

for _ in range(t):
    n = int(input())

    seen = [0 for _ in range(n+1)] # dict for seen cards

    totalPoints = 0
    nums = list(map(int, input().split(' ')))
    for num in nums:
        seen[num]+=1

        if seen[num] == 2:
            totalPoints += 1

    print(totalPoints)