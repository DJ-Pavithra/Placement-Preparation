def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    x=gcd(a,b)
    res=(a*b)/x
    return res

num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))

result=lcm(num1,num2)
print(f"LCM: {result}")
