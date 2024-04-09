package main

import "fmt"

func solve() {
	var problemsCount int
	fmt.Scan(&problemsCount)
	var problems string
	fmt.Scan(&problems)

	balloons := 0
	// inicializamos la lista de problemas con 26 porque hay 26 como maximo
	problemsSolved := make([]bool, 26)
	for _, p := range problems {
		// transformamos el caracter a un numero que podamos mapear al array
		idx := int(p - 'A')
		if problemsSolved[idx] {
			balloons++
		} else {
			problemsSolved[idx] = true
			balloons += 2
		}
	}

	fmt.Println(balloons)
}

func main() {
	var testCases int
	fmt.Scan(&testCases)
	for i := 0; i < testCases; i++ {
		solve()
	}
}
