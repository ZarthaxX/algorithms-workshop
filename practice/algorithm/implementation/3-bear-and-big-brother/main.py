a, b = map(int, input().split(' '))

its = 0
while a <= b:
    a*=3
    b*=2
    its+=1

print(its)