package main

import (
	"fmt"
)

func solve() {
	var sushiCount int
	fmt.Scan(&sushiCount)
	pieces := make([]int, sushiCount)
	for i, _ := range pieces {
		fmt.Scan(&pieces[i])
	}

	compressed := []int{0}
	currentType := 1
	for _, p := range pieces {
		if p == currentType {
			compressed[len(compressed)-1]++
		} else {
			currentType = p
			compressed = append(compressed, 1)
		}
	}

	maxSubsegment := 0
	for i := 0; i < len(compressed)-1; i++ {
		min := compressed[i]
		if compressed[i+1] < min {
			min = compressed[i+1]
		}

		if 2*min > maxSubsegment {
			maxSubsegment = 2 * min
		}
	}

	fmt.Println(maxSubsegment)
}

func main() {
	solve()
}
