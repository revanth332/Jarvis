def gcd(a,b):
    if b%a ==0:
        return a
    return gcd(b%a,b)

t = int(input())
while t:
    a,b = [int(i) for i in input().split()]
    print(gcd(min(a,b),max(a,b)),(a*b)//gcd(min(a,b),max(a,b)))
    t-=1