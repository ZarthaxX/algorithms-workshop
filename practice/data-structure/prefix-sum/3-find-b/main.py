# https://codeforces.com/contest/1923/problem/C
import math
 
def solve():
    n, q = map(int,input().split(' '))
    nums = list(map(int,input().split(' ')))
   
    ones = [0 for i in range(n+1)]
    sum =  [0 for i in range(n+1)]
    for i in range(1, n+1):
        ones[i] = ones[i-1] + (1 if nums[i-1] == 1 else 0)
        sum[i] = sum[i-1] + nums[i-1]
 
    for _ in range(q):
        l,r = map(int,input().split(' '))
        if l == r:
            print("NO")
            continue
 
        onesInRange = ones[r] - ones[l-1]
        sumInRange = sum[r] - sum[l-1]
 
        # para todos los numeros que son 1, lo minimo que podemos poner es 2
        # para todos los que son > 1, lo minimo que podemos poner es 1
        # luego basta ver si esta suma es menor a la del rango, y si es asi sabemos que podriamos llevarlo a sumar lo mismo respetando todo
        if (2*onesInRange + (r-l+1) - onesInRange) <= sumInRange:
            print("YES")
        else:
            print("NO")
 
testCases = int(input())
for i in range(testCases):
    solve()