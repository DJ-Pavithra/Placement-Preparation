import math
def gcd(a,b):
    while b!= 0:
        a,b=b,a%b
    return a

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))

res=gcd(num1,num2)

# or

res2=math.gcd(num1,num2)
print(f"GCD using def: {res}")
print(f"GCD using math func: {res2}")







