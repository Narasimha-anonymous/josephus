def is_pow2(n):
    while n!=2:
        if n==1:
            return True
        elif n%2==1 or n<1:
            return False
        n/=2
    return True
def nearest_pow2(n):
    while not is_pow2(n):
        n-=1
    return n
n=int(input())
x=nearest_pow2(n)
d=n-x
j=2*d+1
print(j)