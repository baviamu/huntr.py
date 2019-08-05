mn1=list(map(str,input()))
st1=l1=0
for g in range(0,len(mn1)-1):
  f=mn1[g]
  if int(f)!=0:
   for k in range(g+1,g+2):
    f=f+mn1[k]
    if int(f)<27 and int(f)>0: st1=st1+1
    elif int(f)==0: st1=st1-1
    else: break
if st1!=1: l1=st1%2
print(st1+l1+1)
