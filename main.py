n,l = map(float, input().split(' '))
a = list(map(float, input().split(' ')))

a.sort()

best = max(a[0], l-a[-1])
for i in range(len(a)-1):
    best = max(best, (a[i+1]-a[i])/2)
    
print(best)
