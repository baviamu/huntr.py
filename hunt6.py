tg=int(input())
b=input("")
b=list(b.split(" "))
w=[]
for x in range(0,len(b)):
  for y in range(x+1,len(b)):
    if b[x]==b[y]:
      w.append(b[x])
if(len(w)==0):
  print("unique")
else:
  print(w[0])
