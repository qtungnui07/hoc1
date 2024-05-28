import math 
n=int(input())
count=0
for i in range(1,n+1):
	if n%i==0:
		count+=1
if count in range(1,int(math.sqrt(n)+1)):
	print("YES")
else:print("NO")
	