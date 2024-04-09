def solve():
	n,q = map(int, input().split(' '))
	nums = list(map(int, input().split(' ')))

	prefixSum = [0] * (len(nums)+1)
	prefixSum[0] = 0
	for i in range(1,len(nums)+1):
		prefixSum[i] = prefixSum[i-1] + nums[i-1]

	for i in range(q):
		l,r,k = map(int, input().split(' '))

		res = prefixSum[l-1] + (prefixSum[len(nums)] - prefixSum[r]) + k*(r-l+1)
		if res%2 == 1:
			print("YES")
		else:
			print("NO")

testCases = int(input())

for i in range(testCases):
    solve()
