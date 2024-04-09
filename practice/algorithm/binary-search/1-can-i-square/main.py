

def calculateWater(cols ,h):
	sum=0
	for c in cols:
		if h > c:
			sum += (h - c)
	return sum

def solve():
	n = int(input())
	total = sum(map(int, input().split(' ')), 0)

	sMin = 0
	sMax = total
	while sMin < sMax:
		sMid = int((sMin + sMax) / 2)
		square = sMid * sMid
		if square < total:
			sMin = sMid + 1
		else:
			sMax = sMid


	if sMax*sMax==total:
		print("YES")
	else:
		print("NO")

tests = int(input())
for _ in range(tests):
	solve()