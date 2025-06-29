import math
input=int(input("Enter the number:"))

if input<=1:
    print("Not prime")
    
else:    
    for i in range(2,int(math.sqrt(input))+1):
        if input%i==0:
            print("Not prime")
            break
        else:
            print("Prime")