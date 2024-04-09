contests = int(input())
 
# parseamos la lista de problemas por competencia
problemsByContest = list(map(lambda s: int(s), input().split(' ')))
# ordenamos las competencias por cantidad de problemas, para recorrer una sola vez todos
problemsByContest.sort()
 
days = 0
for i in range(0, contests):
    if problemsByContest[i] > days:
        days+=1
 
print(days)