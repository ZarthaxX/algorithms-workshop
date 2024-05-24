def solve():
    a,b,c = map(int, input().split(' '))
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")

testCases = int(input())

for i in range(testCases):
    solve()