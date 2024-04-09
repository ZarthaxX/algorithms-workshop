

def calculateWater(cols ,h):
	sum=0
	for c in cols:
		if h > c:
			sum += (h - c)
	return sum

def solve():
	
	n, x = map(int, input().split(' '))
	cols = list(map(int, input().split(' ')))

	hMin = 0
	hMax = 10000000000
	while hMin < hMax:
		hMid = int((hMin + hMax) / 2)
		if calculateWater(cols, hMid) <= x:
			hMin = hMid + 1
		else:
			hMax = hMid

	print(hMin - 1)

tests = int(input())
for _ in range(tests):
	solve()