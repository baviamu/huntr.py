bu,ba = map(int,input().split())
bo2 = list(map(int,input().split()))
bo3 = list(map(int,input().split()))
y =1
for r in bo3:
    if r not in bo2:
        print('NO')
        y = 0
        break
if(y):
    print('YES')
