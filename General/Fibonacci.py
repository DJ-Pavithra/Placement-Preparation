def fibonacci(n):
    i=0
    j=1
    
    print(i,j)
    
    for loop in range(2,n):
        next=i+j
        print(next)
        i=j
        j=next
        
input=int(input("Enter the n term:"))
fibonacci(input)