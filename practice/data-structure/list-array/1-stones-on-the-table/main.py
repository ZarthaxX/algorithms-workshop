n = int(input())
stones = input()

toRemove = 0
for i in range(1,n):
    if stones[i-1] == stones[i]:
        toRemove += 1

print(toRemove)