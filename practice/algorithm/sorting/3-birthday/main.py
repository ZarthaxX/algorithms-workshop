def solve():
    _ = int(input())
    nums = list(map(int, input().split(' ')))
    nums.sort()

    # la estrategia es ordenar los numeros e ir poniendo balanceado de izquierda y derecha los numeros de mas grande a mas chico
    finalNums = []
    for i in range(len(nums)-1, -1, -1):
        if i%2==0:
            finalNums.append(nums[i])
        else:
            finalNums = [nums[i]] + finalNums

    for num in finalNums:
        print(num, end=" ")
    print()

solve()