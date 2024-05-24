import math

a, b = map(int, input().split(' '))
print(math.ceil((math.log(a)-math.log(b)) / (math.log(2)-math.log(3))+10e-10))