t = int(input())

for i in range(t):
    n,a,b = map(int, input().split(' '))

    if 2*a < b:
        print(n*a)
    else:
        tot = b * int(n/2)
        if n % 2 == 1:
            tot += a
        print(tot)