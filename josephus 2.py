n=int(input())
a=0
while 2**a<=n:
	a+=1
d=n-(2**(a-1))
print(2*d+1)
