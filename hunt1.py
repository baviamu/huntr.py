try:
	ed=int(input())
	array=list(map(int,input().split()))
	wq=[]
	for c in array:
		if array.count(c)>1:
			if c not in wq:
				wq.append(c)
	print(*wq)
	if len(wq)==0:
		print("unique")
except ValueError:
	print("invalid")
