ba=int(input())
vi=list(map(int,input().split()[:ba]))
for c in range(len(vi)):
    if((c%2==0)and(vi[c]%2!=0)or(c%2!=0)and(vi[c]%2==0)):
        print(v[i],end=" ")
