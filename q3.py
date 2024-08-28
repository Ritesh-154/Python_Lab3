a=int(input("enter first number : "))
b=int(input("enter second number : "))
def gcd(a,b):
    l1=[]
    l2=[]
    l3=[]
    for i in range(1,a+1):
        if a%i==0:
            l1.append(i)
    for i in range(1,b+1):
        if b%i==0:
            l2.append(i)
    for i in l1:
        if i in l2:
            l3.append(i)
    return max(l3)
def lcm(g,a,b):
    return (a*b)/g
g=gcd(a,b)
l=lcm(g,a,b)
print("gcd of ",a," and ",b," is ",g)
print("lcm of ",a," and ",b," is ",l)