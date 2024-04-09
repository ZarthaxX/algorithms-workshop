def solve():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    numsCopy = nums.copy()
    nums.sort()

    for i in range(len(nums)):
        if nums[i] % 2 != numsCopy[i] % 2:
             print("NO")
             return

    print("YES")

tests = int(input())
for _ in range(tests):
	solve()