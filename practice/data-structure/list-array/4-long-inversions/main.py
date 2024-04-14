def isPossible(list, k):
    inverts = [False for _ in list]

    inverted = False
    for i in range(len(list)-k):
        if inverts[i]:
            inverted = not inverted

        v = list[i]
        if inverted:
            v = not v

        if not v:
            inverts[i+k] = True
            inverted = not inverted

    zeroes = False
    ones = False
    for i in range(len(list)-k, len(list)):
        if inverts[i]:
            inverted = not inverted

        v = list[i]
        if inverted:
            v = not v

        if v:
            ones = True
        else:
            zeroes = True

    return not(zeroes and ones)
            
def solve():
    n = int(input())
    l = list( map(lambda x: True if x=='1' else False, input()))
    
    best = 0
    for i in range(1,n+1):
        if isPossible(l, i):
            best = i

    print(best)

testCases = int(input())

for i in range(testCases):
    solve()
