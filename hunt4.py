m=int(input())
d1=input(" ")
d1=list(d1.split(' '))
a={}
for i in d1:
   if i in a:
      a[i]+=1
   else:
      a[i]=1
for key,value in a.items():
  if value==1:
     print(key)
