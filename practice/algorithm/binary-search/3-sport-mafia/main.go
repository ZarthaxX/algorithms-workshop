package main

import (
	"fmt"
)

func calculateCandies(n, s int64) int64 {
	notEaten := n - s
	return notEaten*(notEaten-1)/2 - s
}

func solve() {
	var n, k int64
	fmt.Scan(&n, &k)

	sMin := int64(0)
	sMax := int64(n)
	for sMin < sMax {
		sMid := (sMin + sMax) / 2
		if calculateCandies(n, sMid) >= k {
			sMin = sMid + 1
		} else {
			sMax = sMid
		}
	}

	fmt.Println(sMin)
}

func main() {
	solve()
}
