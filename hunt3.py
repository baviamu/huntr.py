tm=int(input())
q=list(map(int,input().split()))
on=[]
for i in range(tm):
    if q[i]==l:
        on.append(str(q[i]))
        on.sort()
if len(on)==0:
    print("-1")
else:
    print(" ".join(on))
