package main

import (
	"fmt"
)

func solve() {
	var a, b int64
	fmt.Scan(&a, &b)

	// como maximo tenemos una cantidad de equipos igual a la suma de programadores y matematicos / 4
	teams := (a + b) / 4

	// la cantidad de equipos maxima esta limitada porque necesitamos si o si para cada uno un programador y un matematico
	if a < teams {
		teams = a
	}
	if b < teams {
		teams = b
	}

	fmt.Println(teams)
}

func main() {
	var tests int
	fmt.Scan(&tests)
	for i := 0; i < tests; i++ {
		solve()
	}
}
