
def factorial(x):
	tot=1
	while x>0:
		tot*=x
		x=x-1
	return tot
print factorial(5)
