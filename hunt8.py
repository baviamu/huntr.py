bav=int(input())
aru=input().split()
for m in range(len(aru)):
    for j in range(m+1,len(aru)):
        for u in range(j+1,len(aru)):
            if(int(aru[m])+int(aru[j])==int(aru[u])):
                print(aru[m],aru[j],aru[u])
