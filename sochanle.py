n=int(input())
vaild=True
for i in range(len(str(n))):
	digit=int((str(n))[i])
	position = i+1
	if position %2 ==1:
		if digit %2 ==0:
			vaild=False
			break
	else:
		if digit %2==1:
			vaild =False 
			break 
if vaild:
	print("YES")
else:
	print("NO")