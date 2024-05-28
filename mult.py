a,b=map(int,input().split())
result=0
for i in str(a):
	digit_a=int(i)
	for j in str(b):
		digit_b=int(j)
		result+=digit_a*digit_b
print(result)