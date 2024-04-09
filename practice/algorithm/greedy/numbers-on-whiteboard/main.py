# https://codeforces.com/problemset/problem/1430/C
import math

# vamos sumando siempre los 2 numeros mas grandes, para arrastrar lo menos posible hacia adelante
def solve():
    n = int(input())
    sum = n
    ops = []
    for i in range(n-1, 0, -1):
        ops.append((sum, i))
        sum = math.ceil((sum + i) / 2)

    print(sum)
    for (a, b) in ops:
        print(a, b)

testCases = int(input())

for i in range(testCases):
    solve()