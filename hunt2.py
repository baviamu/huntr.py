yp=int(input())
yp=list(map(int,input().split()))
yp.sort()
yp.reverse()
if yp[0]==0:
    print("0")
else:
    for h in yp:
        print(h,end='')
