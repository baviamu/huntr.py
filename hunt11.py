t=int(input())
g=[]
for i in range (0,t):
	g.append(input())
r=len(g[0])
o=""
for i in range (0,r):
	z=g[0][i]
	u=0
	for j in range (0,t):
		if(z!=g[j][i]):
			u=1
	if(u==0):
		o=o+z
	else:
		break
print(o)
