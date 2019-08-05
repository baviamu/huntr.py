bav=int(input())
bob11=list(map(int,input().split()))
v1=max(bob11)
c,d=0,0
for o in range(0,len(bob11)-1):
  for p in range(o+1,len(bob11)):
    if abs(bob11[o]+bob11[p])<v1:
      c,d=bob11[o],bob11[p]
      v1=abs(c+d)
print(c,d)
