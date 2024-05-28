import math
n=int(input())

def songuyento(m):
	if m in range(1,int(math.sqrt(m))+1):
		return True
	else:return False
results=[]
for _ in range(n):
	a,b=map(int,input().split())
	hieu=b**2-a**2
	if songuyento(hieu):
		results.append("YES")
	else:results.append("NO")
	for result in results:
		print(result)